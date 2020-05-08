import pandas as pd


class FileExplorer:
    """
    Performs useful operations with data
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
        >>> file.views_getter('iG9CE55wbtY')
        47227110
        """
        views = self.df.get(['views', 'vidID_youtube']).T
        values = []
        for view in range(len(self.df['vidID_youtube'])):
            try:
                if i in self.df['vidID_youtube'][view]:
                    for parameter in parameters:
                        values.append(self.df[parameter][view])
                    return values
            except TypeError:
                pass
