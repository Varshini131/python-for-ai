student = {
    "name": "Varshini",
    "age": 20,
    "cgpa": 8.0
}

print(student)

print(student["name"])

student["city"] = "Visakhapatnam"

print(student)

for key, value in student.items():
    print(key, ":", value)