
"1. Count characters in a text file"
with open("data.txt", "r") as f:
    content = f.read()

print("Total characters:", len(content))

"2. Count lines in a text file"

with open("data.txt", "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))

"3. Count words in a text file"
with open("data.txt", "r") as f:
    content = f.read()

words = content.split()
print("Total words:", len(words))

"4. Count alphabets, digits, spaces, and special characters in a text file"
with open("data.txt", "r") as f:
    content = f.read()

alphabets = digits = spaces = special = 0

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


"5. Count alphabets, digits, spaces, and special characters in each line of a text file"
with open("data.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    alphabets = digits = spaces = special = 0
    for ch in line:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
    print(f"Line {i}: Alphabets={alphabets}, Digits={digits}, Spaces={spaces}, Special={special}")

"6. Count vowels and consonants in a text file"
with open("data.txt", "r") as f:
    content = f.read()

vowels = consonants = 0
vowel_set = set("aeiouAEIOU")

for ch in content:
    if ch.isalpha():
        if ch in vowel_set:
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

"7. Count vowels and consonants in each line of a text file"
with open("data.txt", "r") as f:
    lines = f.readlines()

vowel_set = set("aeiouAEIOU")

for i, line in enumerate(lines, start=1):
    vowels = consonants = 0
    for ch in line:
        if ch.isalpha():
            if ch in vowel_set:
                vowels += 1
            else:
                consonants += 1
    print(f"Line {i}: Vowels={vowels}, Consonants={consonants}")

"8. Find the longest line in a text file"
with open("data.txt", "r") as f:
    content = f.read()

words = content.split()
vowel_set = set("aeiouAEIOU")

count = 0
for word in words:
    if any(ch in vowel_set for ch in word):
        count += 1

print("Words containing at least one vowel:", count)