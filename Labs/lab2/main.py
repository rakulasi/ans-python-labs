from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Style, init

def main():
    init(autoreset=True)
    
    N = 18 
    
    print("Создаем объекты с N = {}".format(N))
    
    rect = Rectangle(N, N, "синего")
    circ = Circle(N, "зеленого")
    sq = Square(N, "красного")
    
    print(rect)
    print(circ)
    print(sq)
    
    print("\n" + Fore.YELLOW + "Тест внешнего пакета 'colorama'")
    print(Fore.CYAN + "Этот текст должен быть бирюзовым")
    print(Fore.RED + "Этот текст должен быть красным")
    print(Style.RESET_ALL + "А этот - обычным")

if __name__ == "__main__":
    main()
