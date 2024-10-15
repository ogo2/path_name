import psutil
import win32com.client
import os
import time

def is_explorer_process(proc):
    """Проверяем, является ли процесс проводником Windows (explorer.exe)"""
    try:
        if proc.name().lower() == "explorer.exe" and proc.status() == psutil.STATUS_RUNNING:
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    return False

def get_open_directories():
    """Получаем список открытых директорий (окон проводника)"""
    open_dirs = []

    shell = win32com.client.Dispatch("Shell.Application")
    windows = shell.Windows()

    for window in windows:
        if window.Name == "Проводник":
            folder = window.Document.Folder.Self
            open_dirs.append(folder.Path)

    return open_dirs

def save_directories_to_file(open_dirs, file_path):
    """Сохраняем список открытых директорий в текстовый файл"""
    directory = os.path.dirname(file_path)
    # Проверим, существует ли директория, и создадим её, если необходимо
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Список открытых папок (полный путь):\n")
        for directory in open_dirs:
            f.write(f"{directory}\n")

if __name__ == '__main__':
    # Получаем процессы Проводника (explorer.exe)
    explorer_processes = [proc for proc in psutil.process_iter(['name', 'status']) if is_explorer_process(proc)]

    if explorer_processes:
        # Получаем открытые окна Проводника
        open_dirs = get_open_directories()
        # Сохраняем в файл
        save_directories_to_file(open_dirs, r'C:\Users\adm\Desktop\python_program\path_name\open_directories_with_full_path.txt')

        print(f"Список открытых папок сохранён в 'open_directories_with_full_path.txt'")
    else:

        print("Нет активных процессов Проводника.")
        
    # os.system("shutdown /r /t 0")