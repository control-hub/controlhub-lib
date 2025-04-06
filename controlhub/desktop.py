import os
import subprocess
from time import sleep
from .keyboard import press, write
from typing import List, Dict


def open_file(path: str) -> None:
    """
    Opens a file in the appropriate application.

    Args:
        path (str): Path to the file to open.
    """
    if os.path.exists(path):
        if os.name == "nt": # Windows
            os.startfile(path)
        elif os.name == "posix": # Unix
            subprocess.call(("xdg-open", path))
    else:
        print(f"File not found: {path}")

def cmd(command: str) -> None:
    """
    Executes a command in the command line.

    Args:
        command (str): Command to execute.
    """
    subprocess.Popen(command, shell=True)


def run_program(program_name: str) -> None:
    """
    Runs a program in the command line.

    Args:
        program_name (str): Name of the program to run.
    """
    
    if os.name == "nt": # Windows
        press("win")
        sleep(0.1)
        write(program_name)
        sleep(0.1)
        press("enter")
    elif os.name == "posix": # Unix
        cmd(program_name)
    

def fullscreen(absolute: bool = False) -> None:
    """
    Toggles the active window to fullscreen mode.

    Args:
        absolute (bool): If True, uses F11 for absolute fullscreen mode.
    """
    from .keyboard import press

    press("win", "up")
    if absolute:
        press("f11")


