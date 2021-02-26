def main():
    s = input('введите строку')
    h=0
    for i in range(0,len(s)):
        if s[i]=='c':
            h=h+1
    print()
    print("символ 'c' встретился ",h,"раз")
    for i in range (0,len(s)-1):
        if i==2:
            continue
        print(s[i],end ='')
main()