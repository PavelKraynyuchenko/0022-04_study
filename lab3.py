import math
import random

def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)
flag= True
print("введите действие:"
      "\n + -сложение,"
      "\n - -вычитание,"
      "\n / -деление,"
      "\n * -умножние,"
      "\n ^ -возведение в степень,"
      "\n module -модуль,"
      "\n random -случайное число,"
      "\n fact -факториал,"
      "\n arccos -arccos,"
      "\n quit -выход из программы")
while (flag):
    com = input()

    if com == "+":
        print("введите a=")
        a=float(input())
        print("введите b=")
        b=float(input())
        print(a+b)
    elif com == "-":
        print("введите a=")
        a = float(input())
        print("введите b=")
        b = float(input())
        print(a-b)
    elif com == "*":
        print("введите a=")
        a = float(input())
        print("введите b=")
        b = float(input())
        print(a*b)
    elif com == "/":
        print("введите a=")
        a = float(input())
        print("введите b=")
        b = float(input())
        print(a/b)
    elif com == "^":
        print("введите a=")
        a = float(input())
        print("введите b=")
        b = float(input())
        print(a**b)
    elif com == "module":
        print("введите a=")
        a = float(input())
        print(math.fabs(a))
    elif com == "random":
        print("диапазон случайных чисел от=")
        a = int(input())
        print("до=")
        b = int(input())
        print(random.randint(a,b))
    elif com == "fact":
        print("введите a=")
        a = int(input())
        print(fact(a))
    elif com == "arccos":
        print("введите a=")
        a = float(input())
        print(math.acos(a))
    elif com == "quit":
        flag = False
    else:
        print("Неправильно, попробуй еще раз.")




