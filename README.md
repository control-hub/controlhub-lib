# ControlHub python package

**[Read this page in Russian / Читать на русском](README.ru.md)**

ControlHub is a Python automation library for Windows that provides simple APIs to control the desktop, simulate keyboard and mouse actions, and perform web-related tasks.

## Installation

Install the library via pip:

```bash
pip install controlhub
```

## Features

- Open files and run programs
- Simulate mouse clicks, movements, and drags
- Simulate keyboard input and key combinations
- Download files from the web
- Open URLs in the default browser
- Auto delay added to functions to prevent some errors
- Run shell commands
- Use context managers for holding keys
- Manage data in a data.json file (ControlHub service)

## API Reference & Usage Examples

## `controlhub.desktop`

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

### `click(x: int = None, y: int = None, button: str = 'left') -> None`

Simulate a mouse click at the given coordinates or current position.

```python
from controlhub import click

click()  # Click at current position
click(100, 200)  # Click at (100, 200)
click(300, 400, button='right')  # Right-click at (300, 400)
```

### `move(x: int = None, y: int = None) -> None`

Move the mouse to the given coordinates.

```python
from controlhub import move

move(500, 500)
move(0, 0)
move(1920, 1080)
```

### `drag(x: int = None, y: int = None, x1: int = None, y1: int = None, button: str = 'left', duration: float = 0) -> None`

Drag the mouse from start to end coordinates.

```python
from controlhub import drag

drag(100, 100, 200, 200)
drag(300, 300, 400, 400, button='right')
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

press(['ctrl', 'c'])  # Copy
press(['ctrl', 'v'])  # Paste

press(['ctrl', 'c'], ['ctrl', 'v'], "left") # Copy and paste in 1 line and press left arrow
```

### `hold(*keys: Union[str, Key])`

Context manager to hold keys during a block.

```python
from controlhub import hold, press

with hold('ctrl'):
    press('c')  # Ctrl+C

with hold('shift'):
    press('left')  # Select text

with hold(['ctrl', 'alt']):
    press('tab') # Ctrl+Alt+Tab, I
```

### `write(text: str) -> None`

Type the given text.

```python
from controlhub import write

write("Hello, world!")
write("This is automated typing.")
write("ControlHub is awesome!")
```

## `controlhub.web`

### `download(url: str, directory: str = 'download') -> None`

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

## `controlhub.json_storage`

### `JSONFile(file_path: str)`

Create a JSON-backed storage object to store and retrieve data, like a dictionary. All data is saved to a JSON file `file_path`.

```python
from controlhub.json_storage import JSONFile

storage = JSONFile('mydata.json')
storage.set({"key": "value"})
print(storage.get())  # {'key': 'value'}
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

### `data`

Default storage pointing to `data.json`. Mostly used for ControlHub service.

```python
from controlhub import data

data["key"] = "value"
data["another_key"] = {"a": "b", "b": "new_value"}
print(data["key"])  # Output: "value"

data.merge({"another_key": {"b": "updated_value"}})
print(data["another_key"]["b"])  # Output: "updated_value"
```

## License

This project is licensed under the MIT License.
