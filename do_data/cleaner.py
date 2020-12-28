import pandas as pd
import numpy as np
import fuzzy_pandas as fpd

class Cleaner():
    def __init__(self):
        pass

    def stage_one(self, df, col):
        df[col] = df[col].str.strip()
        df[col] = df[col].str.title()

        print(df[col].unique())




