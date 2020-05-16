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
        self.talks_num = 7
        self.talks = self.indexer()

    def indexer(self):
        """
        () -> list
        Returns a sorted by normalized term frequency list of linked lists
        >>> word = Search('глобальне потепління')
        >>> print(word.talks[0])
        alinakozoriz o08ykAqLOxk.json 24 1103 45.85741528659984 
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
                    translator = transcript[1] + transcript[2]
                    num_of_words = transcript.count(k)
                    tf += num_of_words
            if tf:
                data_file.append(Node(translator,
                                      Node(filename,
                                           Node(tf,
                                                Node(len(transcript))))))

        docs_num = len(os.listdir('data'))
        df = len(data_file)
        idf = math.log(docs_num/(df+1))

        def key(x):
            return x.tail().data
        for file in data_file:
            tf = file.get_tf()
            tf_idf = tf*idf
            file.tail().next = Node(tf_idf)
        data_file.sort(key=key, reverse=True)
        return data_file

    def translator_search(self, video_id):
        """
        str -> int
        Returns the number of videos translated by the same person
        >>> search = Search('одяг')
        >>> talk = search.node_pusher()[0]
        >>> search.translator_search(talk.get_id())
        1
        """
        filename = 'data/' + video_id
        counter = 0
        with open(filename) as f:
            f = json.load(f)
            transcript = f[0][video_id[:-5]].split()
            translator = transcript[1] + transcript[2]
            for talk in self.talks:
                if talk.get_translator() == translator:
                    counter += 1
        return counter

    def node_pusher(self):
        """
        () -> list
        Returns the list of linked lists related to each talk
        >>> word = Search('глобальне потепління')
        >>> talks = word.node_pusher()
        >>> print(talks[0].get_id(), talks[1].get_id())
        o08ykAqLOxk.json rUO8bdrXghs.json
        >>> talks[0].get_title()
        'How we can make the world a better place by 2030'
        >>> talks[0].tail().previous.previous.data
        1141254
        """
        parameter_ls = ['title', 'views', 'url', 'description']
        talks = []
        for talk in self.talks[:self.talks_num]:
            values = FileExplorer().getter(talk.next.data[:-5], parameter_ls)
            t = Node(data=talk.data, next=Node(talk.next.data))
            t.next.next = values.next
            talks.append(t)
        return talks
