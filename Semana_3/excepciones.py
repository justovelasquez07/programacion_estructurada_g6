
from colorama import Fore, Style

while True:

    try:
        edad = int(input("Edad: "))
        break

    except ValueError:
        print(Fore.RED + "Ingrese un valor numerico: " + Style.RESET_ALL)

