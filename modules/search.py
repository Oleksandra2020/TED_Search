"""
Performs searching
"""

import os
import json
import math
from normalizer import stop_words_removal, stemmer
from csv_reader import FileExplorer
from node_ import Node


class Search:
    """
    Performs a search through subtitles
    """

    def __init__(self, ks):
        """
        () -> None
        Initializes found talks
        """
        self.ks = ks
        self.talks = self.indexer()

    def indexer(self):
        """
        () -> list
        >>> word = Search('глобальне потепління')
        >>> print(word.talks[0])
        rUO8bdrXghs.json 11 1516 
        """
        self.ks = stop_words_removal(self.ks)
        words_data_file = []
        data_file = []
        for filename in os.listdir('data'):
            with open('data/' + filename) as f:
                f = json.load(f)
                tf = 0
                for k in self.ks:
                    k = stemmer(k)
                    transcript = f[0][filename[:-5]].split()
                    num_of_words = transcript.count(k)
                    tf += num_of_words
            if tf:
                data_file.append(Node(filename,
                                      Node(tf,
                                           Node(len(transcript)))))

        docs_num = len(os.listdir('data'))
        df = len(data_file)
        idf = math.log(docs_num/(df+1))

        def key(x):
            return x.next.data
        for file in data_file:
            tf = file.next.data
            tf_idf = tf*idf
            file.tail().next = Node(tf_idf)
            data_file.sort(key=key, reverse=True)
        return data_file[:7]

    def node_pusher(self):
        """
        () -> list
        Returns the list of linked lists related to each talk
        >>> word = Search('глобальне потепління')
        >>> talks = word.node_pusher()
        >>> print(talks[0].data, talks[1].data)
        rUO8bdrXghs.json A6GLw12jywo.json
        >>> talks[0].next.data
        'New thinking on the climate crisis'
        >>> talks[0].tail().previous.previous.data
        1751426
        """
        parameter_ls = ['title', 'views', 'url', 'description']
        talks = []
        for talk in self.talks:
            values = FileExplorer().getter(talk.data[:-5], parameter_ls)
            t = Node(talk.data)
            t.next = values.next
            talks.append(t)
        return talks
