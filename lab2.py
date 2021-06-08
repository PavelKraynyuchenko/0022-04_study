def main():
    str = input('введите строку')
    count=0 # count-счетчик
    for i in range(0,len(str)):
        if str[i]=='c':
            count=count+1
    print()
    print("символ 'c' встретился ",count,"раз")
    for i in range (0,len(str)-1):
        if i==2:
            continue
        print(str[i],end ='')
main()
