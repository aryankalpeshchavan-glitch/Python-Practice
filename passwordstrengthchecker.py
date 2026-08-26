import string
def has_uppercase(password):
    return any(ch.isupper() for ch in password)
def has_lowercase(password):
    return any(ch.islower() for ch in password)
def has_digit(password):
    return any(ch.isdigit() for ch in password)
def has_special(password):
    return any(ch in string.punctuation for ch in password)
def check_password_strength(password):
    length_ok = len(password) >= 8
    score = sum([
        has_uppercase(password),
        has_lowercase(password),
        has_digit(password),
        has_special(password)
    ])
    if not length_ok or score < 2:
        return "Weak"
    elif score == 4:
        return "Strong"
    else:
        return "Medium"
pwd = input("Enter your password: ")
strength = check_password_strength(pwd)
print("Length           :", len(pwd))
print("Has Uppercase    :", has_uppercase(pwd))
print("Has Lowercase    :", has_lowercase(pwd))
print("Has Digit        :", has_digit(pwd))
print("Has Special Char :", has_special(pwd))
print("Password Strength:", strength)
