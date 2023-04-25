
''' функция делает строчку ЗАГЛАВНЫМИ буквами'''

def to_upper_case(s):
    return s.upper()

s = input()
to_upper_case(s)


''' функция делает заглавными первые буквы'''

def capitalize_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    return ' '.join(new_words)

capitalize_words('hello world')