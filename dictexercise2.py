products = {
    "Shirt": "Clothes",
    "Jeans": "Clothes",
    "Apple": "Fruits",
    "Banana": "Fruits",
    "Soap": "Toiletries",
    "Towel": "Toiletries"
}
dict1={}
for key,value in products.items():
    if value in dict1:
        dict1[value].append(key)

    else:
        dict1[value]=[key]
print(dict1)
