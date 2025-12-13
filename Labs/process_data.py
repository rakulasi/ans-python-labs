import json
import sys
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1


path = sys.argv[1]    # путь к json-файлу передаётся параметром командной строки

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    # список профессий без повторов, сортировка без учёта регистра
    names = field(arg, 'name')
    return sorted(Unique((n.strip() for n in names if n), ignore_case=True),
                  key=str.lower)


@print_result
def f2(arg):
    # оставить только те, что начинаются со слова "программист"
    return list(filter(lambda s: s.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    # добавить " с опытом Python"
    return list(map(lambda s: f'{s} с опытом Python', arg))


@print_result
def f4(arg):
    # добавить случайную зарплату от 100000 до 200000
    salaries = gen_random(len(arg), 100000, 200000)
    return [f'{name}, зарплата {sal} руб.' for name, sal in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
