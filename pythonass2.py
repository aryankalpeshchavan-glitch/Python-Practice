def get_int_list(prompt):
    """Helper: take comma-separated numbers from user and return as a list of ints."""
    raw = input(prompt)
    return [int(x.strip()) for x in raw.split(",") if x.strip() != ""]
# these are for all set of number codes





# 1. FizzBuzz from 1 to N
print("=" * 50)
print("1. FizzBuzz")
print("=" * 50)
 
n = int(input("Enter the upper limit (FizzBuzz will run from 1 to N): "))
 
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
 
# 2. Virat Kohli - Highest Score
print("\n" + "=" * 50)
print("2. Virat Kohli - Highest Score")
print("=" * 50)
 
score1 = int(input("Enter score 1 (183 vs Pakistan, ODI, 2012): "))
score2 = int(input("Enter score 2 (254 vs South Africa, Test, 2019): "))
score3 = int(input("Enter score 3 (107 vs Sri Lanka, ODI, 2009): "))
 
highest_score = max(score1, score2, score3)
print(f"Highest run scored by Virat Kohli: {highest_score}")
 
# 3. Check if a Number is Odd or Even
print("\n" + "=" * 50)
print("3. Odd or Even Checker")
print("=" * 50)
 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
 
# 4. Check Leap Year
print("\n" + "=" * 50)
print("4. Leap Year Checker")
print("=" * 50)
 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
 
# 5. Check whether numbers are in Ascending Order
print("\n" + "=" * 50)
print("5. Ascending Order Check")
print("=" * 50)
 
number = get_int_list("Enter numbers separated by commas (e.g. 1,3,7,4,9): ")
 
if number == sorted(number):
    print(f"{number} is in Ascending Order")
else:
    print(f"{number} is NOT in Ascending Order")
 
# 6. Find Even Numbers from a List
print("\n" + "=" * 50)
print("6. Even Numbers from List")
print("=" * 50)
 
number = get_int_list("Enter numbers separated by commas (e.g. 1,3,2,8,7): ")
even_numbers = [n for n in number if n % 2 == 0]
print(f"List: {number}")
print(f"Even Numbers: {even_numbers}")
 
# 7. Find Odd Numbers from a List
print("\n" + "=" * 50)
print("7. Odd Numbers from List")
print("=" * 50)
 
number = get_int_list("Enter numbers separated by commas (e.g. 1,3,2,8,7): ")
odd_numbers = [n for n in number if n % 2 != 0]
print(f"List: {number}")
print(f"Odd Numbers: {odd_numbers}")
 
# 8. Make a Single Unique List from Two Lists
print("\n" + "=" * 50)
print("8. Unique List from Two Lists")
print("=" * 50)
 
num1 = get_int_list("Enter first list of numbers separated by commas: ")
num2 = get_int_list("Enter second list of numbers separated by commas: ")
 
unique_list = sorted(set(num1 + num2))
 
print(f"List 1: {num1}")
print(f"List 2: {num2}")
print(f"Unique Combined List: {unique_list}")