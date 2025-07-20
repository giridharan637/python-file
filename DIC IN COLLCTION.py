# 📚 Dictionary Example - All in One

# Create a dictionary
student = {
    "name": "Giri",
    "age": 16,
    "city": "Chennai"
}

print("Original Dictionary:", student)

# Access values
print("\nAccess Values:")
print("Name:", student["name"])
print("Age:", student.get("age"))

# Add new key-value
student["school"] = "ABC School"
print("\nAfter Adding 'school':", student)

# Update existing value
student["age"] = 17
print("After Updating 'age':", student)

# Remove a key-value
student.pop("city")
print("\nAfter Removing 'city':", student)

# Another way to remove
del student["school"]
print("After Removing 'school':", student)

# Add multiple using update()
student.update({"city": "Coimbatore", "grade": "12th"})
print("\nAfter update():", student)

# Loop through keys & values
print("\nLoop Through Dictionary:")
for key, value in student.items():
    print(key, ":", value)

# Show only keys
print("\nAll Keys:", list(student.keys()))

# Show only values
print("All Values:", list(student.values()))
