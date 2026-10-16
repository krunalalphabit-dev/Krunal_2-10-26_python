'''07. Message inspector
Read a sentence and a search word. Report its length, first and last character (if present), whether the search word
occurs, and the first five and last five characters using slicing. Handle an empty sentence.
Extension: Count how many times the search word occurs, ignoring case.'''


sentence = input("Enter a sentence: ")
word = input("Enter a search word: ")

print("Length:", len(sentence))

if sentence:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])
    print("First five characters:", sentence[:5])
    print("Last five characters:", sentence[-5:])
else:
    print("Sentence is empty")

print("Word occurs:", word.lower() in sentence.lower())
print("Word count:", sentence.lower().count(word.lower()))