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
print("введите действие:\n+ -сложение,\n- -вычитание,\n/ -деление,\n* -умножние,\n^ -возведение в степень,\nmodule -модуль,\nrandom -случайное число,\nfact -факториал,\narccos -arccos,\nquit -выход из программы")
while (flag):
    a = 0; b = 0; p = 0;
    p = input()
    if p == "+":
        fun_sum(a,b)
    elif p == "-":
        fun_vychit(a,b)
    elif p == "*":
        fun_umnoj(a,b)
    elif p == "/":
        fun_delen(a,b)
    elif p == "^":
        fun_stepen(a,b)
    elif p == "module":
        fun_module(a)
    elif p == "random":
        fun_random(a,b)
    elif p == "fact":
        print("введите a=")
        a = int(input())
        print(fun_fact(a))
    elif p == "arccos":
        fun_arccos(a)
    elif p == "quit":
        flag=False
    else:
        print("Неправильная команда, попробуй еще раз.")

