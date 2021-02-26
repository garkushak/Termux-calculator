from colorama import init
from colorama import Fore , Back , Style
init



print(Fore.RED + "────────║║─────────║║─────╔╝╚╗───────")
print(Fore.MAGENTA + "╔══╗╔══╗║║─╔══╗╔╗╔╗║║─╔══╗╚╗╔╝╔══╗╔═╗")
print(Fore.GREEN + "║╔═╝║╔╗║║║─║╔═╝║║║║║║─║╔╗║─║║─║╔╗║║╔╝")
print(Fore.BLUE + "║╚═╗║╔╗║║╚╗║╚═╗║╚╝║║╚╗║╔╗║─║╚╗║╚╝║║║─")
print(Fore.CYAN+ "╚══╝╚╝╚╝╚═╝╚══╝╚══╝╚═╝╚╝╚╝─╚═╝╚══╝╚╝─")


what = input("Выберите комманду + - / * Возвести в степень(**) Поделить по модулю(%)")
a = float(input(Fore.BLACK + "Введите первое число: ") )
b = float(input(Fore.GREEN + "Введдите второе число: ") )
if what == "/,*,**,,%,+":
      c = a + b
      print("Результат" + str(c))
elif what == "-":
 	c = a - b
 	print("Резульат" + str(c))

elif what == "/":
	c = a / b
	print("Результат" + str(c))
elif what == "*":
     c = a * b
     print("Результат" + str(c))
elif what == "**":
     c = a ** b
     print("Результат" + str(c))	
elif what == "%":
	c = a % b
	print("Результат" + str(c))





else:
 	print("Выбрана неверная операция!")
