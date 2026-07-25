# Arithmetic Operators

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print()


# Comparison Operators

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print()

# Logical Operators

x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

print()

# Assignment Operators

num = 10

num += 5
print("+= :", num)

num -= 2
print("-= :", num)

num *= 3
print("*= :", num)

num /= 2
print("/= :", num)

print()

# Membership Operators

course = "Python for AI"

print("Python" in course)
print("Java" in course)

print()

# Identity Operators

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)