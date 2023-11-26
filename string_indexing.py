
word = "SuperCoooooooooooooooooooooooolMan!"

print(word[5])

print(word[-10])

print(word[0:5:1])

print(word[:10])

print(word[word.index("Man"):word.index("!")])

# Reverse whole sentence

print(word[::-1])

string = "happy_birthday"
print(string[:string.index("_")])

#### Email Slicer

email = input("Enter your email : ").strip()

# Get username
print(email[:email.index("@")])

# Get domain name
print(email[email.index("@") + 1:])

