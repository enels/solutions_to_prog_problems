def minion_game(string):
    # your code goes here
    
    # set the consonants
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    
    # set the vowels
    vowels = 'AEIOU'
    
    # get length of string
    str_len = len(string)    
    
    cons_set = set()
    vow_set = set()
    
    words = dict()

    for i in range(str_len):
        
        #if the character is a consonant
        if string[i] in consonants:
            
            # get the first character
            cons_set.add(string[i])
            
            # put is vowel to be false
            is_vowel = False
            
        else:
            # get the first character
            vow_set.add(string[i])
            
            # indication that character is a vowel
            is_vowel = True
            
        new_word = string[i]

        if new_word in words:
            # exists
            words[new_word] += 1
        else:
            # does not exists
            words[new_word] = 1

        # iterate through the rest of the characters
        # concatenating it with the previous character
        for j in range(i+1, str_len):
                
            # concatenate the current character with the other
            # suceeding characters
            new_word += string[j]

            # check if word exists in dictionary
            if new_word in words:
                # exists
                words[new_word] += 1
            else:
                # does not exists
                words[new_word] = 1

            if is_vowel:
                # add to vowel set
                vow_set.add(new_word)
            else:
                # add to the consonant set
                cons_set.add(new_word)
    
     # finally get the length of both and return with the length and the player's name
     
    # get the length of the vowel and consonant
    vowel_length = len(vow_set)
    conso_length = len(cons_set)

    # iterate through the words to check which word is greater than 1 and check if it's a vowel or consonant
    for k,v in words.items():
        if k in vow_set and v > 1:
            vowel_length += v - 1
        elif k in cons_set and v > 1:
            conso_length += v - 1

    if vowel_length > conso_length:
        print("Kevin " + str(vowel_length))
    else:
        print("Stuart " + str(conso_length))
    
     
            
                

if __name__ == '__main__':
    s = input()
    minion_game(s)
