#Exercise for day3 

text="machine learning is the future of technology"

#printing lenght

print(len(text))

#print in defferent cases

print(text.upper())
print(text.title())
print(text.capitalize())
print(text.lower())
print(text.strip())
#printing special

print(text[:7])
print(text[-10:])

#replacing

print(text.replace("machine","deep"))
print(text.replace("is","are"))

#split and join

sp=text.split()
print(sp)

joind="_".join(sp)
print(joind)

#finding or checking

print(text.find("future"))
print(text.find("is"))

print("ma" in text)
print("future" in text)
print("tt" in text)


#count 

print(text.count("e"))
print(text.count("t"))

#index

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4]) 

#START & END [true,false]

print(text.startswith("mach"))
print(text.endswith("ogy"))


#multi line string 

details="""my name is shabab alam
im from lower dir tmg
"""
print(details)

name="shabab alam"
age="22"
add="lower dir tmg"
cu_add="naval anchorage, islamabad"
print(f"my name is {name} im {age} years old\n"
f"basically im from {add} and currently living in {cu_add} ")