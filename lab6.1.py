import math
import random
def fun_sum(a,b):
    print("введите a=")
    a = float(input())
    print("введите b=")
    b = float(input())
    return print(a+b)
def fun_vychit(a,b):
    print("введите a=")
    a = float(input())
    print("введите b=")
    b = float(input())
    return print(a-b)
def fun_umnoj(a,b):
    print("введите a=")
    a = float(input())
    print("введите b=")
    b = float(input())
    return print(a*b)
def fun_delen(a,b):
    print("введите a=")
    a = float(input())
    print("введите b=")
    b = float(input())
    return print(a/b)
def fun_stepen(a,b):
    print("введите a=")
    a = float(input())
    print("введите b=")
    b = float(input())
    return print(a**b)
def fun_module(a):
    print("введите a=")
    a = float(input())
    return print(math.fabs(a))
def fun_random(a,b):
    print("диапазон случайных чисел от=")
    a = int(input())
    print("до=")
    b = int(input())
    return print(random.randint(a,b))
def fun_fact(a):
    if a ==0:
        return 1
    return a*fun_fact(a-1)
def fun_arccos(a):
    print("введите a= от 0 до 1")
    a = float(input())
    return print(math.acos(a))
flag=True
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
    a = 0; b = 0; com = 0;
    com = input()
    if com == "+":
        fun_sum(a,b)
    elif com == "-":
        fun_vychit(a,b)
    elif com == "*":
        fun_umnoj(a,b)
    elif com == "/":
        fun_delen(a,b)
    elif com == "^":
        fun_stepen(a,b)
    elif com == "module":
        fun_module(a)
    elif com == "random":
        fun_random(a,b)
    elif com == "fact":
        print("введите a=")
        a = int(input())
        print(fun_fact(a))
    elif com == "arccos":
        fun_arccos(a)
    elif com == "quit":
        flag=False
    else:
        print("Неправильная команда, попробуй еще раз.")

