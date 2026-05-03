# Create dictionary
my_dict = {"name": "Snehal", "age": 20}

# Access elements
print("Name:", my_dict["name"])

# Update dictionary
my_dict["age"] = 21
my_dict["city"] = "Pune"
print("Updated dictionary:", my_dict)

# Remove elements
my_dict.pop("city")
print("After pop:", my_dict)

del my_dict["age"]
print("After delete:", my_dict)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print("Merged dictionary:", merged)