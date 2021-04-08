
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px

from scipy.signal import savgol_filter

import seaborn as sns
import os
import json
import sidetable

from collections import deque
from collections import defaultdict
from pandas.io.json import json_normalize
# import geopandas

from do_data.writer import Writer

class EDA():
    def __init__(self, folder='figures'):
        self.folder = folder
        self.path = os.environ['PWD'] + os.sep + self.folder + os.sep

    def eda_1(self, df):
        df1 = df.groupby(['product_vendor'])['line_gross_sales_total'].agg(['mean', 'sum','count']).reset_index()
        print(df1)

    def eda_2(self, df, date_col, cat, target):
        df1 = df[(df[cat] == "Bodha") |
                 (df[cat] == "Wildflower") |
                 (df[cat] == "Papa & Barkley")
                 ]

        new_cats = list(df1[cat].unique())
        all_cats = list(df1[cat].cat.categories.unique())
        cat_diff = (set(all_cats) - set(new_cats))

        for category in cat_diff:
            df1[cat].cat.remove_categories(category, inplace=True)

        df1=df1[[date_col, cat, target]]

        # use value counts and reindex for aggs
        cols = df1.columns.tolist()
        counts = df1[cols].value_counts()
        df2 = counts.to_frame().reset_index()
        df2.rename(columns={0: 'count'}, inplace=True)

        # sort the df by date to plot in a given order
        df2 = df2.sort_values(by=date_col).reset_index(drop=True)

        # two options to smooth line
        sg = str(target + '_svg')
        df2[sg] = savgol_filter(df2[target], 51, 3)
        sma = str('SMA_' + target)
        df2[sma] = df2[target].rolling(30, min_periods=1).mean()

        print(df2)

        plt.figure()
        sns.lineplot(data=df2
                     , x=date_col
                     , y=sma
                     , hue=cat
                     , alpha=.6
                     , palette='Set2')



        plt.legend(fontsize='small')
        plt.title('EDA2 - Aggregated Counts of Sales by Vendor\nWith Simple Moving Average')
        self.filename = 'eda_2'
        path = self.path + self.filename
        plt.savefig(path)
        plt.show()

        fig = px.line(df2
                      , x=date_col
                      , y=sma
                      , color=cat)
        fig.show()



