message = "Hello world"

print(message)

#print in lowercase
print(message.lower())

#print in uppercase
print(message.upper())

#count method: this returns number of times given substring occurs in the string
print(message.count('l'))

#find method: this returns index where first match occurs, if not found returns -1
print(message.find("lods"))

#replace method: replaces all matching string to given string, if not found returns the original string
message = 'Hello worldy world'
new_message = message.replace('world', 'Universe')
print(new_message)

#string concatenation
greeting = 'Hello'
name = 'Dev'

#string formatting
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

#f- strings
message = f'{greeting}, {name}. Welcome!'
print(message)

