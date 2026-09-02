#mostrar los numberos del o al 9
from colorama import Fore, Style
for number in range(10):
    
    if number % 2 == 0:
        print(Fore.GREEN + f"{number}" "es par" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"{number} es impar " + Style.RESET_ALL)