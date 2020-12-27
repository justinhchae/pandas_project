import pandas as pd

class ModifyColumns():
    def __init__(self):
        pass

    def parse_cols(self, df):
        print('------ Parsing columns text with lower string and underscores')
        df.columns = map(str.lower, df.columns)
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.replace('-', '_')
        return df
