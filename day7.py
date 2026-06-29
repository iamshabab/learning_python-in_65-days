#Day 7 — Loops (for and while)

print("for loop\n")

fruit=["banana","mango","peach"]

for fruit in fruit:
    print(fruit)
    
print("\n range\n")
a=0

for a in range(5):
    print(a)

print("\n start,end\n")       #the end number will be not included in every case (-1)
for a in range (2,7):
    print(a)

print("\n start,end, pattren\n")
for a in range (10,20,2):
    print(a)

print("\n printing in reverse\n")
for a in range (5,0,-1):
    print(a)

#Looping Through a String
print("\n Looping Through a String \n")

name="shabab alam"

for latter in name:
    print(latter)

#Looping Through a Dictionary
print("\n Looping Through a Dictionary \n ")

dec={"name":"shabab alam","age":22,"city":"dir"}

print("\n print keys from dectionary\n ")

for keys in dec:
    print(keys)

print("\n print values from dectionary \n ")

for values in dec.values():
    print(values)

print("\n total dectionary \n ")

for keys,values in dec.items():
    print(f"{keys},{values}")

#The while Loop
print("\n The while Loop\n")

count=1
while count<=5:
    print(count)
    count+=1

#break
print("\n break\n ")
a=[1,2,3,5,6,8,7,6,8,9,8,]
for stop in a:
    if stop==7:
    
     break
    print(stop)

#continue
print("\n continue \n ")
i=0
for i in range(6):
    if i==3: continue
    print(i)


#else in loop
print("\n else in loop")
x=0
for x in range (8):
    print(x)
else:
    print("finished")

#nusted loop
print("\n nusted loop\n")

a=0
b=0
for a in range(1,4):
    for b in range(1,4):
        print(f"{a}*{b}={a*b}")
    print(">>>>>")

#pattren in loops
print("\n printing avrage and total")

set=[20,44,5,77]
total=0
for sets in set:
    total+=sets
avrage= total / len (set)
print(f"total={total} and \n avrage = {avrage}")

#Building a new list from a loop
print("\n Building a new list from a loop\n")

num=[2,4,3,5]
squ=[]
for n in num:
    squ.append(n**2)
print(squ)

#ml 
print("\n machine learning flavoerd examole")

t_epochs=10
accuracy=0.60
target_accuracy=0.95

for epochs in range(1,t_epochs+1):
    accuracy +=0.04
    print(f"Epoch {epochs}/10 — Accuracy: {accuracy:.2}")
    if accuracy>= target_accuracy:
        print("target accuracy achived")
        break
else:
     print("traning complate but target accouracy not achived")