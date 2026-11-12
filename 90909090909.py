import colorama
from colorama import Fore, Style

colorama.init()

for item in dir(colorama):
    if not item.startswith('_'):
        if item in ["Fore",]:
            print(f"важливе {item}(змінює колір)")
        if item in ["Back"]:
            print(f"важливе {item}(змінює колір фона)")
        if item in ["Style"]:
            print(f"важливе {item}(змінює стиль)")
        else:
            print(f"{item}")