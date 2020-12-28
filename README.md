# categorical

A series of object-oriented libraries built with PyCharm around the Pandas package.

## Background

This project represents a collection of my most-used Pandas-oriented methods and transformations to wrangle and analyze data. 

A focus of this repository is on categorical data types.

## Environment

* [environment.yml](https://github.com/justinhchae/categorical/blob/main/environment.yml): Anaconda

* Python 3.8

* PyCharm on MacOS

## Code

* [do_data.getter](https://github.com/justinhchae/categorical/blob/main/do_data/getter.py): Wrapper function that reads table data (as csv or zipped csv) to Pandas DataFrame

* [do_data.writer](https://github.com/justinhchae/categorical/blob/main/do_data/writer.py): Wrapper function that writes DataFrame to csv, pickle, and compressed csv (zip) files

* [do_mods.modify_categories](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_categories.py): Wrapper function that changes DataFrame columns to categorical

* [do_mods.modify_columns](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_columns.py): Function that changes column values to lower case with no spaces

* [do_mods.modify_dates](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_dates.py): Function that processes date columns as datetime

## Usage

```python
from do_data.getter import Reader
from do_data.writer import Writer
from do_mods.modify_categories import ModifyCategories
from do_mods.modify_dates import ModifyDates

reader = Reader()
writer = Writer()
categorize = ModifyCategories()
mod_dates = ModifyDates()

# read source data from a csv
print('--- From Source ---')
df = reader.to_df('source.csv')

df = categorize.make_categories(df=df,
                                cols=['item_name'
                                    , 'condition'
                                    , 'sector'],
                                order={'condition': ['Junk', 'Poor', 'Worn', 'Good', 'Excellent']},
                                )
df = mod_dates.parse_dates(df)


# write the dataframe to a zipped csv and pickle file
writer.to_package(df, 'analysis')

## uncomment below to read df from zipped csv file
# benefits: common cross-platform data format
print('--- From CSV ---')
df = reader.to_df('analysis.zip')

## uncomment below to read a pickled file
# benefits: retains pandas categorical meta data
print('--- From Pickle ---')
df = reader.to_df('analysis.pickle')
```

### Source Data

* [source.csv](https://github.com/justinhchae/categorical/blob/main/data/source.csv): A table of made-up records. Each row is an event where an item was retrieved. 

|  | Retrieved Date  | Item Name | Retrieved | Condition | Sector |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Example | 2019-01-01, 2019-03-4  | Toaster, Lighter  | True, False  | Junk, Excellent  | 1, 2 |
| Data Type | String  | String  | String  | String | Integer |

### Processed Data

* [analysis.zip](https://github.com/justinhchae/categorical/blob/main/data/analysis.zip): A compressed version of source.csv after processing.

* [analysis.pickle](https://github.com/justinhchae/categorical/blob/main/data/analysis.pickle): A serialized version of source.csv after processing. 


|  | retrieved_date  | item_name | retrieved | condition | sector |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Example | 2019-01-01, 2019-03-4  | Toaster, Lighter  | True, False  | Junk, Excellent  | 1, 2 |
| Data Type | pd.Datetime  | Category  | Bool  | Ordered Category | Category |

## References

* Pandas Categorical: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Categorical.html

* Pandas Pickle: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_pickle.html

* Pandas CSV: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

* Pandas Datetime: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
