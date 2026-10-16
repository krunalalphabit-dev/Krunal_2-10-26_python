'''05. Name card
Read a full name. Print it in uppercase, lowercase, title case, and with leading/trailing spaces removed. Show the
character count before and after trimming.
Extension: Print the first and last character when the cleaned name is non-empty.'''


name = input("Enter your full name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Before trimming:", len(name))

clean_name = name.strip()

print("After trimming:", clean_name)
print("Character count after trimming:", len(clean_name))

if clean_name:
    print("First character:", clean_name[0])
    print("Last character:", clean_name[-1])