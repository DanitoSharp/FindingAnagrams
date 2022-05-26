# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #First layer of validation - Comparing lengths
    if len(word) != len(anagram):
        return False

    # Created two dictionaries to store separately each letter
    # as a key and count of the letter as value.
    dic = {}
    for l in word:
        dic[l.lower()] = word.count(l)

    dic_s = {}
    for l_s in anagram:
        dic_s[l_s.lower()] = anagram.count(l_s)

    # second layer of validation - Compareing the values from both dictionaries
    # to know if they don't match.
    for seen in word:
        if dic.get(seen) != dic_s.get(seen):
            return False

    return True

#Done
print(find_anagram("mooN", "mono"))

