word = 'python programming'
print(f'UPPER: {word.upper()}')
print(f'COUNT: {word.count("o")}')
word1 = ' Data Science '
print(word1.strip())

email = 'user@gmail.com'
result = email.split('@')
print(f'User: {result[0]}\nDomain: {result[1]}')

word2 = 'developer'
newWord = word2[::-1]
print(newWord)