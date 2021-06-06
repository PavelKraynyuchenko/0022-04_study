from math_two import m

run = True
print(
        "введите действие:\n+ -сложение,\n- -вычитание,\n/ -деление,\n* -умножние,\n^ -возведение в степень,\nmodule -модуль,\nrandom -случайное число,\nfact -факториал,\narccos -arccos,\nquit -выход из программы")

while (run):
    str = input()

    if str == "/":
        m.fun_delen(self=('self'))

    elif str == "quit":
        run = False

    elif str == "*":
        m.fun_umnoj(self=('self'))

    elif str == "-":
        m.fun_vychit(self=('self'))

    elif str == "+":
        m.fun_sum(self=('self'))

    elif str == "^":
        m.fun_stepen(self=('self'))

    elif str == "m":
        m.fun_module(self=('self'))

    elif str == "arccos":
        m.fun_arccos(self=('self'))

    elif str == "!":
        print("a =")
        a = float(input())
        print(m.fun_fact(a))

    elif str == "rand":
        m.fun_random(self=('self'))

    else:
        print("Неправильно, попробуй еще раз.")