from stop_words import get_stop_words

with open('stop_words.txt', 'w') as f:
    stop_words = get_stop_words('uk')
    for word in range(len(stop_words)):
        stop_words[word] += '\n'
    f.writelines(stop_words)