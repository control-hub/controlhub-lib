# Пакет ControlHub для Python

**[Читать на английском / Read this page in English](README.md)**

ControlHub — это библиотека для автоматизации Windows на Python, предоставляющая простые API для управления рабочим столом, имитации действий клавиатуры и мыши, а также выполнения веб-задач.

## Установка

Установите библиотеку через pip:

```bash
pip install controlhub
```

## Возможности

-   Открытие файлов и запуск программ
-   Имитация кликов мыши, перемещений и перетаскиваний
-   Имитация ввода с клавиатуры и сочетаний клавиш
-   Загрузка файлов из интернета
-   Открытие URL-адресов в браузере по умолчанию

---

## API и примеры использования

## `controlhub.desktop`

### `open_file(path: str) -> None`

Открывает файл в приложении по умолчанию.

```python
from controlhub import open_file

open_file("C:\\Users\\User\\Documents\\file.txt")
open_file("example.pdf")
open_file("image.png")
```

### `cmd(command: str) -> None`

Выполняет команду оболочки асинхронно.

```python
from controlhub import cmd

cmd("notepad.exe")
cmd("dir")
cmd("echo Hello World")
```

### `run_program(program_name: str) -> None`

Ищет установленную программу по имени и запускает её.

```python
from controlhub import run_program

run_program("notepad")
run_program("chrome")
run_program("word")
```

### `fullscreen(absolute: bool = False) -> None`

Разворачивает текущее окно на весь экран. Если `absolute=True` — переключает режим полноэкранного (F11).

```python
from controlhub import fullscreen

fullscreen()
fullscreen(absolute=True)
fullscreen(absolute=False)
```

### `search_program(program_name: str) -> str`

Ищет путь к исполняемому файлу программы по имени.

```python
from controlhub import search_program

path = search_program("notepad")
print(path)

path = search_program("chrome")
print(path)

path = search_program("word")
print(path)
```

---

## `controlhub.keyboard`

### `click(x: int = None, y: int = None, button: str = 'left') -> None`

Имитация щелчка мышью по заданным координатам или в текущей позиции.

```python
from controlhub import click

click()  # Щелкнуть в текущей позиции
click(100, 200)  # Щелкнуть по координатам (100, 200)
click(300, 400, button='right')  # Правый щелчок по координатам (300, 400)
```

### `move(x: int = None, y: int = None) -> None`

Перемещает курсор мыши в указанные координаты.

```python
from controlhub import move

move(500, 500)
move(0, 0)
move(1920, 1080)
```

### `drag(x: int = None, y: int = None, x1: int = None, y1: int = None, button: str = 'left', duration: float = 0) -> None`

Перетаскивает мышь из одной точки в другую.

```python
from controlhub import drag

drag(100, 100, 200, 200)
drag(300, 300, 400, 400, button='right')
drag(500, 500, 600, 600, duration=1.5)
```

### `get_position() -> tuple[int, int]`

Возвращает текущие координаты курсора мыши.

```python
from controlhub import get_position

pos = get_position()
print(pos)

x, y = get_position()
print(f"Положение мыши: ({x}, {y})")
```

### `press(*keys: Union[str, Key]) -> None`

Имитирует нажатие и отпускание одной или нескольких клавиш.

```python
from controlhub import press

press('ctrl', 'c')  # Копировать
press('ctrl', 'v')  # Вставить
press('alt', 'tab')  # Переключение между окнами
```

### `hold(*keys: Union[str, Key])`

Контекстный менеджер: удерживает клавиши во время выполнения блока кода.

```python
from controlhub import hold, press

with hold('ctrl'):
    press('c')  # Удерживаем Ctrl и нажимаем C (Копировать)

with hold('shift'):
    press('left')  # Выделение текста

with hold('alt'):
    press('tab')  # Переключение между окнами
```

### `write(text: str) -> None`

Вводит указанный текст.

```python
from controlhub import write

write("Привет, мир!")
write("Это автоматический ввод текста.")
write("ControlHub — крутая штука!")
```

---

## `controlhub.web`

### `download(url: str, directory: str = 'download') -> None`

Скачивает файл по URL в указанную папку.

```python
from controlhub import download

download("https://example.com/file.zip")
download("https://example.com/image.png", directory="images")
download("https://example.com/doc.pdf", directory="docs")
```

### `open_url(url: str) -> None`

Открывает веб-страницу в браузере по умолчанию.

```python
from controlhub import open_url

open_url("https://www.google.com")
open_url("github.com")  # Автоматически добавит http://
open_url("https://stackoverflow.com")
```

---

## Лицензия

Этот проект распространяется под лицензией MIT.
