import os

def open_directories_from_file(file_path):
    """Читает файл и открывает все директории, указанные в нём"""
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        # Пропускаем первую строку с заголовком
        lines = f.readlines()[1:]
        for line in lines:
            folder_path = line.strip()  # Убираем лишние пробелы и символы новой строки
            if os.path.exists(folder_path):
                print(f"Открываем папку: {folder_path}")
                os.startfile(folder_path)  # Открытие папки в Проводнике
            else:
                print(f"Папка не найдена: {folder_path}")

if __name__ == "__main__":
    file_path = r'C:\Users\adm\Desktop\python_program\path_name\open_directories_with_full_path.txt'
    open_directories_from_file(file_path)