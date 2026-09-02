def search_and_replace(source_file, target_file, search_word, replace_word):
    with open(source_file, "r") as infile:
        content = infile.read()
    count = content.count(search_word)
    updated_content = content.replace(search_word, replace_word)
    with open(target_file, "w") as outfile:
        outfile.write(updated_content)
    return count
search = input("Enter the word to search  : ")
replace = input("Enter the word to replace : ")
replacements = search_and_replace("notes.txt", "notes_updated.txt", search, replace)
print("Number of replacements made :", replacements) 
print("Updated content written to  : notes_updated.txt")