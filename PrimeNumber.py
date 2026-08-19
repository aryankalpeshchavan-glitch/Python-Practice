def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

count = 0

print("Prime numbers:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
        count += 1

print("\nCount of primes:", count)