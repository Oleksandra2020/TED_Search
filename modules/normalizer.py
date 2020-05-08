import re
import json


def stop_words_removal(transcript):
    """
    str -> list
    Returns the list with stop words removed
    """
    with open('modules/DataSearch/stop_words.txt') as f:
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
    adjectives = 'ими|ій|ий|а|е|ова|ове|ів|є|їй|єє|еє|я|ім|ем|им|ім|их|іх|ою|йми|іми|у|ю|ого|ому|ої|'
    participle = 'ий|ого|ому|им|ім|а|ій|у|ою|ій|і|их|йми|их|'
    noun = 'а|ев|ов|е|ями|ами|еи|и|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я|і|ові|ї|ею|єю|ою|є|еві|ем|єм|ів|їв|ю|'
    reflexive = 'ся|cь|cи|'
    perfectiveground = 'ив|ивши|ившись|в|вши|вшись|'
    verb = 'сь|ся|ив|ать|ять|у|ю|ав|али|учи|ячи|вши|ши|е|ме|ати|яти|є'
    word1 = word

    pat1 = 'ивши|ившись|вши|вшись|ими|ала|яхом|лася|іння|ення'
    pat2 = 'ять|ють|лю|ти|ать|ять|ити|ої|ові|ова|ове|али|ена|учи|ячи|ьмо|вши|ши|ів'
    pat3 = 'ьмося|ється|ються|еться|аться|тися|тись|ість|ого|іми|те|ею|єю|ою|йми|ому|ями|ами|иям|ям|ием|ємо|йми|юся|ем|ам|ла|ач|ом|еи|ію|ой|ій|їй|ий|ию|ім|им|ім|их|іх|ою|ої|ий'
    pat4 = 'єє|еє|ою|их|их|ев|ов|ей|ах|иях|ях|ью|ия|еві|ем|єм|ів|їв|ся|cь|cи|ив|сь|ся|ив|ав|ме|ти'
    pat5 = 'а|е|є|я|у|ю|і|е|и|й|о|ї|є|в|ь'
    patterns = [pat3, pat2, pat5, pat4, pat1]
    pat6 = 'пере|за|при|пре|прі|зі|із|з|с'

    def checker(word, pattern):
        temp_word = re.findall(r'\w.+(?={})'.format(pattern), word)
        # print(temp_word)
        # if temp_word:
        #     temp_word = re.findall(r'(?<=){}(\w.+)'.format(pat6), temp_word[0])
        if temp_word:
            return temp_word
        return False
    i = 0
    while i < len(patterns):
        res = checker(word, patterns[i])
        if res:
            # return word1, res
            return res[0]
        i += 1
    return word


class UkrainianStemmer():
    def __init__(self, word):
        self.word = word
        self.vowel = r'аеиоуюяіїє'  # http://uk.wikipedia.org/wiki/Голосний_звук
        self.perfectiveground = r'(ив|ивши|ившись|ыв|ывши|ывшись((?<=[ая])(в|вши|вшись)))$'
        # http://uk.wikipedia.org/wiki/Рефлексивне_дієслово
        self.reflexive = r'(с[яьи])$'
        # http://uk.wikipedia.org/wiki/Прикметник + http://wapedia.mobi/uk/Прикметник
        self.adjective = r'(ими|ій|ий|а|е|ова|ове|ів|є|їй|єє|еє|я|ім|ем|им|ім|их|іх|ою|йми|іми|у|ю|ого|ому|ої)$'
        # http://uk.wikipedia.org/wiki/Дієприкметник
        self.participle = r'(ий|ого|ому|им|ім|а|ій|у|ою|ій|і|их|йми|их)$'
        # http://uk.wikipedia.org/wiki/Дієслово
        self.verb = r'(сь|ся|ив|ать|ять|у|ю|ав|али|учи|ячи|вши|ши|е|ме|ати|яти|є)$'
        # http://uk.wikipedia.org/wiki/Іменник
        self.noun = r'(а|ев|ов|е|ями|ами|еи|и|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я|і|ові|ї|ею|єю|ою|є|еві|ем|єм|ів|їв|ю)$'
        self.rvre = r'[аеиоуюяіїє]'
        self.derivational = r'[^аеиоуюяіїє][аеиоуюяіїє]+[^аеиоуюяіїє]+[аеиоуюяіїє].*(?<=о)сть?$'
        self.RV = ''

    def ukstemmer_search_preprocess(self, word):
        word = word.lower()
        word = word.replace("'", "")
        word = word.replace("ё", "е")
        word = word.replace("ъ", "ї")
        return word

    def s(self, st, reg, to):
        orig = st
        self.RV = re.sub(reg, to, st)
        return (orig != self.RV)

    def stem_word(self):
        word = self.ukstemmer_search_preprocess(self.word)
        if not re.search('[аеиоуюяіїє]', word):
            stem = word
        else:
            p = re.search(self.rvre, word)
            start = word[0:p.span()[1]]
            self.RV = word[p.span()[1]:]

            # Step 1
            if not self.s(self.RV, self.perfectiveground, ''):

                self.s(self.RV, self.reflexive, '')
                if self.s(self.RV, self.adjective, ''):
                    self.s(self.RV, self.participle, '')
                else:
                    if not self.s(self.RV, self.verb, ''):
                        self.s(self.RV, self.noun, '')
            # Step 2
            self.s(self.RV, 'и$', '')

            # Step 3
            if re.search(self.derivational, self.RV):
                self.s(self.RV, 'ость$', '')

            # Step 4
            if self.s(self.RV, 'ь$', ''):
                self.s(self.RV, 'ейше?$', '')
                self.s(self.RV, 'нн$', u'н')

            stem = start + self.RV
        return stem


# doc = 'SN7wO06Yz1E.json'
# trans = stop_words_removal(doc)
# for word in range(len(trans)):
#     trans[word] = stemmer(trans[word])
# print(trans)
