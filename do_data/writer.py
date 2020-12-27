import pandas as pd
import json
import os

class Writer():
    def __init__(self, folder='data'):
        self.folder = folder
        self.path = os.environ['PWD'] + os.sep + self.folder + os.sep

    def to_package(self, df, filename, compression=True, echo=True):
        print('Packaging Writer')
        self.to_csv(df, filename, compression, echo)
        self.to_pickle(df, filename, echo)

    def to_csv(self, df, filename='file.csv', compression=True, echo=True):
        csv = '.csv'
        zipped = '.zip'

        self.filename = filename

        if csv not in filename:
            filename_csv = str(filename + csv)
            self.filename = filename_csv

        path = self.path + self.filename

        if compression:

            compression_opts = dict(method='zip',
                                    archive_name=self.filename)

            filename_zip = str(filename + zipped)
            self.filename = filename_zip
            path = self.path + self.filename
            print(path)

            df.to_csv(path, index=False,
                      compression=compression_opts)

            if echo:
                print('Compressed dataframe to', path)
                print()

        else:
            df.to_csv(path)

            if echo:
                print('Wrote dataframe to', path)
                print()

    def to_pickle(self, df, filename='file.pickle', echo=True):
        pickle = '.pickle'

        self.filename = filename

        if pickle not in filename:
            filename_ammended = str(filename + pickle)
            self.filename = filename_ammended

        path = self.path + self.filename
        df.to_pickle(path)

        if echo:
            print('Wrote dataframe to', path)
            print()

    def to_json(self, df, filename='file.json', orient='columns', echo=True):
        self.filename = filename
        path = self.path + self.filename
        df.to_json(path, orient=orient)

        if echo:
            print('Wrote dataframe to', path)
            print()
