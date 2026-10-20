'''P3. Palindrome phrase (strings and slicing)
Read a word or phrase, normalize it to lowercase, remove spaces, and determine whether it reads the same forward
and backward. Print the normalized text and result.'''

text = input("Enter a word or phrase: ")

text = text.lower()
text = text.replace(" ", "")

print("Normalized text:", text)

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")