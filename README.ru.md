# Пакет ControlHub для Python

**[Read this page in English / Читать на английском](README.md)**

ControlHub – это библиотека автоматизации на Python для Windows, которая позволяет легко управлять рабочим столом, имитировать действия клавиатуры и мыши, а также выполнять задачи, связанные с интернетом.

## Установка

Установите библиотеку через pip:

```bash
pip install controlhub
```

## Возможности

-   Открывать файлы и запускать программы
-   Имитировать клики, движения и перетаскивание мыши
-   Имитировать ввод текста с клавиатуры и нажатие сочетаний клавиш
-   Скачивать файлы из интернета
-   Открывать ссылки в браузере по умолчанию
-   Автоматическая задержка после функций, чтобы избежать ошибок

---

## API и примеры использования

## `controlhub.desktop`

### `open_file(path: str) -> None`

Открыть файл в приложении по умолчанию.

```python
from controlhub import open_file

open_file("C:\\Users\\User\\Documents\\file.txt")
open_file("example.pdf")
open_file("image.png")
```

### `cmd(command: str) -> None`

Выполнить команду в командной строке асинхронно.

```python
from controlhub import cmd

cmd("notepad.exe")
cmd("dir")
cmd("echo Hello World")
```

### `run_program(program_name: str) -> None`

Найти программу по названию и запустить её.

```python
from controlhub import run_program

run_program("notepad")
run_program("chrome")
run_program("word")
```

### `fullscreen(absolute: bool = False) -> None`

Развернуть текущее окно. Если `absolute=True`, включается полноэкранный режим (F11).

```python
from controlhub import fullscreen

fullscreen()
fullscreen(absolute=True)
fullscreen(absolute=False)
```

### `switch_to_next_window`

Переключиться на следующее окно (только Windows): Alt + Tab

### `switch_to_last_window`

Переключиться на предыдущее окно (только Windows): Alt + Shift + Tab

### `reload_window`

Переключается на следующее окно дважды, возвращая фокус текущему окну.

---

## `controlhub.keyboard`

### `click(x: int = None, y: int = None, button: str = 'left') -> None`

Имитация клика мышью по указанным координатам или текущему положению курсора.

```python
from controlhub import click

click()  # Клик в текущей позиции
click(100, 200)  # Клик по координатам (100, 200)
click(300, 400, button='right')  # Правый клик (300, 400)
```

### `move(x: int = None, y: int = None) -> None`

Переместить мышь в указанные координаты.

```python
from controlhub import move

move(500, 500)
move(0, 0)
move(1920, 1080)
```

### `drag(x: int = None, y: int = None, x1: int = None, y1: int = None, button: str = 'left', duration: float = 0) -> None`

Перетащить мышь из одной точки в другую.

```python
from controlhub import drag

drag(100, 100, 200, 200)
drag(300, 300, 400, 400, button='right')
drag(500, 500, 600, 600, duration=1.5)
```

### `get_position() -> tuple[int, int]`

Получить текущую позицию курсора мыши.

```python
from controlhub import get_position

pos = get_position()
print(pos)

x, y = get_position()
print(f"Мышь находится в ({x}, {y})")
```

### `press(*keys: Union[AnyKey, Iterable[AnyKey]]) -> None`

Имитация нажатий и отпускания клавиш.

```python
from controlhub import press

press(['ctrl', 'c'])  # Копировать
press(['ctrl', 'v'])  # Вставить

press(['ctrl', 'c'], ['ctrl', 'v'], "left") # Скопировать, вставить и нажать стрелку влево
```

### `hold(*keys: Union[str, Key])`

Контекстный менеджер, удерживающий клавиши во время выполнения блока.

```python
from controlhub import hold, press

with hold('ctrl'):
    press('c')  # Копировать

with hold('shift'):
    press('left')  # Выделить текст

with hold(['ctrl', 'alt']):
    press('tab') # Ctrl+Alt+Tab
    pass # И дальше любой выполненный код будет выполнен с зажатыми ctrl, alt
```

### `write(text: str) -> None`

Ввод заданного текста с клавиатуры.

```python
from controlhub import write

write("Привет, мир!")
write("Это автоматический ввод текста.")
write("ControlHub – это круто!")
```

---

## `controlhub.web`

### `download(url: str, directory: str = 'download') -> None`

Скачать файл по ссылке в указанную директорию.

```python
from controlhub import download

download("https://example.com/file.zip")
download("https://example.com/image.png", directory="images")
download("https://example.com/doc.pdf", directory="docs")
```

### `open_url(url: str) -> None`

Открыть ссылку в браузере по умолчанию.

```python
from controlhub import open_url

open_url("https://www.google.com")
open_url("github.com")  # автоматически добавится http://
open_url("https://stackoverflow.com")
```

---

## Лицензия

Проект распространяется под лицензией MIT.