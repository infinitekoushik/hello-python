# Dictionary example in Python

student = {
    "name": " Chandra Koushik",
    "age": 16,
    "course": "CS Diploma"
}

print("Student name:", student["name"])
print("Student age:", student["age"])

# Adding new key
student["grade"] = "A"
print("Updated student info:", student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
