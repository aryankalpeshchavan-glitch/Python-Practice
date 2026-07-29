# Q1

n = int(input("Enter number of days: "))

sales = []

for i in range(n):
    sales.append(float(input("Enter sales amount: ")))

total = sum(sales)
average = total / n

print("\n----- Cafe Sales Report -----")
print("Total Sales          :", total)
print("Average Daily Sales  :", average)
print("Highest Sales        :", max(sales))
print("Lowest Sales         :", min(sales))

if average >= 5000:
    print("Status               : Target achieved")
else:
    print("Status               : Target not achieved")

print()


# Q2

name = input("Enter customer name: ")
items = int(input("Enter number of items: "))
bill = float(input("Enter total bill amount: "))

print("\n----- Book Store Bill -----")
print("Data Types")
print(type(name))
print(type(items))
print(type(bill))
print()

if bill >= 2000:
    discount = bill * 0.10
else:
    discount = 0

final = bill - discount

print("Original Bill        :", bill)
print("Discount             :", discount)
print("Final Payable Amount :", final)

print()


# Q3

name = input("Enter student name: ")
mobile = input("Enter mobile number: ")

print("\n----- Student ID -----")

if len(mobile) != 10 or not mobile.isdigit():
    print("Invalid mobile number")
else:
    student_id = name.upper()[:3] + mobile[-4:]
    print("Student ID           :", student_id)

print()


# Q4

cart = input("Enter product names: ").split()

updated = []

for item in cart:
    if item not in updated:
        updated.append(item)

duplicates = len(cart) - len(updated)

print("\n----- Shopping Cart -----")
print("Original Cart        :", cart)
print("Updated Cart         :", updated)
print("Duplicates Removed   :", duplicates)

print()


# Q5

books = input("Enter book status: ").split()

issued = books.count("issued")
available = books.count("available")
total = len(books)

print("\n----- Library Report -----")
print("Total Books          :", total)
print("Issued Books         :", issued)
print("Available Books      :", available)

if issued > total / 2:
    print("Status               : High demand")
else:
    print("Status               : Normal demand")

print()


# Q6

ages = list(map(int, input("Enter ages: ").split()))

print("\n----- Fitness Center -----")
print("Original List        :", ages)

seniors = []

for age in ages:
    if age >= 60:
        seniors.append(age)

print("Senior Members       :", seniors)
print("Total Seniors        :", len(seniors))

if len(seniors) >= 5:
    print("Status               : Offer special discount")
else:
    print("Status               : Regular charges")