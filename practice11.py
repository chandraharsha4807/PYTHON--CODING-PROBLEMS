def discountedCart(data):
    
    if data["age"] < 20:
        data["cart"]["Books"] = (int((data["cart"]["Books"] )-((data["cart"]["Books"] )*0.25)))
        data["cart"]["Sports Item"] = (int((data["cart"]["Sports Item"] )-((data["cart"]["Sports Item"] )*0.25)))
        data["cart"]["Electronics"] = (int((data["cart"]["Electronics"] )-((data["cart"]["Electronics"] )*0.1)))
    elif data["age"] > 20 and data["age"] < 40:
        data["cart"]["Home Supplies"] = (int((data["cart"]["Home Supplies"] )-((data["cart"]["Home Supplies"] )*0.25)))
        data["cart"]["Electronics"] = (int((data["cart"]["Electronics"] )-((data["cart"]["Electronics"] )*0.1)))
    else:
        data["cart"]["Electronics"] = (int((data["cart"]["Electronics"] )-((data["cart"]["Electronics"] )*0.1)))
    return data["cart"]




data = {
    "name" : "Clark",
    "age" : 21,
    "cart" : {"Books":300, "Home Supplies":2000, "Sports Item": 100, "Electronics": 2000}
}
keys_list = list(data["cart"].keys())
print(keys_list)
#print(type(data["age"]))
discounted_Cart = discountedCart(data)

print(discounted_Cart)
print(sum(discounted_Cart.values()))