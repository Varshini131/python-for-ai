# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Welcome to Python for AI!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()

print(content)