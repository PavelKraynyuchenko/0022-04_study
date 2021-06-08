import math
import random

class calc():
    def fun_fact(a):
        if a == 0:
            return 1
        return a * math.fun_fact(a - 1)

    def fun_sum(self):
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a + b)

    def fun_delen(self):
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a / b)

    def fun_umnoj(self):
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a * b)

    def fun_vychit(self):
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a - b)

    def fun_stepen(self):
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a ** b)

    def fun_module(self):
        print("a =")
        a = float(input())
        print(math.fabs(a))

    def fun_arccos(self):
        print("введите a= от 0 до 1")
        a = float(input())
        print(math.acos(a))

    def fun_random(self):
        print("рандомное число в диапазона от = ")
        a = int(input())
        print("до =")
        b = int(input())
        return print(random.randint(a,b))
