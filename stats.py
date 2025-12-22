from collections import Counter 

def count_words(text):
    return len(text.split())

def count_chars(text):
    freq = Counter(text.lower())
    return dict(freq)




