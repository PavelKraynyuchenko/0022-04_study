def main():
 number1=int(input('введите произвольное число'))
 number2=int(input('введите пограничное число'))
 if number1>number2:
     if number1>number2*3:
         print("произвольное число больше пограничного в 3 раза")
     else:
         print("произвольное число больше пограничного")
 if number1<number2:
     print("произвольное число меньше пограничного")
 if number1==number2:
     print("числа равны")
main()
