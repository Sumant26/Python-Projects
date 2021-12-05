name = 'Sumant'
surname = 'Tulshibagwale'

# CONCATENATION 
# 1st way using +

fullName = name + surname
print(fullName)

fullName = name + ' ' + surname
print(fullName)

# 2nd way PREFERRED WAY
fullName = f'{name} {surname}'
print(fullName)

sentence = 'this is a sentence in lowercase'
sentence.upper()

sentence = 'THIS IS A SENTENCE IN UPPERCASE'
sentence.lower()

sentenceWords = sentence.split(' ')
print(sentenceWords)

sentence = 'I, AM A PYTHON HERO'
sentenceWords = sentence.split(', ')
print(sentenceWords)