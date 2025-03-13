import psutil
import win32com.client
import os
import time
import logging

# Настройка логирования
logging.basicConfig(
    filename=r'log\script_log.log',  # Путь к лог-файлу
    level=logging.INFO,  # Уровень логирования (INFO)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат записи
)

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

# Переменные для отслеживания времени
last_30min = time.time()
last_2hours = time.time()
last_3hours = time.time()
last_4hours = time.time()
last_5hours = time.time()

# Новые переменные для отслеживания времени
last_10hours = time.time()
last_12hours = time.time()
last_15hours = time.time()
last_17hours = time.time()
last_19hours = time.time()
last_21hours = time.time()
last_24hours = time.time()
last_48hours = time.time()
last_96hours = time.time()
while True:
    try:
        # Получаем процессы Проводника
        explorer_processes = [proc for proc in psutil.process_iter(['name', 'status']) if is_explorer_process(proc)]
        if explorer_processes:
            # Получаем открытые окна Проводника
            open_dirs = get_open_directories()
            
            # Сохраняем пути каждые 30 секунд
            save_directories_to_file(open_dirs, r'interval\interval_30sec\open_directories_with_full_path.txt')
            logging.info("Список открытых папок сохранён в 'interval_30sec'")
            
            # Сохраняем каждые 30 минут
            if time.time() - last_30min >= 30 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_30min\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_30min'")
                last_30min = time.time()
            
            # Сохраняем каждые 2 часа
            if time.time() - last_2hours >= 2 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_2hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_2hours'")
                last_2hours = time.time()
                
            # Сохраняем каждые 3 часа
            if time.time() - last_3hours >= 3 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_3hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_3hours'")
                last_3hours = time.time()
                
            # Сохраняем каждые 4 часа
            if time.time() - last_4hours >= 4 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_4hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_4hours'")
                last_4hours = time.time()
                
            # Сохраняем каждые 5 часов
            if time.time() - last_5hours >= 5 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_5hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_5hours'")
                last_5hours = time.time()
                
            # Сохраняем каждые 10 часов
            if time.time() - last_10hours >= 10 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_10hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_10hours'")
                last_10hours = time.time()
                
            # Сохраняем каждые 12 часов
            if time.time() - last_12hours >= 12 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_12hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_12hours'")
                last_12hours = time.time()
                
            # Сохраняем каждые 15 часов
            if time.time() - last_15hours >= 15 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_15hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_15hours'")
                last_15hours = time.time()
                
            # Сохраняем каждые 17 часов
            if time.time() - last_17hours >= 17 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_17hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_17hours'")
                last_17hours = time.time()
                
            # Сохраняем каждые 19 часов
            if time.time() - last_19hours >= 19 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_19hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_19hours'")
                last_19hours = time.time()
                
            # Сохраняем каждые 21 часов
            if time.time() - last_21hours >= 21 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_21hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_21hours'")
                last_21hours = time.time()
                
            # Сохраняем каждые 24 часа
            if time.time() - last_24hours >= 24 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_24hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_24hours'")
                last_24hours = time.time()
              # Сохраняем каждые 48 часов
            if time.time() - last_48hours >= 48 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_48hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_48hours'")
                last_48hours = time.time()
            # Сохраняем каждые 96 часов
            if time.time() - last_96hours >= 96 * 60 * 60:
                save_directories_to_file(open_dirs, r'interval\interval_96hours\open_directories_with_full_path.txt')
                logging.info("Список открытых папок сохранён в 'interval_96hours'")
                last_96hours = time.time()
        else:
            logging.info("Нет активных процессов Проводника.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}. Перезапуск через 5 секунд...")
    
    # Задержка перед следующим обновлением списка папок (30 секунд)
    time.sleep(30)