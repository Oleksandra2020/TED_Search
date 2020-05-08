import os
import json
import math
from normalizer import stop_words_removal, UkrainianStemmer, stemmer
from csv_reader import FileExplorer
from node_ import Node


class Search:
    """
    Performs a search on subtitles
    """

    def __init__(self):
        """
        () -> None
        Initializes found talks
        """
        self.talks = self.input_measure()

    def input_measure(self):
        """
        () -> list
        """
        ks = input('Search for videos: ').strip()
        ks = stop_words_removal(ks)
        words_data_file = []
        data_file = []
        for filename in os.listdir('data.2'):
            with open('data.2/' + filename) as f:
                f = json.load(f)
                tf = 0
                for k in ks:
                    # k = UkrainianStemmer(k).stem_word()
                    transcript = f[0][filename[:-5]].split()
                    num_of_words = transcript.count(k)
                    tf += num_of_words
            if tf:
                data_file.append(Node(filename,
                                      Node(tf,
                                           Node(len(transcript)))))

        docs_num = len(os.listdir('data.2'))
        df = len(data_file)
        idf = math.log(docs_num/(df+1))
        for file in data_file:
            tf = file.next.data
            tf_idf = tf*idf
            file.tail(file).next = Node(tf_idf)

            def key(x):
                return x.next.data
            data_file.sort(key=key, reverse=True)
        return data_file[:7]

    def node_pusher(self):
        """
        () -> list
        Returns the list of linked lists related to each talk
        """
        parameter_ls = ['title', 'views', 'url', 'description']
        talks = []
        for talk in self.talks:
            # print(talk.next.data)
            values = FileExplorer().getter(talk.data[:-5], parameter_ls)
            t = Node(talk.data, Node(values[0], Node(
                values[1], Node(values[2], Node(values[3])))))
            talks.append(t)
        return talks


talks = Search().node_pusher()
# print(talks)
for talk in talks:
    print(talk.data, talk.next.next.next.data)
