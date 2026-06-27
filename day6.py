#Day 6 — Conditionals (if, elif, else)

print("conditionals \n if, elif, else")
#if
print("if condition")

a=18
if a >= 18:
    print("you are an adult")

#elif
print("\n if else condition")

a=15
if a>=18:
    print("you are an adult")

else:
    print("you are a minor")

#elif else
print("\n if, elif and else") 

score=99

if score>=90:
    print("A+ grade")

elif score>=80:
    print("A- grade")

elif score>=70:
    print("B grade")

elif score>=60:
    print("C grade")

else:
    print("you are fail")

#Comparison Operators
print("\n Comparison Operators")

x=20
y=30

print(y == x)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x > 10)
print(10 >= 100)

#and OR Not
print("logical operator and, or, not")

#and

high=120
low=49

if high <= 130 and low >= 50:                   #both condition to be true
    print("in controled")

else:
    print("your both condition are not true")

#or

if high <= 130 or low >= 50:
    print("you are okay")

else:
    print("only one condition is to be true")

#not
print("\n not condition change true to false and false to true")

banned=False

if not banned:
    print("wellcome")


#checking
print("\n cheacking ")

fruit="apple"

if fruit in ("apple","mango","banana"):
    print(f"{fruit} is avilable")
else:
    print(f"{fruit} is not avialable")

#Nested Conditionals
print("\n Nested Conditionals       if inside another if")
age=20
has_id=False
if age >= 18:
    if has_id:
        print("you are allowed")
    else:
        print("dont have id")
else:
    print("you are minor")

#one line condition
print("\n one line if condition")

a=20
status="adult" if a >= 18 else "minor"
print(status)

#machine learning base example
print("\n ml base example")

accuracy=0.90
loss=0.1
epochs_trained = 60

if accuracy >= 0.95:
    print("model is ready")

elif accuracy >= 0.90 and loss < 0.2:
    print("your model is good but need more traning")

elif epochs_trained >= 100:
    print("stoped _max epochs trained ")
else:
    print("model need more traning ")