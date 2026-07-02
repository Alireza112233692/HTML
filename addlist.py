fruits = ["sib", "moz", "porteghal"]

fruits.append("hendoone")
# ba method append mitonim akhar listemon ye item ezafe konim 
print(fruits)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
# baraye chasboondan da]o ta list beham dige az method extend estefade mikonim
print(list1)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
# ba ravesh (list + list) ham mishe chasboondeshon beham dige
print(result)
# mesall :

names = []

esm1 = input("esm aval: ")
names.append(esm1)

esm2 = input("esm dovom: ")
names.append(esm2)

esm3 = input("esm sevom: ")
names.append(esm3)

esm4 = input("esm chaharom: ")
names.append(esm4)

print(names[2])  


# hala baraye hazf kardan meghdar daron listemoon 4 rah vojod darad  :

fruits = ["sib", "moz", "porteghal"]

fruits.remove("sib")

print(fruits) 

fruits = ["sib", "moz", "porteghal"]

fruits.pop(2)

print(fruits)

# nokte ahe pop() khali bashe dakhelesh index akhar ro back mikone 

fruits = ["sib", "moz", "porteghal"]

del fruits[1]

print(fruits)