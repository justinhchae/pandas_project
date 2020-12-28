import numpy as np
import pandas as pd

class ModifyCategories():
    def __init__(self):
        pass

    def make_categories(self, df, cols, order=None, standardize=True, echo=True, preview=True):
        """
        :param df: a Pandas DataFrame
        :param cols: a list of column names
        :param order: dictionary keyed by a string (col name) and a list of ordered values as strings
                      {String: [list of strings]}
                      {ColName: [col1, col2, col3,...]}
                      if ordered, provide data from lowest value to highest value
        :return: a Pandas DataFrame with cols as Categorical
        """
        print('------ Parsing columns as categories')

        col_list = list(df.columns)

        df[cols] = df[cols].astype('category')

        if order:
            for key, value in order.items():

                if key in col_list:

                    if standardize:
                        cat_list = [x.strip() for x in value]
                        cat_list = [x.title() for x in cat_list]
                    else:
                        cat_list = value

                    df[key] = df[key].cat.as_ordered()
                    df[key] = df[key].cat.reorder_categories(cat_list, ordered=True)

                    cat_col = str(key + '_cat_num')
                    df[cat_col] = df[key].cat.codes

                    # a sorted list of unique values only true if ordered
                    cats = df[cat_col].unique()
                    cats.sort()

                    if echo:
                        print('Ordered Column:', key, '| In order:', list(zip(cat_list, cats)))
                        print()

                    if preview:
                        print(df.head(2))
                else:
                    print('Skipping', key, 'Reason: Not a Column in DF')
                    print()

        print(df.dtypes)

        return df


