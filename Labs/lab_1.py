import sys
import math

def get_coefficient(name, cli_arg=None):
    if cli_arg is not None:
        try:
            value = float(cli_arg)
            print(f"Коэффициент {name} из командной строки: {value}")
            return value
        except ValueError:
            print(f"Некорректный параметр для {name}. Введите с клавиатуры.")
    
    while True:
        try:
            value = float(input(f"Введите коэффициент {name}: "))
            return value
        except ValueError:
            print(f"Ошибка: введите корректное число для {name}.")

def solve_equation(a, b, c):
    
    print(f"\nРешаем: {a}x^4 + {b}x^2 + {c} = 0")
    
    final_roots = set() 
    
    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение 0 = 0. Бесконечное множество решений.")
            else:
                print(f"Уравнение {c} = 0. Решений нет.")
        else:
            y = -c / b
            if y == 0:
                final_roots.add(0.0)
            elif y > 0:
                root_val = math.sqrt(y)
                final_roots.add(root_val)
                final_roots.add(-root_val)
            else:
                print("Решений нет (x^2 не может быть отрицательным).")
            
    else:
        d = b**2 - 4 * a * c
        print(f"Дискриминант (для y=x^2): D = {d}")

        if d >= 0:
            y1 = (-b + math.sqrt(d)) / (2 * a)
            y2 = (-b - math.sqrt(d)) / (2 * a)
            
            print(f"Промежуточные корни (для y): y1 = {y1}, y2 = {y2}")
            
            positive_y_roots = {y for y in [y1, y2] if y >= 0}

            if not positive_y_roots:
                print("Действительных корней нет (оба y < 0).")
            
            for y in positive_y_roots:
                if y == 0:
                    final_roots.add(0.0)
                else:
                    root_val = math.sqrt(y)
                    final_roots.add(root_val)
                    final_roots.add(-root_val)
        else:
            print("Действительных корней нет (дискриминант < 0).")

    return sorted(list(final_roots)) 

def main():
    args = sys.argv[1:] 
    
    a_arg = args[0] if len(args) > 0 else None
    b_arg = args[1] if len(args) > 1 else None
    c_arg = args[2] if len(args) > 2 else None

    a = get_coefficient("A", a_arg)
    b = get_coefficient("B", b_arg)
    c = get_coefficient("C", c_arg)

    roots = solve_equation(a, b, c)

    if roots:
        print(f"\nНайдены действительные корни (x): {roots}")
        print(f"Всего корней: {len(roots)}")
    elif a != 0 or b != 0 or c != 0:
        print("\nДействительных корней не найдено.")

if __name__ == "__main__":
    main()
