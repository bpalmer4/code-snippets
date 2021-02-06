import string
import pandas as pd
import numpy as np

def fake_data(nrows=1000, ncols=5, ncats=4, dates=True, seed=42):
    """ A function to return a DataFrame of fake data.
        Usage: df = fake_data()
        Arguments
        - nrows - 1 <= int - number of rows in the DataFrame
        - ncols - 1 <= int <= 26 - number of columns in the DataFrame (max=26)
        - ncats - 0 <= int <= 26 - number of categories in 'Group' column 
                  (max=26, if 0 specified the Group column is not added)
        - dates - boolean - whether to include a 'Date' column
        - seed - None or int - preset the random state for a repeatable 
                 DataFrame
        Returns a pandas DataFrame."""

    if seed is not None:
        np.random.seed(seed)
    
    col_names = list(string.ascii_uppercase[:ncols])
    df = ((pd.DataFrame(np.random.rand(nrows, ncols), columns=col_names)
           - 0.5)
          .cumsum()
         )
        
    if ncats:
        cat_names = list(string.ascii_lowercase[:ncats])
        df['Group'] = [np.random.choice(cat_names)
                              for _ in range(len(df))]
    if dates:
        df['Date'] = pd.date_range('1/1/2018',
                                   periods=len(df), freq='D')
    return df

#print(fake_data().head())
#df = fake_data() 