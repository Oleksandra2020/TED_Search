"""
Retrieves data from csv file
"""
import pandas as pd
from node_ import Node, TwoWayNode


class FileExplorer:
    """
    Retrieves columns from csv file
    """

    def __init__(self):
        """
        () -> None
        Initializes the filename, data frame and ids
        """
        self.file = 'ted_metadata_kaggle.csv'
        self.df = self.csv_reader()
        self.ids = None

    def csv_reader(self):
        """
        () -> dict
        Returns a list of ids
        >>> FileExplorer().csv_reader()[:4]
           Unnamed: 0  comments  ...     views  vidID_youtube
        0           0      4553  ...  47227110    iG9CE55wbtY
        1           1       265  ...   3200520    rDiGYuQicpA
        2           2       124  ...   1636292    NEjZt0y6OOw
        3           3       200  ...   1697550    gQ-cZRmHfs4
        <BLANKLINE>
        [4 rows x 19 columns]
        """
        data = pd.read_csv(self.file)
        self.df = pd.DataFrame(data=data)
        return self.df

    def id_retriever(self):
        """
        () -> list
        Returns the list of video idss
        >>> file = FileExplorer()
        >>> ids = file.id_retriever()
        >>> len(ids)
        2550
        >>> for i in range(3):
        ...    print(ids[i], end = ', ')
        iG9CE55wbtY, rDiGYuQicpA, NEjZt0y6OOw, 
        """
        self.ids = self.df['vidID_youtube']
        return self.ids

    def getter(self, i, parameters):
        """
        str -> int
        Returns the number of views given the video id i
        >>> file = FileExplorer()
        >>> file.getter('iG9CE55wbtY', ['views']).next.data
        47227110
        """
        views = self.df.get(['views', 'vidID_youtube']).T
        values = TwoWayNode()
        for view in range(len(self.df['vidID_youtube'])):
            try:
                if i in self.df['vidID_youtube'][view]:
                    for parameter in parameters[::-1]:
                        next_node = values
                        values.data = self.df[parameter][view]
                        values.previous = TwoWayNode()
                        values = values.previous
                        values.next = next_node
                    return values
            except TypeError:
                pass

