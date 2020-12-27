import pandas as pd
import numpy as np
import re

class ModifyDates():
    def __init__(self):
        self.hourly = np.timedelta64(1, 'h')
        self.daily = np.timedelta64(1, 'D')
        self.today = pd.Timestamp.now()

    def get_date_cols(self, df):
        date_pattern = r'_date'
        date_cols = [c for c in df.columns if re.search(date_pattern, c)]
        return date_cols

    def parse_dates(self, df, cols=None):

        if cols is None:
            cols = self.get_date_cols(df)

        for col in cols:
            if col in cols:
                df[col] = pd.to_datetime(df[col],
                                     errors='coerce',
                                     infer_datetime_format=False)

        print('------ Parsed date columns')
        print()

        return df

