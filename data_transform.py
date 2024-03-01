import pandas as pd


class DataTransform:
    """
    
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

    def to_categorical(self, column):
        self.df[column] = self.df[column].astype('category')
        return self.df
    
    def format_dates(self, column):
        self.df[column] = pd.to_datetime(self.df[column], format='%b-%Y')
        return self.df

    def term_to_numeric(self, column):
        self.df[column] = self.df[column].astype('string')
        self.df[column] = self.df[column].str.extract('(\d+)', expand=False) \
            .astype(float)
        return self.df