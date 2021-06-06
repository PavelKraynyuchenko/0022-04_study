#r = 0
def writing_file(name):
    list_1 = []

    file = open(name + ".txt", "r")
    for line in file:
        list_1.append(line)
    file.close
    file = open(name + ".txt", "w")

    for key, val in dict.items():
        file.write('{}:{}\n'.format(key, val))
    file.close
    file = open(name + ".txt", "a")

    for i in range(len(list_1)):
        file.write(list_1[i])
    file.close


mass = []
list_3 = []

print("quit -выход из цикла")

while (True):
    c = input()
    if c == "quit":
        break
    else:
        mass.append(c)

set_2 = set(mass)
print("список -", mass)
print("множество - ", set_2)
print("количество символов в список =", len(mass))
print("заполните следующий список из", len(mass), "символов")

for i in range(len(mass)):
    check = input()
    list_3.append(c)

print(list_3)
s = {list_3[i]: mass[i] for i in range(len(mass))}

print("Введите название файла")
name = input()

dict = s

try:
    writing_file(name)
except IOError as e:
    file = open(name + ".txt", "a")
    writing_file(name)