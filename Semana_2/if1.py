from colorama import Fore, Style

grade = int(input("Enter your grade: "))

if grade >= 60:
    print(Fore.GREEN + "You get pass")
else:
    print(Fore.RED + "Your learning is at an initial stage.")

print(Style.RESET_ALL)