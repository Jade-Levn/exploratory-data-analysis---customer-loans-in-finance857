import pandas as pd


class DataTransform:
    """
    
    """
    def to_categorical(self, df, column):
        self.df[column] = self.df[column].astype('category')
        return self.df
    
    def format_dates(self, df, column):
        self.df[column] = pd.to_datetime(self.df[column], format='%b-%Y')
        return self.df

    def term_to_numeric(self, df, column):
        self.df[column] = self.df[column].astype('string')
        self.df[column] = self.df[column].str.extract('(\d+)', expand=False) \
            .astype(float)
        return self.df

    def drop_column(self, df, column):
        return self.df.drop(column, axis=1, inplace=True)