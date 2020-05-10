"""
Cleans and stems the lexicographical unit
"""
import re


def stop_words_removal(transcript):
    """
    str -> list
    Returns the list with stop words removed
    >>> stop_words_removal('з пригодами')
    ['пригодами']
    """
    with open('modules/stop_words.txt') as f:
        stop_words = []
        for line in f:
            stop_words.append(line.strip())
    symbs = '[.,()"-~_—♪?!@»‎«:;]'
    for symb in symbs:
        transcript = transcript.replace(symb, '')
    transcript = transcript.strip().split()
    final_tr = []
    word = 0
    while word < len(transcript):
        transcript[word] = transcript[word].lower()
        if transcript[word] not in stop_words:
            final_tr.append(transcript[word])
        word += 1
    return final_tr


def stemmer(word):
    """
    str -> str
    Stems the word
    >>> stemmer("перепонами")
    'перепон'
    >>> word = 'до та після конференції'
    >>> word = stop_words_removal(word)
    >>> print(word)
    ['конференції']
    >>> stemmer(word[0])
    'конференц'
    """
    perfectiveground = r'(ив|ивши|ившись|ыв|ывши|ывшись((?<=[ая])(в|вши|вшись)))$'
    reflexive = r'(с[яьи])$'
    adjective = r'(ими|ій|ий|а|е|ова|ове|ів|є|їй|єє|еє|я|ім|ем|им|ім|их|іх|ою|йми|іми|у|ю|ого|ому|ої)$'
    participle = r'(ий|ого|ому|им|ім|а|ій|у|ою|ій|і|их|йми|их)$'
    verb = r'(сь|ся|ив|ать|ять|у|ю|ав|али|учи|ячи|вши|ши|е|ме|ати|яти|є)$'
    noun = r'(а|ев|ов|е|ями|ами|еи|и|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я|і|ові|ї|ею|єю|ою|є|еві|ем|єм|ів|їв|ю)$'
    rvre = r'[аеиоуюяіїє]'
    derivational = r'[^аеиоуюяіїє][аеиоуюяіїє]+[^аеиоуюяіїє]+[аеиоуюяіїє].*(?<=о)сть?$'
    patterns = [perfectiveground, reflexive, adjective, participle, verb, noun]
    for pattern in patterns:
        temp_word = re.search(r'\w.+(?={})'.format(pattern), word)
        if temp_word:
            word = temp_word.group(0)
            break
    temp_word = re.search(r'\w.+(?={})'.format(derivational), word)
    if not temp_word:
        temp_word = re.search(r'\w.+(?={})'.format(rvre), word)
        if temp_word:
            return temp_word.group(0)
    else:
        word = temp_word.group(0)
    return word
