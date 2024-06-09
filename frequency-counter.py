# Given two strings, write a function to determine if the second string is an anagram of the first. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(string1, string2):
  
    """checks if one string is the angram of a second

    >>> isAnagram("mark", "kram")
    True
    >>> isAnagram("hello", "bello")
    False
    >>> isAnagram("Listen", "Silent")
    True
    >>> isAnagram("Astronomer", "Moon starer")
    True
    """
    
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    if(len(string1) != len(string2)):
        return False

    string1_dictionary = {}
    for letter in string1:
        string1_dictionary[letter] = string1_dictionary.get(letter, 0) + 1
    
    string2_dictionary = {}
    for letter in string2:
        string2_dictionary[letter] = string2_dictionary.get(letter, 0) + 1
    
    return string1_dictionary == string2_dictionary

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)