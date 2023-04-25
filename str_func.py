def capitalize_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    return ' '.join(new_words)

capitalize_words('hello world')