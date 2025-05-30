from functools import cache
import os
import subprocess

user_home = os.path.expanduser("~")

shortcuts = {
    "cmd": "Command Prompt",
    "powershell": "Windows PowerShell",
    "explorer": "File Explorer",
    "vscode": "Visual Studio Code",
}

index_list = [
    user_home + r"\AppData\Roaming\Microsoft\Windows\Start Menu",
    r"C:\ProgramData\Microsoft\Windows\Start Menu",
    user_home + r"\Desktop",
]

def fuzzy_score(query: str, target: str) -> int:
    query = query.lower()
    target = target.lower()
    score = 0
    t_index = 0
    in_sequence = False

    for q in query:
        found = False
        while t_index < len(target):
            if target[t_index] == q:
                if t_index == 0 or target[t_index - 1] in " _-/\\":
                    score += 10
                if in_sequence:
                    score += 5
                else:
                    score += 1
                in_sequence = True
                found = True
                t_index += 1
                break
            else:
                in_sequence = False
            t_index += 1
        if not found:
            return -1
    return score


def search_best_lnk(query: str, paths: list[str], use_shortcuts: bool = True) -> str | None:
    query_lower = query.lower()
    
    if use_shortcuts and query_lower in shortcuts:
        query_lower = shortcuts[query_lower]
    
    candidates = [(path, os.path.splitext(os.path.basename(path))[0]) for path in paths]
    matched = []

    # Direct
    for path, name in candidates:
        if name.lower().startswith(query_lower):
            matched.append((path, name, 1000))

    # Substring
    if not matched:
        for path, name in candidates:
            if query_lower in name.lower():
                matched.append((path, name, 500))

    # Fuzzy
    if not matched:
        for path, name in candidates:
            score = fuzzy_score(query, name)
            if score > 0:
                matched.append((path, name, score))

    if not matched:
        return None

    # Sort by score and length of name
    matched.sort(key=lambda x: (-x[2], len(x[1])))

    return matched[0][0]

@cache
def index_programs():
    """
    Returns a list of all .lnk files in the index list.
    """
    programs = []

    for path in index_list:
        for root, dirs, files in os.walk(path):
            for file in files:
                programs.append(os.path.join(root, file))

    return programs

def main():
    search_result = search_best_lnk(input("> "), index_programs())
    print(search_result)

    if input("open? (y/n): ") == "y":
        subprocess.Popen(search_result, shell=True)
    

if __name__ == "__main__":
    main()
