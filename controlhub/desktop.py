import os
import subprocess
import psutil
from typing import TypedDict, List
from time import sleep
from .keyboard import press, write
from .config import BASE_DELAY
from .search import search_best_lnk, index_programs

def cmd(command: str, popen=False) -> None:
    """
    Executes a command in the command line.

    Args:
        command (str): Command to execute.
    """
    if popen:
        subprocess.Popen(command, shell=True)
    else:
        os.system(command)


def open_file(path: str, delay: float = None) -> None:
    """
    Opens a file in the appropriate application after converting it to an absolute path.

    Args:
        path (str): Path to the file to open.
    """
    delay = delay or BASE_DELAY * 2
    absolute_path = os.path.abspath(path)

    if os.path.exists(absolute_path):
        if os.name == "nt":  # Windows
            press(["win", "r"])
            sleep(BASE_DELAY)
            write(absolute_path)
            sleep(BASE_DELAY)
            press("enter")
        elif os.name == "posix":  # Unix
            subprocess.call(("xdg-open", absolute_path))

        sleep(delay)
    else:
        print(f"File not found: {absolute_path}")


def run_program(prompt: str, delay: float = None, use_shortcuts: bool = True) -> str | None:
    """
    Runs a program without using gui, only indexed programs. Returns link to the program if found (on Windows, otherwise None).

    Args:
        prompt (str): Command to run.
    """
    
    delay = delay or BASE_DELAY * 4

    if os.name == "nt":  # Windows
        link = search_best_lnk(prompt, index_programs(), use_shortcuts=use_shortcuts)
        subprocess.Popen(link, shell=True)
    
    elif os.name == "posix":  # Unix
        link = None
        subprocess.Popen(prompt, shell=True)

    sleep(delay)
    return link
    

class ProcessInfo(TypedDict):
    pid: int
    name: str

def kill_process(fragment: str, kill: bool = True) -> List[ProcessInfo]:
    """
    Kills process by it's name fragment
    
    Args:
        fragment (str): Process name fragment
        kill (bool): Kill found processes or not
    
    Returns:
        List[ProcessInfo]: List of killed processes
    """
    killed_processes = []
    
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_info: ProcessInfo = process.info
            process_name = process_info['name']
            
            if fragment.lower() in process_name.lower():
                if kill:
                    process.kill()
                killed_processes.append(process_info)

        except psutil.NoSuchProcess:
            pass
    
    return killed_processes

def fullscreen(absolute: bool = False, delay: float = None) -> None:
    """
    Toggles the active window to fullscreen mode.

    Args:
        absolute (bool): If True, uses F11 for absolute fullscreen mode.
    """
    delay = delay or BASE_DELAY

    press(["win", "up"])
    sleep(delay)

    if absolute:
        press("f11")


def _check_os() -> bool:
    """
    Checks if the operating system is Windows.
    """
    if os.name != "nt":
        raise NotImplementedError("This function is only implemented for Windows.")


# Only for Windows
def switch_to_next_window(delay: float = None) -> None:
    """
    Switches to the next active window.
    """
    delay = delay or BASE_DELAY

    _check_os()

    press(["alt", "tab"])
    sleep(delay)


# Only for Windows
def switch_to_last_window(delay: float = None) -> None:
    """
    Switches to the last active window.
    """
    delay = delay or BASE_DELAY

    _check_os()

    press(["alt", "shift", "tab"])
    sleep(delay)


# Only for Windows
def reload_window(delay: float = None) -> None:
    """
    Reloads the active window.
    """
    delay = delay or BASE_DELAY

    _check_os()

    switch_to_next_window(delay)
    switch_to_next_window(delay)
