from colorama import init
from colorama import Fore , Back , Style
init



print(Fore.RED + "────────║║─────────║║─────╔╝╚╗───────")
print(Fore.MAGENTA + "╔══╗╔══╗║║─╔══╗╔╗╔╗║║─╔══╗╚╗╔╝╔══╗╔═╗")
print(Fore.GREEN + "║╔═╝║╔╗║║║─║╔═╝║║║║║║─║╔╗║─║║─║╔╗║║╔╝")
print(Fore.BLUE + "║╚═╗║╔╗║║╚╗║╚═╗║╚╝║║╚╗║╔╗║─║╚╗║╚╝║║║─")
print(Fore.CYAN+ "╚══╝╚╝╚╝╚═╝╚══╝╚══╝╚═╝╚╝╚╝─╚═╝╚══╝╚╝─")

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
