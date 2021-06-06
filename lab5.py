str = []
str2 = []
print("вводите слова")
print("quit -выход из цикла")
while(True):
    x = input()
    if x == "quit":
        break
    else:
        str.append(x)
str3 = set(str)
print("список -",str)
print("множество - ",str3)
print("количество символов в списке =",len(str))
print("заполните следующий список из",len(str),"слов")
for i in range(len(str)):
    x = input()
    str2.append(x)
print(str2)
dir = {str[i]:str2[i] for i in range(len(str))}
print(dir)