# 1. Ask the user to store a temperature value in a variable
#    (just assign it directly, e.g. temperature = 38)
#    Then print:
#    - "Freezing"  if below 0
#    - "Cold"      if 0 to 15
#    - "Warm"      if 16 to 30
#    - "Hot"       if above 30


temprature=3

if temprature < 0:
    print("freezing")
elif temprature >=0 and temprature <= 15:
    print("cold")
elif temprature > 15 and temprature <= 30:
    print("warm")
else:
    print("hot")


# 2. Create variables: username and password
#    Check if username == "admin" AND password == "1234"
#    Print "Login successful" or "Access denied"

username="admin"
password=1234

if username == "admin" and password == 1234:
    print("login successful")
else:
    print("access denied")
    


# 3. Create a variable: day = "Saturday"
#    Check if it is a weekday or weekend and print accordingly
#    Weekdays: Monday to Friday
#    Weekend: Saturday, Sunday

day="saturday"
if day in {"monday","tuesday","wednsday","thursday","friday"}:
    print(f"{day} is on weekday")
elif day in {"saturday","sunday"}:
    print(f"{day} is a weekend")


# 4. Store a number and check:
#    - If it is positive, negative, or zero
#    - If it is even or odd
#    (hint: use % to check even/odd)

number=12
if number > 0:
    print("positive number")
elif number == 0:
    print("zero")
elif number < 0:
    print("negative number")
if number % 2== 0:
    print("even number")
    if number % 2 !=0:
        print("odd number")

# 5. ML Challenge:
#    Create variables: accuracy = 0.87, loss = 0.12, epoch = 30
#    Write conditions to print one of:
#    - "Deploy model"         if accuracy > 0.95
#    - "Keep training"        if accuracy > 0.80 and loss < 0.20
#    - "Reduce learning rate" if loss >= 0.20
#    - "Something is wrong"   otherwise

accuracy=0.87
loss=0.12
epoch=30

if accuracy > 0.95:
    print("deploy model")
elif accuracy > 0.80 and loss < 0.20:
    print("keep traning")
elif loss >= 0.20:
    print("reduce learning rate")
else:
    print("something is wrong")