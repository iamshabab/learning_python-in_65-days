#Dictionaries & Sets
print("dictionaries")

student={
    "name":"shabab",
    "age":22,
    "city":"dir",
    "is_student":True
   
}
print(student["name"]) #first way not recomanded
print(student.get("name")) #2nd way > using value return
print(student.get("is_student"))

#Adding 
print("\n Adding")

student={"name":"shabab alam","age":22,"city":"dir"}
student["email"]="shabab@gmail.com"
print(student)

#Updating
print("\n updating")

student["age"]=23
print(student)


#Removing of key
print("\n removing of key")

del student["email"]
print(student)

#removing and retur of a value
print("\n removing and retur of a value")

age=student.pop("age")
print(age)
print(student)

#usfull method
print("\n usefull method for dectionaries")

person={
    "name":"shabab",
    "age":22,
    "city":"dir"

}
#printing keys
print("\n printing keys ")

print(person.keys())

#printing values
print("\n printing values") 

print(person.values())

 #prenting total items
print("\n prenting total items ")

print(person.items())

 #printing lenght
print("\n printing lenght")

print(len(person))

#checking true false if a key exist
print("\n checking true and false if a key exist or not ")

print("name" in person)
print("city" in person)


#Nested Dictionaries
print("\n Nested Dictionaries")

student={
    "shabab":{"age":22,"score":88},
    "jalil":{"age":23,"score":90},
}

print(student)                              #total nusted dictionaries
print(student["shabab"])                    #inner dictionaries
print(student["jalil"]["score"])            #specfic values

#Dictionary from Two Lists
print("\n Dictionary from Two Lists> combine two lists into a dictionary")

keys=["name","age","city"]
values=["shabab alam",22,"dir"]

print(dict(zip(keys,values)))              #direct method not recommended

person=dict(zip(keys,values))               #2nd method highly recommended
print(person)

#set
print("\n set >unique items ")

fruit={"mango","banana","apple","banana","orange"}      #with repeted data
print(fruit)                                            #didnt print repeated data only print unique

#uses of sets
print("\n uses of sets/ why we use sets")

a={1,2,3,4,5,6}
b={2,3,7,8,7,6}

print(a | b)                        #union unique items 
print(a & b)                        #intersection comman items 
print(a - b)                        #different items present in a but not in b


#adding, removing in a set 
print("\n adding in sets ")

color={"red","green","blue"}

color.add("yallow")
print(color)

print("\n removing from set")

color.remove("green")
print(color)

#convert a list into set 
print("\n convert a list into a set for removing repeated data")

numbers=[1,3,4,5,2,3,1]
numbers=set(numbers)
print(numbers)