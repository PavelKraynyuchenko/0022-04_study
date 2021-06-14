from math_two import calc

flag = True
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

    if com == "/":
        calc.fun_delen(self=('self'))

    elif com == "quit":
        flag = False

    elif com == "*":
        calc.fun_umnoj(self=('self'))

    elif com == "-":
        calc.fun_vychit(self=('self'))

    elif com == "+":
        calc.fun_sum(self=('self'))

    elif com == "^":
        calc.fun_stepen(self=('self'))

    elif com == "module":
        calc.fun_module(self=('self'))

    elif com == "arccos":
        calc.fun_arccos(self=('self'))

    elif com == "fact":
        print("a =")
        a = float(input())
        print(calc.fun_fact(a))

    elif com == "random":
        calc.fun_random(self=('self'))

    else:
        print("Неправильно, попробуй еще раз.")
