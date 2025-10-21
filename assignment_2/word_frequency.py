import re

def word_freq():
    freqs = {}

    text = ''
    try:
        with open('my_text.txt') as f:
            text = f.read()
    except FileNotFoundError as error:
        print(error)
    
    words = [word for word in re.split(r'\W+', text) if word]
    
    for word in words:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] = freqs[word] + 1
    
    return freqs

print(word_freq())