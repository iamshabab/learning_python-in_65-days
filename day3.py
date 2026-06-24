name="shabab alam"
city="islamabad"
massage="im learning python"

#finding lenght

print(len(name))
print(len(city))
print(len(massage))



#indexing

print(name[0])
print(name[-1])
print(name[3])
print(name[-11])
print(name[10])

#slicing [start:end] the end indix not included

text="love playing cricket"

print(text[0:4])
print(text[5:12])
print(text[13:])
print(text[:5])
print(text[-7:])
print(text[:])
print(text[-15:-8])
print(text[:-8])



#different cases (uppere,lower)

massage="hello , my name is shabab alam"

print(massage.upper())
print(massage.title()) #each starting character
print(massage.capitalize()) #starting character of the sentence only
print(massage.lower())
print(massage.strip())
print(massage.replace("shabab alam","jalil"))

print(massage.startswith("hello"))
print(massage.endswith("alam"))
print(massage.endswith("jalil"))
print(massage.find("is"))
print(massage.find("alam"))
print(massage.find("hello"))
print(massage.startswith("h"))

#spliting and joining

word=massage.split()
print(word)
print(massage.split())
massage="shabab,22,islamabad"
word=massage.split(",")
print(word)

text="my name is khan"
text=text.split()
print(text)
joind="-".join(text)
print(joind)

#checking what inside string is

text="iamshabab@gmail.com"

print("my" in text)
print("shabab" in text)
print("@" in text)
print(text.count("m"))
print(text.count("my"))
print(text.count("a"))


age=22
print(f"my name is {name} im {age} years old")

#multi line string

sent="""my name is shabab alam
iam from lower dir tmg 
currently living in islamabad"""

print(sent)

