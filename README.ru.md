# Пакет ControlHub для Python

**[Read this page in English / Читать на английском](README.md)**

ControlHub — это библиотека автоматизации на Python для Windows, которая предоставляет простые API для управления рабочим столом, имитации действий клавиатуры и мыши, а также выполнения задач, связанных с интернетом.

## Установка

Установите библиотеку через pip:

```bash
pip install controlhub
```

## Возможности

-   Открытие файлов и запуск программ
-   Имитация кликов мыши, перемещений и перетаскиваний
-   Имитация ввода текста с клавиатуры и нажатия сочетаний клавиш
-   Скачивание файлов из интернета
-   Открытие ссылок в браузере по умолчанию
-   Автоматическая задержка для предотвращения ошибок
-   Выполнение shell-команд
-   Управление удержанием клавиш через контекстные менеджеры
-   Работа с данными в файле `data.json` (сервис ControlHub)
-   Изменение базовой задержки путём изменения переменной окружения `CH_DELAY`
-   Взаимодействуйте с данными controlhub прямо из скрипта

> [!NOTE]
> Базовая задержка по умолчанию составляет 0.2 секунды, но её можно изменить, задав переменную окружения `CH_DELAY`. У core скриптов по умолчанию `CH_DELAY` 0.8 секунд.

## API и примеры использования

## `controlhub.desktop`

Модуль для взаимодействия с windows пк через функции.

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

Развернуть текущее окно. При `absolute=True` включить полноэкранный режим (F11).

```python
from controlhub import fullscreen

fullscreen()
fullscreen(absolute=True)
fullscreen(absolute=False)
```

### `switch_to_next_window`

Переключение на следующее окно (только Windows): Alt + Tab

### `switch_to_last_window`

Переключение на предыдущее окно (только Windows): Alt + Shift + Tab

### `reload_window`

Переключиться на следующее окно дважды, чтобы вернуть фокус текущему окну.

## `controlhub.keyboard`

Модуль для взаимодействия с клавиатурой и мышкой через функции.

### `click(x: int = None, y: int = None, button: str = "left") -> None`

Имитация клика мышью по указанным координатам или текущей позиции курсора.

```python
from controlhub import click

click()
click(100, 200)
click(300, 400, button="right")
```

### `move(x: int = None, y: int = None) -> None`

Переместить мышь в указанные координаты.

```python
from controlhub import move

move(500, 500)
move(0, 0)
move(1920, 1080)
```

### `drag(x: int = None, y: int = None, x1: int = None, y1: int = None, button: str = "left", duration: float = 0) -> None`

Перетащить мышь из одной точки в другую.

```python
from controlhub import drag

drag(100, 100, 200, 200)
drag(300, 300, 400, 400, button="right")
drag(500, 500, 600, 600, duration=1.5)
```

### `get_position() -> tuple[int, int]`

Получить текущую позицию мыши.

```python
from controlhub import get_position

x, y = get_position()
print(f"Мышь находится в ({x}, {y})")
```

### `press(*keys: Union[AnyKey, Iterable[AnyKey]]) -> None`

Имитация нажатий клавиш.

```python
from controlhub import press

press(["ctrl", "c"])
press(["ctrl", "v"])
press(["ctrl", "c"], ["ctrl", "v"], "left")
```

### `hold(*keys: Union[str, Key])`

Контекстный менеджер для удержания клавиш.

```python
from controlhub import hold, press

with hold("ctrl"):
    press("c")

with hold("shift"):
    press("left")

with hold(["ctrl", "alt"]):
    press("tab")

with hold("ctrl", "shift"):
    press("esc")
```

### `write(text: str) -> None`

Печать текста с помощью клавиатуры. Также поддерживает \n.

```python
from controlhub import write

write("Привет, мир!")
write("Это автоматический ввод.")
write("ControlHub – топ!")
write("from controlhub import write\nwrite(\"Hello, world\")")
```

## `controlhub.web`

Модуль для взаимодействия с интернетом через функции.

### `download(url: str, directory: str = "download") -> None`

Скачать файл по ссылке в указанную папку.

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
open_url("github.com")
open_url("https://stackoverflow.com")
```

## `controlhub.pocketbase`

Модуль для взаимодействия с записями о компьютерах и выполнениях в pocketbase через функции.

> [!ВАЖНО]
> Функции из этого модуля могут выполняться только в скриптах controlhub.

### `get_execution() -> ExecutionResponse`

Возвращает выполнение из базы данных.

```python
from controlhub import get_execution

print(get_execution())
```

### `update_execution(data: ExecutionRecord) -> ExecutionResponse`

Обновляет выполнение в базе данных и возвращает его.

```python
from controlhub import update_execution

new_execution = {
    "status": "3",
    "duration": 20
}

print(update_execution(new_execution))
```

### `get_computer() -> ComputerResponse`

Возвращает компьютер из базы данных.

```python
from controlhub import get_computer

print(get_computer())
```

### `get_offline_computer() -> ComputerResponse`

Возвращает компьютер из локальной переменной окружения `COMPUTER_JSON`.

```python
from controlhub import get_offline_computer

print(get_offline_computer())
```

### `update_computer(data: ExecutionRecord) -> ExecutionResponse`

Обновляет компьютер в базе данных и возвращает его.

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

Создать объект для хранения данных в JSON-файле.

```python
from controlhub.json_storage import JSONFile

storage = JSONFile("mydata.json")
storage.set({"key": "value"})
print(storage.get())
```

### `JSONFile.get() -> dict`

Получить все данные из файла.

```python
print(storage.get())
```

### `JSONFile.set(data: dict) -> None`

Полностью заменить содержимое файла.

```python
storage.set({"new_key": "new_value"})
print(storage.get())
```

### `JSONFile.merge(data: dict) -> dict`

Объединить новые данные с существующими без перезаписи всего файла.

```python
storage.merge({"another_key": {"nested": "value"}})
print(storage.get())
```

### `JSONFile` как словарь

Можно работать с `JSONFile` как с обычным словарём:

```python
storage["name"] = "ControlHub"
print(storage["name"])

del storage["name"]

print("name" in storage)

for key in storage:
    print(key)
```

### `data`

Стандартный экземпляр `JSONFile`, указывающий на файл `data.json`, используется в скриптах ControlHub.

```python
from controlhub import data

data["key"] = "value"
data["another_key"] = {"a": "b", "b": "new_value"}
print(data["key"])

data.merge({"another_key": {"b": "updated_value"}})
print(data["another_key"]["b"])
```

## Лицензия

Проект распространяется под лицензией MIT.
