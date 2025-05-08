# ControlHub python package

**[Read this page in Russian / Читать на русском](README.ru.md)**

ControlHub is a Python automation library for Windows that provides simple APIs to control the desktop, simulate keyboard and mouse actions, and perform web-related tasks.

## Installation

Install the library via pip:

```bash
pip install controlhub
```

## Features

-   Open files and run programs
-   Simulate mouse clicks, movements, and drags
-   Simulate keyboard input and key combinations
-   Download files from the web
-   Open URLs in the default browser
-   Auto delay added to functions to prevent some errors
-   Run shell commands
-   Use context managers for holding keys
-   Manage data in a data.json file (ControlHub service)
-   Changing basic delay value by changing the environment variable `CH_DELAY`
-   Interact with controlhub's data right from script

> [!NOTE]
> The basic delay is 0.2 seconds by default, but it can be changed by changing the environment variable `CH_DELAY`. In controlhub core scripts `CH_DELAY` is 0.8 by default.

## API Reference & Usage Examples

## `controlhub.desktop`

Module to interact with windows pc via functions

### `open_file(path: str) -> None`

Open a file with the default application.

```python
from controlhub import open_file

open_file("C:\\Users\\User\\Documents\\file.txt")
open_file("example.pdf")
open_file("image.png")
```

### `cmd(command: str) -> None`

Execute a shell command asynchronously.

```python
from controlhub import cmd

cmd("notepad.exe")
cmd("dir")
cmd("echo Hello World")
```

### `run_program(program_name: str) -> None`

Search for a program by name and run it.

```python
from controlhub import run_program

run_program("notepad")
run_program("chrome")
run_program("word")
```

### `fullscreen(absolute: bool = False) -> None`

Maximize the current window. If `absolute=True`, toggle fullscreen mode (F11).

```python
from controlhub import fullscreen

fullscreen()
fullscreen(absolute=True)
fullscreen(absolute=False)
```

### `switch_to_next_window`

Switches to next window (only Windows): Alt + Tab

### `switch_to_last_window`

Switches to last window (only Windows): Alt + Shift + Tab

### `reload_window`

Makes `switch_to_next_window` 2 times to make current window active

## `controlhub.keyboard`

Module to interact with keyboard and mouse via functions

### `click(x: int = None, y: int = None, button: str = "left") -> None`

Simulate a mouse click at the given coordinates or current position.

```python
from controlhub import click

click()  # Click at current position
click(100, 200)  # Click at (100, 200)
click(300, 400, button="right")  # Right-click at (300, 400)
```

### `move(x: int = None, y: int = None) -> None`

Move the mouse to the given coordinates.

```python
from controlhub import move

move(500, 500)
move(0, 0)
move(1920, 1080)
```

### `drag(x: int = None, y: int = None, x1: int = None, y1: int = None, button: str = "left", duration: float = 0) -> None`

Drag the mouse from start to end coordinates.

```python
from controlhub import drag

drag(100, 100, 200, 200)
drag(300, 300, 400, 400, button="right")
drag(500, 500, 600, 600, duration=1.5)
```

### `get_position() -> tuple[int, int]`

Get the current mouse position.

```python
from controlhub import get_position

pos = get_position()
print(pos)

x, y = get_position()
print(f"Mouse is at ({x}, {y})")
```

### `press(*keys: Union[AnyKey, Iterable[AnyKey]]) -> None`

Simulate pressing and releasing keys.

```python
from controlhub import press

press(["ctrl", "c"])  # Copy
press(["ctrl", "v"])  # Paste

press(["ctrl", "c"], ["ctrl", "v"], "left") # Copy and paste in 1 line and press left arrow
```

### `hold(*keys: Union[str, Key])`

Context manager to hold keys during a block.

```python
from controlhub import hold, press

with hold("ctrl"):
    press("c")  # Ctrl+C

with hold("shift"):
    press("left")  # Select text

with hold(["ctrl", "alt"]):
    press("tab") # Ctrl+Alt+Tab, I

with hold("ctrl", "shift"):
    press("esc") # Ctrl+Shift+Escape
```

### `write(text: str) -> None`

Type the given text. Also supports \n.

```python
from controlhub import write

write("Hello, world!")
write("This is automated typing.")
write("ControlHub is awesome!")
write("from controlhub import write\nwrite(\"Hello, world\")")
```

## `controlhub.web`

Module to interact with internet via functions

### `download(url: str, directory: str = "download") -> None`

Download a file from a URL into a directory.

```python
from controlhub import download

download("https://example.com/file.zip")
download("https://example.com/image.png", directory="images")
download("https://example.com/doc.pdf", directory="docs")
```

### `open_url(url: str) -> None`

Open a URL in the default web browser.

```python
from controlhub import open_url

open_url("https://www.google.com")
open_url("github.com")  # Will prepend http://
open_url("https://stackoverflow.com")
```

## `controlhub.pocketbase`

Module to interact with pocketbase computer and execution records via functions

> [!IMPORTANT]
> Functions from this module can be executed only in controlhub scripts

### `get_execution() -> ExecutionResponse`

Returns execution from database

```python
from controlhub import get_execution

print(get_execution())
```

### `update_execution(data: ExecutionRecord) -> ExecutionResponse`

Updates execution in database and returns it

```python
from controlhub import update_execution

new_execution = {
    "status": "3",
    "duration": 20
}

print(update_execution(new_execution))
```

### `get_computer() -> ComputerResponse`

Returns computer from database

```python
from controlhub import get_computer

print(get_computer())
```

### `get_offline_computer() -> ComputerResponse`

Returns computer from local env variable `COMPUTER_JSON`

```python
from controlhub import get_offline_computer

print(get_offline_computer())
```

### `update_computer(data: ExecutionRecord) -> ExecutionResponse`

Updates computer in database and returns it

```python
from controlhub import update_computer

new_computer = {
    "data": {
        "weather": "clear",
        "mood": "good",
        "vscode installed": True
    }
}

print(update_computer(new_computer))
```

## `controlhub.json_storage`

### `JSONFile(file_path: str)`

Create a JSON-backed storage object to store and retrieve data, like a dictionary. All data is saved to a JSON file `file_path`. 

```python
from controlhub.json_storage import JSONFile

storage = JSONFile("mydata.json")
storage.set({"key": "value"})
print(storage.get())  # {"key": "value"}
```

### `JSONFile.get() -> dict`

Read and return all data from the file.

```python
print(storage.get())
# Output: {"key": "value"}
```

### `JSONFile.set(data: dict) -> None`

Completely replace the file contents.

```python
storage.set({"new_key": "new_value"})
print(storage.get())
```

### `JSONFile.merge(data: dict) -> dict`

Merge new data into the file without losing existing fields.

```python
storage.merge({"another_key": {"nested": "value"}})
print(storage.get())
```

### `JSONFile` magic methods

You can also use `JSONFile` like a dictionary:

```python
storage["name"] = "ControlHub"
print(storage["name"])  # Output: ControlHub

del storage["name"]

print("name" in storage)  # Output: False

for key in storage:
    print(key)
```

## License

This project is licensed under the MIT License.
