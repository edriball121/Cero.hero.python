saludo = "Hello World"

print(saludo)
print("Hola mundo")
print(saludo, "!!!")

# Print with different separators
print("Hello", "World", sep=", ")
print("Hello", "World", sep="---")

# Print with different end characters
print("Hello", end=" ")
print("World", end="!!!\n")

# Print formatted strings
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")

# Print multiple lines
print("""This is a
multi-line
string""")

# Print with escape characters
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello \"World\"")

# Print to a file
with open("output.txt", "w") as file:
    print("Hello World", file=file)