'''27. Word frequency (dictionary counting)
Read a sentence, normalize it to lowercase, split it into words, and count each word in a dictionary. Print each word
and count. Punctuation handling is an optional extension.'''

sentence = input("Enter a sentence: ")

sentence = sentence.lower()
words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(word, ":", count)