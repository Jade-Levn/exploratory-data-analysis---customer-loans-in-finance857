from IPython import display
import pandas as pd


"""
Task 2 to-do list:
-Create DataTransform Class /
-Describe columns /
-Count distinct categorical colums - how?
-Shape data set
-Calculate number or percentage of nulls
"""


class DataTransform:
    """
    -Correct format of columns
        >Numerical representation?
        >Categorical representation?
        >Correct date format?

    1. View columns with info?  
    """
    def load_dataframe(self, csv, show_num_rows=5, head_or_tail='head'):
        self.df = pd.read_csv(csv)
        pd.set_option('display.max_columns', None)
        
        if head_or_tail == 'head':
            return self.df.head(show_num_rows)
        elif head_or_tail == 'tail':
            return self.df.tail(show_num_rows)
        return self.df.head(show_num_rows)
    
    def view_column_dtypes(self):
        self.df
        return self.df.info()
    
    def format_column(self):
        self.df
        pass
    
       
class DataFrameInfo:
    
    def describe_columns(self, df):
        return df.describe()

    def convert_columns(self, df):
        #write code to convert columns
        pass
    
