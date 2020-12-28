# categorical

A series of object-oriented libraries built with PyCharm around the Pandas package.

## Background

This project represents a collection of my most-used Pandas-oriented methods and transformations to wrangle and analyze data. 

A focus of this repository is on categorical data types.

## Environment

* environment.yml

* Python 3.8

* PyCharm on MacOS

## Code

* [do_data.getter](https://github.com/justinhchae/categorical/blob/main/do_data/getter.py): Wrapper function that reads table data (as csv or zipped csv) to Pandas DataFrame

* [do_data.writer](https://github.com/justinhchae/categorical/blob/main/do_data/writer.py): Wrapper function that writes DataFrame to csv, pickle, and compressed csv (zip) files

* [do_mods.modify_categories](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_categories.py): Wrapper function that changes DataFrame columns to categorical

* [do_mods.modify_columns](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_columns.py): Function that changes column values to lower case with no spaces

* [do_mods.modify_dates](https://github.com/justinhchae/categorical/blob/main/do_mods/modify_dates.py): Function that processes date columns as datetime

## Data

* source.csv: A table of made-up records. Each row is an event where an item was retrieved. 

Retrieved Date, Item Name, Retrieved, Condition, Sector

* analysis.zip: A compressed version of source.csv after processing.

* analysis.pickle: A serialized version of source.csv after processing. 


