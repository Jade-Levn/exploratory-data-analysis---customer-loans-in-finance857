import pandas as pd


class DataFrameInfo:
    
    def describe_columns(self, df):
        return df.describe()