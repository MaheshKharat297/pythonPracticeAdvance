from collections import defaultdict


def group_anagrams(words):
    anagrams = defaultdict(list)  # Dictionary to store grouped anagrams
    for word in words:
        # Sort the word and use it as the key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())


# Example usage
words = ["eat", "ate", "bat", "tab", "tea"]
print(group_anagrams(words))

#lst = ["eat","ate","bat","tab","tea"]
#output:[['eat', 'ate', 'tea'], ['bat', 'tab']]


