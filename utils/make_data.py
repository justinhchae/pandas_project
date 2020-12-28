import pandas as pd
import numpy as np
import numpy.lib.recfunctions as rfn

import os
import uuid
import shortuuid
import random

from do_data.writer import Writer

class MakeData():
    def __init__(self):
        self.hourly = np.timedelta64(1, 'h')
        self.daily = np.timedelta64(1, 'D')
        self.today = pd.Timestamp.now()
        self.writer = Writer()

    def make_random_dates(self, start, end, n):
        """
        source: https://stackoverflow.com/questions/50559078/generating-random-dates-within-a-given-range-in-pandas
        :param start: A string date like '2010-01-01', should be less than end date
        :param end: A string date like '2020-01-01', should be greater than start date
        :param n: number of records to return
        :return: a series of random datetime stamps in a given range
        """
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        start_u = start.value//10**9
        end_u = end.value//10**9
        return pd.DatetimeIndex((10**9*np.random.randint(start_u, end_u, n, dtype=np.int64)).view('M8[ns]'))

    def make_df(self, make_default=True, perfect=False, size=5000, col_names=None, values=None):

        # df = pd.DataFrame()

        if make_default:

            columns = ['Object ID', 'Retrieved Date', 'Retrieved', 'Condition', 'Sector', 'Status', 'Status Date']
            n_cols = len(columns)
            n_sectors = 8
            sectors = [x for x in range(n_sectors)]

            if perfect:
                conditions = ['Excellent', 'Poor', 'Good', 'Spare Parts', 'Trash']
            else:
                conditions = ['Excellent', 'excellent', 'excelent', 'Poor', 'poor', 'Good', 'good', 'Spare Parts',
                              'Trash', 'trsh']

            statuses = ['Inventoried', 'Repaired', 'Pending Repair', 'Pending Inventory', 'Missing']

            def filler():
                arr = np.zeros((size, n_cols))

                dtype = str(arr.dtype)
                dtypes = np.dtype([(n, dtype) for n in columns])

                structured = rfn.unstructured_to_structured(arr, dtypes)
                df = pd.DataFrame.from_records(data=structured)

                df['Object ID'] = df.apply(lambda x:shortuuid.uuid(), axis=1)
                
                df['Retrieved Date'] = self.make_random_dates('2010-01-01', '2020-12-31', size)

                # https://stackoverflow.com/questions/6824681/get-a-random-boolean-in-python
                df['Retrieved'] = df.apply(lambda x: bool(random.getrandbits(1)), axis=1)

                df['Sector'] = df.apply(lambda x: np.random.choice(sectors, 1, replace=True)[0], axis=1)

                df['Condition'] = df.apply(lambda x: np.random.choice(conditions, 1, replace=True)[0], axis=1)

                df['Status'] = df.apply(lambda x: np.random.choice(statuses, 1, replace=True)[0], axis=1)

                df['Status Date'] = self.make_random_dates('2020-01-01', '2020-12-31', size)

                df = df.sort_values(by='Retrieved Date').reset_index(drop=True)

                def shuffle(yr):
                    full = (list(str(yr)))
                    inner = full[1:3]
                    inner.reverse()
                    full[1:3] = inner
                    yr = int(''.join(full))
                    return yr


                if not perfect:
                    n_samples = int(size *.002)

                    if n_samples < 1:
                        n_samples = 1

                    s1 = df.sample(n=n_samples, replace=False, random_state=0)
                    s1['Retrieved Date'] = s1['Retrieved Date'].apply(lambda x: x.replace(year=shuffle(x.year)))
                    df['Retrieved Date'].update(s1['Retrieved Date'])

                    s2 = df.sample(n=n_samples, replace=False, random_state=21)
                    s2['Retrieved Date'] = s2['Retrieved Date'].apply(lambda x: '')
                    df['Retrieved Date'].update(s2['Retrieved Date'])

                    df['Retrieved Date'] = pd.to_datetime(df['Retrieved Date'])

                    s3 = df.sample(n=n_samples, replace=False, random_state=42)
                    s3['Retrieved'] = s3['Retrieved'].apply(lambda x: '')
                    df['Retrieved'].update(s3['Retrieved'])

                return df

            df_out = filler()

            # print(df[(df['Retrieved Date'].isnull()) | (df['Retrieved Date'].dt.year > 2050)])
            # print(df[(df['Retrieved Date'].isnull())])
            # print(df[(df['Retrieved Date'].dt.year > 2050)])
            # print(df[(df['Retrieved'] == '')])
            # print(df[(df['Retrieved'] == True)])

            self.writer.to_csv(df_out, 'source')



        # return df
