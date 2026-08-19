def calculate_result(marks_list):
    total = sum(marks_list)
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade


marks = []

for i in range(3):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

total, percentage, grade = calculate_result(marks)

print("\n----- STUDENT RESULT -----")
print("Total Marks:", total, "/ 300")
print("Percentage:", percentage, "%")
print("Grade:", grade)