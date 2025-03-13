import os
import flet as ft

def get_file_path(interval):
    """Определяет путь к файлу на основе выбранного интервала"""
    interval_map = {
        "30 секунд": 30,
        "30 минут": 1800,
        "2 часа": 7200,
        "3 часа": 10800,
        "4 часа": 14400,
        "5 часов": 18000,
        "10 часов": 36000,
        "12 часов": 43200,
        "15 часов": 54000,
        "17 часов": 61200,
        "19 часов": 68400,
        "21 часов": 75600,
        "24 часа": 86400,
        "48 часов": 172800,
        "96 часов": 345600
    }
    seconds = interval_map.get(interval)
    if seconds == 30:
        return r'interval\interval_30sec\open_directories_with_full_path.txt'
    elif seconds == 1800:
        return r'interval\interval_30min\open_directories_with_full_path.txt'
    elif seconds == 7200:
        return r'interval\interval_2hours\open_directories_with_full_path.txt'
    elif seconds == 10800:
        return r'interval\interval_3hours\open_directories_with_full_path.txt'
    elif seconds == 14400:
        return r'interval\interval_4hours\open_directories_with_full_path.txt'
    elif seconds == 18000:
        return r'interval\interval_5hours\open_directories_with_full_path.txt'
    elif seconds == 36000:
        return r'interval\interval_10hours\open_directories_with_full_path.txt'
    elif seconds == 43200:
        return r'interval\interval_12hours\open_directories_with_full_path.txt'
    elif seconds == 54000:
        return r'interval\interval_15hours\open_directories_with_full_path.txt'
    elif seconds == 61200:
        return r'interval\interval_17hours\open_directories_with_full_path.txt'
    elif seconds == 68400:
        return r'interval\interval_19hours\open_directories_with_full_path.txt'
    elif seconds == 75600:
        return r'interval\interval_21hours\open_directories_with_full_path.txt'
    elif seconds == 86400:
        return r'interval\interval_24hours\open_directories_with_full_path.txt'
    elif seconds == 172800:
        return r'interval\interval_48hours\open_directories_with_full_path.txt'
    elif seconds == 345600:
        return r'interval\interval_96hours\open_directories_with_full_path.txt'
    else:
        return None

def open_directories_from_file(file_path):
    """Читает файл и открывает все директории, указанные в нем"""
    if not os.path.exists(file_path):
        return f"Файл {file_path} не найден."

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
        for line in lines:
            folder_path = line.strip()
            if os.path.exists(folder_path) or folder_path.startswith("::"):
                print(f"Открываем папку: {folder_path}")
                os.startfile(folder_path)
            else:
                print(f"Папка не найдена: {folder_path}")
    return "Папки успешно открыты."

def display_saved_directories(page, selected_interval, list_view):
    """Отображает список сохраненных папок в ListView"""
    file_path = get_file_path(selected_interval)
    if not file_path or not os.path.exists(file_path):
        list_view.controls = [ft.Text(f"Файл для интервала {selected_interval} не найден.")]
        page.update()
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
            content = [line.strip() for line in content]

        if not content:
            content = ["Список папок пуст."]

        list_view.controls = [ft.Text(line) for line in content]
        page.update()

    except Exception as e:
        list_view.controls = [ft.Text(f"Произошла ошибка: {e}")]
        page.update()

def start_opening(page, interval):
    """Запускает процесс открытия папок через выбранный интервал"""
    file_path = get_file_path(interval)
    if not file_path:
        page.snack_bar = ft.SnackBar(ft.Text("Не удалось найти файл для данного интервала."))
        page.snack_bar.open = True
        page.update()
        return

    result = open_directories_from_file(file_path)
    page.snack_bar = ft.SnackBar(ft.Text(result))
    page.snack_bar.open = True
    page.update()

def main(page: ft.Page):
    page.title = "Автоматическое открытие папок"
    page.window_width = 400
    page.window_height = 500  # Увеличил высоту для списка папок
    page.window_resizable = False

    intervals = [
        "30 секунд", "30 минут", "2 часа", "3 часа", "4 часа", "5 часов",
        "10 часов", "12 часов", "15 часов", "17 часов", "19 часов",
        "21 часов", "24 часа", "48 часов", "96 часов"
    ]
    
    dropdown = ft.Dropdown(
        label="Выберите интервал открытия папок",
        options=[ft.dropdown.Option(i) for i in intervals],
        value=intervals[0]
    )

    list_view = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)

    def on_submit(e):
        selected_interval = dropdown.value
        if selected_interval:
            start_opening(page, selected_interval)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Выберите временной интервал."))
            page.snack_bar.open = True
            page.update()

    def on_display(e):
        selected_interval = dropdown.value
        if selected_interval:
            display_saved_directories(page, selected_interval, list_view)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Выберите временной интервал."))
            page.snack_bar.open = True
            page.update()

    def stop_program(e):
        page.window_close()

    page.add(
        dropdown,
        ft.ElevatedButton("Просмотреть сохраненные папки", on_click=on_display),
        ft.Row([
            ft.ElevatedButton("Запустить", on_click=on_submit),
            ft.ElevatedButton("Остановить", on_click=stop_program)
        ], alignment="center"),
        list_view  # Добавляем ListView для отображения списка папок
    )

if __name__ == "__main__":
    ft.app(target=main)