#day 4 exercise

# Part 1 — Lists
# 1. Create a list of 5 of your favorite foods

food=["baryani","mathan karahi","chiken white handi","pizza","shawarma","alo parata"]

# 2. Print the first and last item

print(food[0]) #first 
print(food[-1]) #last

# 3. Add a new food at the end

food.append("anda parat")
print(food)


# 4. Replace the second item with something else
food.pop(1)
food.insert(1,"sabzi")
print(food)

# 5. Remove the third item

food.remove("chiken white handi")
print(food)

# 6. Print the final list, its length, and sort it

print(len(food))
food.sort()
print(food)


# Part 2 — Nested List

# 7. Create a nested list of 3 students with [name, age, score]

student=[
["shabab",22,90],
["jalil",23,95],
["abdul",25,96],
]

# 8. Print the second student's name and score

print(student[1][0])
print(student[1][2])


# Part 3 — Tuples
# 9. Create a tuple of your city, country, and timezone

details=("islamabad",'pakistan',"(GMT+5)")

# 10. Unpack it into 3 variables and print each one

city,country,timezone=details
print(f"{city},{country},{timezone}")
