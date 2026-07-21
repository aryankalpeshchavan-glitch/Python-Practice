
# 1. Print hello world

print("Hello World")



# 2. Program to add two integers (input from user)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
sum_result = num1 + num2
print("Sum of", num1, "and", num2, "is:", sum_result)



# 3. Square of a number

num = int(input("Enter a number: "))
square = num ** 2
print("Square of", num, "is:", square)



# 4. Swap two numbers

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("Before swapping: a =", a, ", b =", b)

a, b = b, a   # swapping using tuple unpacking

print("After swapping: a =", a, ", b =", b)



# 5. Area of a cricket stadium (circle) with radius 30 meters

radius = 30
area = 3.14159 * radius * radius
print("Area of the cricket stadium is:", area, "sq. meters")



# 6. Take IA1 and IA2 marks and check pass/fail
#    (Assuming max marks = 20 each, total = 40, passing = 40%)

ia1 = float(input("Enter IA1 marks: "))
ia2 = float(input("Enter IA2 marks: "))
total = ia1 + ia2

if total >= 16:   # 40% of 40 = 16
    print("Total marks:", total, "-> Student PASSED the IA exam")
else:
    print("Total marks:", total, "-> Student FAILED the IA exam")



# 7. Find largest of 3 numbers

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("The largest number is:", largest)



# 8. Calculate factorial of a number

n = int(input("Enter a number to find factorial: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is:", factorial)