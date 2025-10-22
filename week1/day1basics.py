# Program 1: Print welcome message
print('Hello World')


# Program 2: Print welcome message using variables
message = "Hello, World!"

print(message)


# Program 3: Print length of a string
message = "Hello, World!"

print(len(message))


# Program 4: Accessing the first character of the string
message = "Hello, World!"

print(message[0])


# Slicing
# Program 5: Printing just the first word
message = "Hello, World!"

print(message[:5])


# Program 6: Printing just the last word
message = "Hello, World"

print(message[7:])


# Program 7: Convert the string to uppercase
message = "Hello, World!"

print(message.upper())


# Program 8: Convert the string to lowercase
message = "Hello, World!"

print(message.lower())


# string.count() method
# Program 9: How many spaces are there?
sentence = "Python is fun to learn"

print(sentence.count(' '))


# Program 10: Count the number of 'l'
message = "Hello World"

print(message.count('l'))


# Program 11: How many 5's are there?
data = "12345-67890"

print(data.count('5'))


# Program 12: How many times 'na' appear?
text = "banana"
print(text.count('na'))


# string.replace() method
# Program 13: What's the output?
text = "hello world"
result = text.replace('world', 'python')
print(result)
# <-- OUTPUT -->
# hello python


# Program 14: Concatenate strings

greeting = "Hello"
name = "Michael"

message = greeting + ', ' + name + '. Welcome!'

print(message)


# Program 15: Formatted strings

greeting = "Hello"
name = "Michael"

message = '{}, {}. Welcome!'.format(greeting, name)