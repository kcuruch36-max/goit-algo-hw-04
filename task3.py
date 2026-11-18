
import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def show_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + indent + "Папка: " + item.name)
            show_directory(item, indent + "    ")
        else:
            print(Fore.GREEN + indent + "Файл: " + item.name)


try:
    path = Path(sys.argv[1])

    if path.is_dir():
        show_directory(path)
    else:
        print("Такої директорії не існує")

except IndexError:
    print("Вкажіть шлях до директорії")

except PermissionError:
    print("Немає доступу до директорії")
