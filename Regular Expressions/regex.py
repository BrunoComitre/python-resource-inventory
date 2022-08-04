import re
from re import MULTILINE, findall, match, search

print(re.match('abc', 'abc'))

print(re.match('abc', 'efabcd'))

print(re.search('abc', 'efabcd'))

print(re.findall('abc', '123ef156abc789d0abc'))


# Meta character


print(match('.', 'abc'))

print(match('.', '123'))

print(match('.', '   '))

print(match('.', '\t\t'))

print(match('.', '\n'))

print(search('.', 'abc'))

print(search('.', '\nabc'))

print(findall('.', 'abc'))


# Anchors ^ $


print(findall('^.', 'abc\nedf\nghi'))

# re.MULTILINE means that starts to the end of line
print(findall('^.', 'abc\nedf\nghi'), re.MULTILINE)

print(findall('.$', 'abc\nedf\nghi'))

print(findall('.$', 'abc\nedf\nghi'), re.MULTILINE)

# Means that ^ and $ match the beginning and end of each line, respectively.
print(match('^.$', 'abc'))

print(match('^.$', ''))

print(findall('^.$', 'abc\nedf\nghi'), re.MULTILINE)


# Class of Characters

# Con
print(findall('[aeiou]', 'John Wick Doctor Strange'))

# Negative Class of Characters
print(findall('[^aeiou]', 'John Wick Doctor Strange'))

# Range of Characters
print(findall('[a-f]', 'John Wick Doctor Strange'))

# Range of Characters with Capital Letters
print(findall('[a-fA-Z]', 'John Wick Doctor Strange'))

# Range of Characters with Capital Letters
print(findall('[a-zA-Z]', 'John Wick Doctor Strange'))

# Range of Characters with Capital Letters and Numbers
print(findall('[a-zA-Z0-9_]', 'John Wick Doctor Strange'))

# Range with all Characters
print(findall('[\w]', 'John Wick Doctor Strange'))

# Special Sequences

'''
\d - Digit [0-9]

\D - Not a Digit [^0-9]

\s - Whitespace [\t\n\r\f\v]

\S - Not Whitespace [^\t\n\r\f\v]

\w - Word Character [a-zA-Z0-9_]

\W - Not a Word Character [^a-zA-Z0-9_]
'''
