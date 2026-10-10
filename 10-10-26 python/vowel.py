greet = "My name is Krunal"
vowel = 0
space = 0
consonent = 0
for i in greet:
    if i in "aeiou":
        vowel+=1
    elif i.isalpha():
        consonent+=1
    elif i ==" ":
        space+=1
print(vowel)
print(consonent)
print(space)