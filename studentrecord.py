import json

student = {
    "roll_no": 101,
    "name": "Rahul",
    "department": "EXCS",
    "marks": 85,
    "passed": True
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("student.json created successfully!")

with open("student.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Roll Number:", data["roll_no"])
print("Department:", data["department"])
print("Marks:", data["marks"])

students = [
    {"roll_no": 101, "name": "Rahul", "department": "EXCS", "marks": 85, "passed": True},
    {"roll_no": 102, "name": "Priya", "department": "EXCS", "marks": 92, "passed": True},
    {"roll_no": 103, "name": "Amit", "department": "EXCS", "marks": 67, "passed": True},
    {"roll_no": 104, "name": "Neha", "department": "EXCS", "marks": 45, "passed": False}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    student_data = json.load(file)

print("\nStudent Details:")

for student in student_data:
    print(student["name"], "-", student["marks"])

print("\nStudents scoring 80 or above:")

for student in student_data:
    if student["marks"] >= 80:
        print(student["name"], student["marks"])

topper = max(student_data, key=lambda student: student["marks"])

print("\nTopper:", topper["name"])
print("Marks:", topper["marks"])

total_marks = 0

for student in student_data:
    total_marks += student["marks"]

average = total_marks / len(student_data)

print("Average Marks:", average)