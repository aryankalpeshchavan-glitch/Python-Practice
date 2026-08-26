def count_character_types(sentence):
    vowels = consonants = digits = spaces = special = 0
    vowel_chars = "aeiouAEIOU"
    for ch in sentence:
        if ch.isalpha():
            if ch in vowel_chars:
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
    return vowels, consonants, digits, spaces, special
user_input = input("Enter a sentence: ")
v, c, d, s, sp = count_character_types(user_input)
print("Vowels            :", v)
print("Consonants        :", c)
print("Digits            :", d)
print("Spaces            :", s)
print("Special Characters:", sp)