
#lists
print("lists ")

fruit=["banana","apple","mango"]
numbers=["22","11","44","50"]
mix=["shabab","22","islamabad"]
print("\n printing lists ")

print(fruit)
print(numbers)
print(mix)


#printing specfic index in a list
print("\n printing specfic indexs in a list ")

print(fruit[0])
print(mix[1:])


#specfic changes in lists 
print("\n specfic changes in list ")

fruit[0]="grapes"
print(fruit)
mix[-1]="rawalpandi"
print(mix)

#adding to the end
print("\n adding something to the end of a list ")

fruit.append("fineapple")
print(fruit)


#adding in specific index
print("\n adding in specfic index ")


fruit.insert(1,"kewi")
print(fruit)

#removeing specfic
print("\n removing specfic from the list ")

fruit.remove("apple")
print(fruit)

#removing by index
print("\n remove something from list by index")

fruit.pop(2)
print(fruit)

#remove from the end of a list
print("\n remove from the end of a lsit")

fruit.pop()
print(fruit)

#lists def methods 
print("\n lists defferent methods")

numbers=[1,3,5,7,9,11,23,1,2,3]

print(numbers.count(1))
print(numbers.index(2))
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.clear()
print(numbers)

#checking sometrhing in the list
print("\n checking something in list")

city=["islamabad","rawalpandi"]

print("rawalpandi" in city)
print("rawat" in city)

#nested lists
print("\n nested lists")

student=[
["shabab",22,24,26], #nested lists inner list end with ,
["jalil",25,26,27],
["kashif",28,"dir",30],
]

print(student[0])
print(student[1][2])
print(student[-1][-2])

#tuple
print("\n tupple (cant be change once created)")

person=("shabab",22,"dir")
fahad=("salam",22,45)
num=(22,44,55)

print(person[0])
print(num[0:-1])
print(fahad[2])

#assining tuple/list item to virable
print("\n assining tuple/list item to virable\n working for both list and tuple")

person=("shabab",22,"islamabad")
person2=["jalil",23,"dir"]

name,age,city=person
name2,age2,city2=person2

print(name)
print(age)
print(city2)
