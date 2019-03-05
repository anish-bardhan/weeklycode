def caesar(string, shift):
    #create alphabet arrays
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #create blank hashes
    dictionary1 = {}
    dictionary2 = {}
    dictionary3 = {}
    #set count variable
    count = 1
    #fill hashes
    for x in range(len(alpha)):
        dictionary1[x+1] = alpha[x]
    for y in alpha:
        dictionary2[y] = count
        count += 1
    for y in ALPHA:
        dictionary3[y] = count
        count += 1

    #create array for list
    word = list(string)
    #create new word array
    new_word = []
    #loop through letters in word
    for letter in word:
        #check if letter is in alphabet
        if letter in alpha:
            #make a position using number
            position = dictionary2[letter]
            #add position and shift
            position += shift
            #check if number is too large
            if position > 26:
                #put number in right place
                position -= 26
                #find new letter
                new_letter = dictionary1[position]
                #add letter to word
                new_word.append(new_letter)
            else:
                new_letter = dictionary1[position]
                new_word.append(new_letter)
        #check if letter is upper case
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

    #join word
    print(''.join(new_word))

#call function
caesar("happy am i!", 1)

def decrypt(string, shift):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
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
