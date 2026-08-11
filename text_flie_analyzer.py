
FILENAME = "data.txt"
VOWELS = set("aeiouAEIOU")


def read_file():
    with open(FILENAME, "r") as f:
        return f.read()


def read_lines():
    with open(FILENAME, "r") as f:
        return f.readlines()


def count_characters():
    content = read_file()
    print("Total characters:", len(content))


def count_lines():
    lines = read_lines()
    print("Total lines:", len(lines))


def count_words():
    content = read_file()
    words = content.split()
    print("Total words:", len(words))


def classify_chars(text):
    alphabets = digits = spaces = special = 0
    for ch in text:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
    return alphabets, digits, spaces, special


def count_char_types_file():
    content = read_file()
    a, d, s, sp = classify_chars(content)
    print(f"Alphabets: {a}\nDigits: {d}\nSpaces: {s}\nSpecial characters: {sp}")


def count_char_types_lines():
    lines = read_lines()
    for i, line in enumerate(lines, start=1):
        a, d, s, sp = classify_chars(line)
        print(f"Line {i}: Alphabets={a}, Digits={d}, Spaces={s}, Special={sp}")


def classify_vowels(text):
    vowels = consonants = 0
    for ch in text:
        if ch.isalpha():
            if ch in VOWELS:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


def count_vowels_consonants_file():
    content = read_file()
    v, c = classify_vowels(content)
    print(f"Vowels: {v}\nConsonants: {c}")


def count_vowels_consonants_lines():
    lines = read_lines()
    for i, line in enumerate(lines, start=1):
        v, c = classify_vowels(line)
        print(f"Line {i}: Vowels={v}, Consonants={c}")


def count_words_with_vowels():
    content = read_file()
    words = content.split()
    count = sum(1 for word in words if any(ch in VOWELS for ch in word))
    print("Words containing at least one vowel:", count)


def show_menu():
    print("""
========== TEXT FILE ANALYZER ==========
1. Count characters in the file
2. Count lines in the file
3. Count words in the file
4. Count alphabets, digits, spaces & special chars (whole file)
5. Count alphabets, digits, spaces & special chars (each line)
6. Count vowels & consonants (whole file)
7. Count vowels & consonants (each line)
8. Count words containing vowels
9. Run ALL of the above
0. Exit
=========================================
""")


def run_all():
    count_characters()
    print()
    count_lines()
    print()
    count_words()
    print()
    count_char_types_file()
    print()
    count_char_types_lines()
    print()
    count_vowels_consonants_file()
    print()
    count_vowels_consonants_lines()
    print()
    count_words_with_vowels()


def main():
    actions = {
        "1": count_characters,
        "2": count_lines,
        "3": count_words,
        "4": count_char_types_file,
        "5": count_char_types_lines,
        "6": count_vowels_consonants_file,
        "7": count_vowels_consonants_lines,
        "8": count_words_with_vowels,
        "9": run_all,
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting... Goodbye!")
            break

        action = actions.get(choice)
        if action:
            try:
                print()
                action()
            except FileNotFoundError:
                print(f"Error: '{FILENAME}' not found. Place it in the same folder as this script.")
        else:
            print("Invalid choice, try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()