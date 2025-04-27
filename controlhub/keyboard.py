import pyautogui
import time

from contextlib import contextmanager
from pynput.keyboard import Controller, Key
from typing import Union, Iterable

keyboard = Controller()


def click(
    x: int = None, y: int = None, button: str = "left", delay: float = 0.1
) -> None:
    """
    Simulates a mouse click at the given coordinates.

    Args:
        x (int, optional): X-coordinate. If None, uses current position.
        y (int, optional): Y-coordinate. If None, uses current position.
        button (str): Mouse button ('left', 'right', 'middle'). Defaults to 'left'.
    """
    current_pos = pyautogui.position()
    x = x if x is not None else current_pos.x
    y = y if y is not None else current_pos.y

    pyautogui.click(x, y, button=button)

    if delay > 0:
        time.sleep(delay)


def move(x: int = None, y: int = None) -> None:
    """
    Simulates mouse movement to the given coordinates.

    Args:
        x (int, optional): X-coordinate. If None, uses current position.
        y (int, optional): Y-coordinate. If None, uses current position.
    """
    current_pos = pyautogui.position()
    x = x if x is not None else current_pos.x
    y = y if y is not None else current_pos.y

    pyautogui.moveTo(x, y)


def drag(
    x: int = None,
    y: int = None,
    x1: int = None,
    y1: int = None,
    button: str = "left",
    duration: float = 0,
) -> None:
    """
    Simulates mouse dragging from one set of coordinates to another.

    Args:
        x (int, optional): Starting X-coordinate. If None, uses current position.
        y (int, optional): Starting Y-coordinate. If None, uses current position.
        x1 (int, optional): Ending X-coordinate. If None, uses current position.
        y1 (int, optional): Ending Y-coordinate. If None, uses current position.
        button (str): Mouse button ('left', 'right', 'middle'). Defaults to 'left'.
    """
    current_pos = pyautogui.position()
    start_x = x if x is not None else current_pos.x
    start_y = y if y is not None else current_pos.y
    end_x = x1 if x1 is not None else current_pos.x
    end_y = y1 if y1 is not None else current_pos.y

    # Move to start position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown(button=button)

    pyautogui.moveTo(start_x + 1, start_y + 1)
    pyautogui.moveTo(start_x, start_y)

    pyautogui.moveTo(end_x, end_y, duration=duration)

    pyautogui.mouseUp(button=button)


def get_position() -> tuple[int, int]:
    return pyautogui.position()


AnyKey = Union[str, Key]

def convert_keys(*keys: Union[AnyKey, Iterable[AnyKey]]) -> str:
    """
    Converts a list of keys to their corresponding classes.

    Args:
        *keys (Union[str, Key]): A list of keys to be converted.
    """
    special_keys = {
        "win": Key.cmd,
        "alt": Key.alt,
        "ctrl": Key.ctrl,
        "shift": Key.shift,
        "enter": Key.enter,
        "space": Key.space,
        "esc": Key.esc,
        "backspace": Key.backspace,
        "delete": Key.delete,
        "tab": Key.tab,
        "caps": Key.caps_lock,
        "numlock": Key.num_lock,
        "scrolllock": Key.scroll_lock,
        "printscreen": Key.print_screen,
        "pause": Key.pause,
        "insert": Key.insert,
        "home": Key.home,
        "pageup": Key.page_up,
        "pagedown": Key.page_down,
        "end": Key.end,
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right,
        **{f"f{i}": getattr(Key, f"f{i}") for i in range(1, 13)},
    }

    return [
        special_keys[k]
        if isinstance(k, str) and k in special_keys
        else convert_keys(*k)
        if isinstance(k, Iterable) and not isinstance(k, str)
        else k
        for k in keys
    ]

def press(*keys: Union[AnyKey, Iterable[AnyKey]], delay: float = 0.1) -> None:
    """
    Simulates key presses.

    Args:
        *keys: Sequence of keys to press.
    """

    keys = convert_keys(*keys)

    for key in keys:
        if isinstance(key, Iterable):
            for k in key:
                keyboard.release(k)
                keyboard.press(k)
            for k in key:
                keyboard.release(k)
            time.sleep(delay)

        else:
            keyboard.release(key)
            keyboard.press(key)
            keyboard.release(key)
            time.sleep(delay)


@contextmanager
def hold(keys: Union[AnyKey, Iterable[AnyKey]], delay: float = 0.1):
    """
    Simulates key presses.

    Args:
        *keys: Sequence of keys to press.
    """

    if not isinstance(keys, Iterable):
        keys = (keys,)

    keys = convert_keys(*keys)

    try:
        for key in keys:
            keyboard.release(key)
            keyboard.press(key)
        yield
    finally:
        for key in keys[::-1]:
            keyboard.release(key)

        if delay > 0:
            time.sleep(delay)


def write(text: str) -> None:
    """
    Simulates keyboard input of the given text.

    Args:
        text (str): Text to type.
    """
    keyboard.type(text)
