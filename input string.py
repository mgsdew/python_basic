
# Ask user for name

name = input("What's your name ? ")

# Ask user for Age

age = input("How old are you ? ")

print(type(age))

sentence = "Your name is {} and you are {} years old!!"
output = sentence.format(name, age)

print(output)