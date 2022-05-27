# Check if a word is an anagrams


def find_anagrams(word1,word2):
    if(sorted(word1)!= sorted(word2)):
        return False
    else:
        return True
    return False

print("Enter two words to check")
Word1 = input("Enter first word: ")
Word2 = input("Enter second word: ")

print(find_anagrams(Word1, Word2))