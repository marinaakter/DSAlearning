# List, Slicing, Tuple, Sets, Dictionary

# List
# List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
my_list = ["apple", "banana", "cherry"]
print(my_list)

# Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a Tuple
my_tuple = ("apple", "banana", "cherry")

# Sets
# Set is a collection which is unordered and unindexed. No duplicate members.

# Create a Set
my_set = {"apple", "banana", "cherry"}


# Access Items
print(my_list[1])

# Slice
print(my_list[1:3])

# Change Item Value
my_list[1] = "blackcurrant"

# Loop Through items
for x in my_list:
    print(x)
    
# Check if Item Exists
if "apple" in my_list:
    print("Yes, 'apple' is in the fruits list")
    
# List Length
print(len(my_list))

# Add Items
my_list.append("orange")

# Remove Item
my_list.remove("banana")

# Set Methods
# Add Items
my_set.add("orange")


# Dictionary

# Create a Dictionary

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing Items
print(my_dict["model"])

# Change Values
my_dict["year"] = 2018
