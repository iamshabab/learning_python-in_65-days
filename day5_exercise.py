# Part 1 — Dictionaries

# 1. Create a dictionary for a laptop with keys:
#    brand, model, price, ram, is_available

laptop={

"brand":"lenove",
"model":"lp2015",
"price":60000,
"ram":"8gb",
"is_avilable":True,

}

print(laptop)

# 2. Print the brand and price using both [] and .get()

print(laptop["brand"])
print(laptop["price"])

print(laptop.get("brand"))          #get()
print(laptop.get("price"))          #get()

# 3. Add a new key "storage" with a value

laptop["storage"]="256gb"
print(laptop)

# 4. Update the price

laptop["price"]=70000
print(laptop)

# 5. Remove "is_available"

del laptop["is_avilable"]
print(laptop)

# 6. Print all keys, all values, and the total number of keys

print(laptop.keys())
print(laptop.values())
print(len(laptop.keys()))

# Part 2 — Nested Dictionary
# 7. Create a dictionary of 2 products, each with name, price, and stock
proudect={
"proudect_1":{"name":"phone","price":"rs 30000","stock":"45 piece"},
"proudect_2":{"name":"laptop","price":"rs 100000","stock":"5 piece"}
}
print(proudect)

# 8. Print the price of the second product
print(proudect["proudect_2"]["price"])

# Part 3 — Sets
# 9. Create two sets: one for Python topics you know, one for topics you want to learn
topic_iknow={"output function","variable","strings","list","tuple"}
topic_dnow={"conditional functions","loops","mathamitical equation","configurtaion"}

# 10. Print the union, intersection, and difference of the two sets

print(topic_iknow | topic_dnow)
print(topic_iknow & topic_dnow)
print(topic_iknow - topic_dnow)
# 11. Create a list with duplicates and use a set to remove them


color=["green","blue","red","green","blue","yellow","brown","green"]
color=set(color)
print(color)

