def has_vowel_than_consonant(s, next_char_index=0, vowel_count=0):
    """
    checks if a string has more vowels than consonants
    :param s: string to check
    :param next_char_index: next character in string
    :param vowel_count: number of vowel
    :return: True if vowel > consonant, False otherwise
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    # base case
    if next_char_index == len(s):
        if vowel_count > len(s) - vowel_count:
            return True
        else:
            return False

    # recursive circle
    # if character is a vowel
    if s[next_char_index].lower() in vowels:
        # recurse with an increment in numbegr of vowels
        return has_vowel_than_consonant(s, next_char_index + 1, vowel_count + 1)
    # if character is a consonant
    else:
        # recurse with number of vowels remain the same
        return has_vowel_than_consonant(s, next_char_index + 1, vowel_count)

if __name__ == "__main__":
    print(has_vowel_than_consonant("Enoma"))
    print(has_vowel_than_consonant("Emmanuel"))