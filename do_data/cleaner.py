import pandas as pd
import numpy as np
import fuzzy_pandas as fpd


class Cleaner():
    def __init__(self):
        pass

    def stage_one(self, df, cols):

        for col in cols:
            df[col] = df[col].str.strip()
            df[col] = df[col].str.title()

            if col == 'item_name':

                key_itemname = {'Toster': 'Toaster'
                                ,'Yoyo': 'Yo-Yo'}

                df[col] = np.where(df[col].isin(key_itemname), df[col].map(key_itemname), df[col])

            if col == 'condition':
                key_itemname = {'Excelent': 'Excellent'
                                , 'Trsh': 'Trash'}

                df[col] = np.where(df[col].isin(key_itemname), df[col].map(key_itemname), df[col])

        return df