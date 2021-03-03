import math
import random

def fact(x):
    if x ==0:
        return 1
    return x*fact(x-1)
flag= True
print("введите действие:\n+ -сложение,\n- -вычитание,\n/ -деление,\n* -умножние,\n^ -возведение в степень,\nmodule -модуль,\nrandom -случайное число,\nfact -факториал,\narccos -arccos,\nquit -выход из программы")
while (flag):
    a = input()

    if a == "+":
        print("введите x=")
        x=float(input())
        print("введите y=")
        y=float(input())
        print(x+y)
    elif a == "-":
        print("введите x=")
        x = float(input())
        print("введите y=")
        y = float(input())
        print(x-y)
    elif a == "*":
        print("введите x=")
        x = float(input())
        print("введите y=")
        y = float(input())
        print(x*y)
    elif a == "/":
        print("введите x=")
        x = float(input())
        print("введите y=")
        y = float(input())
        print(x/y)
    elif a == "^":
        print("введите x=")
        x = float(input())
        print("введите y=")
        y = float(input())
        print(x**y)
    elif a == "module":
        print("введите x=")
        x = float(input())
        print(math.fabs(x))
    elif a == "random":
        print("диапазон случайных чисел от=")
        x = int(input())
        print("до=")
        y = int(input())
        print(random.randint(x,y))
    elif a == "fact":
        print("введите x=")
        x = int(input())
        print(fact(x))
    elif a == "arccos":
        print("введите x=")
        x = float(input())
        print(math.acos(x))
    elif a == "quit":
        flag = False
    else:
        print("Неправильно, попробуй еще раз.")


