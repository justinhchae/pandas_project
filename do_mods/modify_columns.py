import pandas as pd

class ModifyColumns():
    def __init__(self):
        pass

    def parse_cols(self, df):
        """
        :params df: a data frame
        :args: replaces col headers with lower case and removes spaces
        :returns a df with modified columns
        """
        print('------ Parsing columns text with lower string and underscores')
        df.columns = map(str.lower, df.columns)
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.replace('-', '_')

        print(df.columns)
        return df
