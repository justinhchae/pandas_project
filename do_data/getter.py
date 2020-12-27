import pandas as pd
import os

from do_mods.modify_columns import ModifyColumns

class Reader():
    def __init__(self, folder='data', display_all_cols=True):
        self.folder = folder
        self.path = os.environ['PWD'] + os.sep + self.folder + os.sep
        self.modify_columns = ModifyColumns()

        if display_all_cols:
            pd.set_option('display.max_columns', None)

    def to_df(self
              , filename=None
              , index_col=None
              , usecols=None
              , dtype=None
              , preview=True
              , echo=True
              ):

        if not isinstance(filename, str):
            return "Filename should be a string"

        if filename:
            csv = '.csv'
            pickle = '.pickle'

            if csv in filename or pickle not in filename:
                self.filename = filename
                path = self.path + self.filename

                if echo:
                    print('Reading From:', path)
                    print()

                df = pd.read_csv(path
                                 , index_col=index_col
                                 , usecols=usecols
                                 , dtype=dtype
                                 , low_memory=False
                                 )
                if echo:
                    print('Read dataframe of length', len(df))
                    print()

                if preview:
                    print(df.head(2))
                    print()

                df = self.modify_columns.parse_cols(df)

                return df

            if pickle in filename:
                self.filename = filename
                path = self.path + self.filename

                if echo:
                    print('Reading From:', path)
                    print()

                df = pd.read_pickle(path)

                if echo:
                    print('Read dataframe of length', len(df))
                    print()

                if preview:
                    print(df.head(2))
                    print()

                return df
