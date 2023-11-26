text = "Happy Coding!"

# Count a specific character
print(text.count("p"))
# Convert to lower
print(text.lower())
# Convert to upper
print(text.upper())

# Condition check

print(text.islower())
print(text.isupper())
print(text.istitle())
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())

# Index checking

print(text.index("Coding"))

# Striping

text1 = "000000000000HappyYou00000000000"

print(text1.strip("0"))
print(text1.rstrip("0"))
print(text1.lstrip("0"))

name = input("What's your name?" )
print(len(name))

name2 = input("What's your name?" ).strip()
print(len(name2))