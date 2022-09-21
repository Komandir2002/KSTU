import os.path, time
from pathlib import Path
import os
filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    file_path = Path.cwd()
    file_stats = os.stat(file_path)
    print(f'Путь: {file_path}\n'
          f'size in bytes is: {file_stats.st_size}\n'
          f'size in Megabytes is : {file_stats.st_size / (1024 * 1024)}')
    print("last modified: %s" % time.ctime(os.path.getmtime(file_path)))
    print("created: %s" % time.ctime(os.path.getctime(file_path)))
else:
    print("Файл не существует")
