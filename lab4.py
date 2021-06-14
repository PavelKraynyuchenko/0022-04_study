print("введите 3 названия овоща")
print("первый овощ")
ovosch1 = input()
print("вторый овощ")
ovosch2 = input()
print("третий овощ")
ovosch3 = input()

output1 = ovosch1.lower()
output2 = ovosch2.lower()
output3 = ovosch3.lower()

output4 = ovosch1.upper()
output5 = ovosch2.upper()
output6 = ovosch3.upper()

output7 = ovosch1.capitalize()
output8 = ovosch2.capitalize()
output9 = ovosch3.capitalize()

print(output1,output2,output3)
print(output4,output5,output6)
print(output7,output8,output9)

print("введите количество первого овоща=")
count1 =int(input())
print("введите количество второго овоща=")
count2 =int(input())
print("введите количество третьего овоща=")
count3 =int(input())

print("количество овощей: {0}-{1},{2}-{3},{4}-{5}".format(ovosch1,count1,ovosch2,count2,ovosch3,count3))









