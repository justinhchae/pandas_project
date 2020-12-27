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
# print('--- From CSV ---')
# df = reader.to_df('analysis.zip')

## uncomment below to read a pickled file
# benefits: retains pandas categorical meta data
print('--- From Pickle ---')
df = reader.to_df('analysis.pickle')





