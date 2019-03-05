def caesar(string, shift):
    #create
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    dictionary1 = {}
    dictionary2 = {}
    dictionary3 = {}
    count = 1
    for x in range(len(alpha)):
        dictionary1[x+1] = alpha[x]
    for y in alpha:
        dictionary2[y] = count
        count += 1
    for y in ALPHA:
        dictionary3[y] = count
        count += 1

    word = list(string)
    new_word = []

    for letter in word:
        if letter in alpha:
            position = dictionary2[letter]
            position += shift
            if position > 26:
                position -= 26
                new_letter = dictionary1[position]
                new_word.append(new_letter)
            else:
                new_letter = dictionary1[position]
                new_word.append(new_letter)
        elif letter in ALPHA:
            position = dictionary3[letter]
            position += shift
            if position > 26:
                position -= 26
                new_letter = dictionary1[position]
                new_word.append(new_letter)
            else:
                new_letter = dictionary1[position]
                new_word.append(new_letter)
        else:
            new_word.append(letter)

    print(''.join(new_word))

caesar("happy am i!", 1)

def decrypt(string, shift):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    dictionary1 = {}
    dictionary2 = {}
    count = 1
    for x in range(len(alpha)):
        dictionary1[x+1] = alpha[x]
    for y in alpha:
        dictionary2[y] = count
        count += 1

    word = list(string)
    new_word = []

    for letter in word:
        if letter in alpha:
            position = dictionary2[letter]
            position -= shift
            if position < 0:
                position += 26
                new_letter = dictionary1[position]
                new_word.append(new_letter)
            else:
                new_letter = dictionary1[position]
                new_word.append(new_letter)
        else:
            new_word.append(letter)
    print(''.join(new_word))

decrypt("ibqqz bn j!", 1)
