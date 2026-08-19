def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def nPr(n, r):
    return factorial(n) // factorial(n - r)


n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r > n or n < 0 or r < 0:
    print("Invalid values of n and r")
else:
    print("nCr =", nCr(n, r))
    print("nPr =", nPr(n, r))