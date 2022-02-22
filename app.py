import random

input_file = "5_letter_words.txt"

txt_file = open(input_file, "r")
lines = txt_file.read().splitlines()

def starterWord():
    count = 5

    while count > 0:
        rand_num = random.randint(0, len(lines)-1)
        rand_word = lines[rand_num]
        
        new_rand_word = []
        for letter in list(rand_word):
            if letter in new_rand_word:
                continue

        print(rand_word)
        count = count - 1

def searchLetterInPlace(word_list, index, letter):
    new_word_list = []
    for word in word_list:
        if list(word)[index] == letter:
            new_word_list.append(word)
    return new_word_list

def containersLetter(word_list, letter):
    new_word_list = []
    for word in word_list:
        if letter in list(word):
            new_word_list.append(word)
    return new_word_list

def notContainersLetter(word_list, letter):
    new_word_list = []
    for word in word_list:
        if not letter in list(word):
            new_word_list.append(word)
    return new_word_list

new_word_list = lines
new_word_list = searchLetterInPlace(new_word_list, 1, "a")
new_word_list = searchLetterInPlace(new_word_list, 2, "r")
new_word_list = searchLetterInPlace(new_word_list, 3, "k")
new_word_list = searchLetterInPlace(new_word_list, 4, "s")
new_word_list = notContainersLetter(new_word_list, "o")
new_word_list = notContainersLetter(new_word_list, "t")
new_word_list = notContainersLetter(new_word_list, "l")
new_word_list = notContainersLetter(new_word_list, "u")
#new_word_list = containersLetter(new_word_list, "s")


for word in new_word_list:
    print(word)

#starterWord()
