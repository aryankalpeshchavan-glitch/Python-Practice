def analyze_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    total_lines = len(lines)
    total_words = 0
    max_word_count = 0
    max_line_text = ""
    max_line_number = 0
    for idx, line in enumerate(lines, start=1):
        words = line.strip().split()
        word_count = len(words)
        total_words += word_count
        if word_count > max_word_count:
            max_word_count = word_count
            max_line_text = line.strip()
            max_line_number = idx
    return total_lines, total_words, max_line_number, max_line_text, max_word_count
total_lines, total_words, max_line_number, max_line_text, max_word_count = analyze_file("notes.txt")
print("Total number of lines :", total_lines)
print("Total number of words :", total_words)
print("Line with maximum words (Line", max_line_number, "):")
print(max_line_text)
print("Word count            :", max_word_count)