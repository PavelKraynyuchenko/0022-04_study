list_1 = []
list_3 = []

def mass_key():
    str = []
    while (True):
        c = input()
        if c == "quit":
            break
        else:
            str.append(c)
    return str

def mass_values(str):
    str_3 = []
    for i in range(len(str)):
        c = input()
        str_3.append(c)
    return str_3

#completion-завершение
def completion_list(str_3, str):
    s = {str[i]: str_3[i] for i in range(len(str))}
    return s

print("quit -выход из цикла")
list_1 = mass_key()

list_2 = set(list_1)
print("список -", list_1)
print("множество - ", list_2)
print("количество символов в списке =", len(list_1))
print("заполните следующий список из", len(list_1), "символов")

list_3 = mass_values(list_1)

print(list_3)
list = completion_list(list_3, list_1)
print(list)
