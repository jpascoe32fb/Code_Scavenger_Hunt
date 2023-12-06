#Clue 1
array = [1, 2, 3, 4, 5]
for element in array:
    print(element)

#Clue 2
print("Hello World"

#Clue 3 
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#Clue 4
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

#Clue 5
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing a value using a key
print(my_dict["name"]) # Output: Alice

#Clue 6
try:
    # Attempt to execute code that may cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific error
    print("Cannot divide by zero.")

#Clue 7
for i in range(10):
    if i == 5:
        break
    print(i)

#Clue 8
for i in range(3): # Outer loop
    for j in range(3): # Inner loop
        print(f"({i}, {j})", end=" ")
    print() # Newline for each iteration of the outer loop

#Clue 9
try:
    # Code that may raise an exception
    file = open("example.txt", "r")
    data = file.read()
except IOError:
    # Handle the IO error
    print("Error reading file.")
finally:
    # This block will always be executed
    file.close()
    print("File closed.")

#Clue 10
my_list = [("apple", "a fruit"), ("carrot", "a vegetable")]

# Accessing an element by its index and getting its name and value
name, description = my_list[0]
print(f"{name}: {description}")