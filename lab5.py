list1 = []
key2 = []
print("вводите слова")
print("quit -выход из цикла")
while(True):
    x = input()
    if x == "quit":
        break
    else:
        list1.append(x)
plenty3 = set(list1)
print("список -",list1)
print("множество - ",plenty3)
print("количество символов в списке =",len(list1))
print("заполните следующий список из",len(list1),"слов")
for i in range(len(list1)):
    x = input()
    key2.append(x)
print(key2)
dict = {list1[i]:key2[i] for i in range(len(list1))}
print(dict)
