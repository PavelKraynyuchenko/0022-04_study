print("введите 3 названия овоща")
print("первый овощ")
ovosch1 = input()
print("вторый овощ")
ovosch2 = input()
print("третий овощ")
ovosch3 = input()

z1 = ovosch1.lower()
x1 = ovosch2.lower()
c1 = ovosch3.lower()

z2 = ovosch1.upper()
x2 = ovosch2.upper()
c2 = ovosch3.upper()

z3 = ovosch1.capitalize()
x3 = ovosch2.capitalize()
c3 = ovosch3.capitalize()

print(z1,x1,c1)
print(z2,x2,c2)
print(z3,x3,c3)

print("введите количество первого овоща=")
count1 =int(input())
print("введите количество второго овоща=")
count2 =int(input())
print("введите количество третьего овоща=")
count3 =int(input())

print("количество овощей: {0}-{1},{2}-{3},{4}-{5}".format(ovosch1,count1,ovosch2,count2,ovosch3,count3))









