import os
import subprocess
from time import sleep
from .keyboard import press, write


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


def open_file(path: str, delay:float=0.2) -> None:
    """
    Opens a file in the appropriate application after converting it to an absolute path.

    Args:
        path (str): Path to the file to open.
    """
    absolute_path = os.path.abspath(path)
    
    if os.path.exists(absolute_path):
        if os.name == "nt": # Windows
            press(["win", "r"])
            sleep(0.1)
            write(absolute_path)
            sleep(0.1)
            press("enter")
        elif os.name == "posix": # Unix
            subprocess.call(("xdg-open", absolute_path))
        
        sleep(delay)
    else:
        print(f"File not found: {absolute_path}")

def run_program(program_name: str, shell: bool = False, delay: float=0.4) -> None:
    """
    Runs a program in the command line.

    Args:
        program_name (str): Name of the program to run.
    """
    
    if os.name == "nt" and not shell: # Windows
        press("win")
        sleep(0.1)
        write(program_name)
        sleep(0.1)
        press("enter")
    elif os.name == "posix" or shell: # Unix
        subprocess.Popen(program_name, shell=True)
    

def fullscreen(absolute: bool = False, delay: float=0.1) -> None:
    """
    Toggles the active window to fullscreen mode.

    Args:
        absolute (bool): If True, uses F11 for absolute fullscreen mode.
    """

    press(["win", "up"])
    if absolute:
        press("f11")

def _check_os(name: str = "nt") -> bool:
    """
    Checks if the operating system is Windows.
    """
    if os.name != "nt":
        raise NotImplementedError("This function is only implemented for Windows.")
    
# Only for Windows
def switch_to_next_window(delay: float=0.1) -> None:
    """
    Switches to the next active window.
    """
    _check_os()

    press(["alt", "tab"])
    sleep(delay)

# Only for Windows
def switch_to_last_window(delay: float=0.1) -> None:
    """
    Switches to the last active window.
    """
    _check_os()

    press(["alt", "shift", "tab"])
    sleep(delay)
    
# Only for Windows
def reload_window(delay: float=0.1) -> None:
    """
    Reloads the active window.
    """
    _check_os()

    switch_to_next_window(delay)
    switch_to_next_window(delay)