import pandas as pd
class DataFrameInfo:
    """
    -Describe all columns in the DataFrame to check their data types /
    -Extract statistical values: median, standard deviation and mean from the columns and the DataFrame X (not sure if I need this)
    -Count distinct values in categorical columns/
    -Print out the shape of the DataFrame X don't need this as I already know how many rows there are
    -Generate a count/percentage count of NULL values in each column
    -Any other methods you may find useful
    """
    def __init__(self, dataset):
        self.df = pd.read_csv(dataset)
        pd.set_option('display.max_columns', None)
    
    def show_rows(self, num_rows=5, head_or_tail='head'):
        if head_or_tail == 'head':
            return self.df.head(num_rows)
        elif head_or_tail == 'tail':
            return self.df.tail(num_rows)
        
        return self.df.head(num_rows)

    def get_info(self):
        return self.df.info()

    def describe_columns(self):
        return self.df.describe()

    def count_categorical(self, column):
        return self.df[column].value_counts()

    def null_percentages(self):
        print("Percentage of null values per column:")
        return self.df.isnull().mean() * 100