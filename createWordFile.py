
input_file = "full_words.txt"
output_file = "5_letter_words.txt"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
clear_letters = []

def checkWord(word):
    for char in list(word):
        if not char in letters:
            return False
    return True

txt_file = open(input_file, "r")
lines = txt_file.read().splitlines()

for word in lines:
    if len(word) == 5 and checkWord(word):
        clear_letters.append(word)

txt_file = open(output_file, "w")
for word in clear_letters:
    txt_file.write(word)
    txt_file.write("\n")
txt_file.close()
