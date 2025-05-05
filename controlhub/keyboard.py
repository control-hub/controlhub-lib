import pyautogui
import time

from contextlib import contextmanager
from pynput.keyboard import Controller, Key
from typing import Union, Iterable
from .config import BASE_DELAY

keyboard = Controller()

special_keys = {
    "win": Key.cmd,
    "cmd": Key.cmd,
    "windows": Key.cmd,
    "alt": Key.alt,
    "lalt": Key.alt_l,
    "ralt": Key.alt_r,
    "ctrl": Key.ctrl,
    "lctrl": Key.ctrl_l,
    "rctrl": Key.ctrl_r,
    "shift": Key.shift,
    "lshift": Key.shift_l,
    "rshift": Key.shift_r,
    "enter": Key.enter,
    "space": Key.space,
    "esc": Key.esc,
    "escape": Key.esc,
    "backspace": Key.backspace,
    "del": Key.delete,
    "delete": Key.delete,
    "tab": Key.tab,
    "caps": Key.caps_lock,
    "capslock": Key.caps_lock,
    "num": Key.num_lock,
    "numlock": Key.num_lock,
    "scroll": Key.scroll_lock,
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
    **{f"f{i}": getattr(Key, f"f{i}") for i in range(1, 12 + 1)},
}


def click(
    x: int = None, y: int = None, button: str = "left", delay: float = None
) -> None:
    """
    Simulates a mouse click at the given coordinates.

    Args:
        x (int, optional): X-coordinate. If None, uses current position.
        y (int, optional): Y-coordinate. If None, uses current position.
        button (str): Mouse button ('left', 'right', 'middle'). Defaults to 'left'.
    """
    delay = delay or BASE_DELAY
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


def convert_keys(
    *keys: Union[AnyKey, Iterable[AnyKey]],
) -> Iterable[Union[AnyKey, Iterable[AnyKey]]]:
    """
    Converts a list of keys to their corresponding classes.

    Args:
        *keys (Union[str, Key]): A list of keys to be converted.
    """

    return [
        special_keys[k]
        if isinstance(k, str) and k in special_keys
        else convert_keys(*k)
        if isinstance(k, Iterable) and not isinstance(k, str)
        else k
        for k in map(
            lambda x: x.lower().replace("_", "")
            if isinstance(x, str) and x != "_"
            else x,
            keys,
        )
    ]


def press(*keys: Union[AnyKey, Iterable[AnyKey]], delay: float = None) -> None:
    """
    Presses keys on a keyboard.

    Args:
        *keys: Sequence of keys to press.
        delay (float): Little delay between keys, by default `BASE_DELAY` seconds

    Examples:
        press(["ctrl", "a"], "backspace")
        press(["Ctrl", "Alt", "Delete"])
        press("Caps_Lock", "caps")
    """
    delay = delay or BASE_DELAY
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
def hold(*keys: Union[AnyKey, Iterable[AnyKey]], delay: float = None):
    """
    Simulates key presses.

    Args:
        *keys: Sequence of keys to press.

    Examples:
        with hold("ctrl", "a"):
        with hold(["ctrl", "a"])
    """
    delay = delay or BASE_DELAY

    if len(keys) == 1:
        keys = keys[0]

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


def write(text: str, delay: float = None, enter_delay: float = None) -> None:
    """
    Simulates keyboard input of the given text.

    Args:
        text (str): Text to type.
        delay (float): Little delay after written text, by default 0 seconds
        enter_delay (float): Little delay between lines and enter presses, by default `BASE_DELAY` * 4 seconds
    """

    text_lines = text.split("\n")
    delay = delay or BASE_DELAY * 0
    enter_delay = enter_delay or BASE_DELAY * 4

    for i in range(len(text_lines)):
        line = text_lines[i]
        keyboard.type(line)

        if i != len(text_lines) - 1:
            press("enter", delay=enter_delay)

    if delay > 0:
        time.sleep(delay)
