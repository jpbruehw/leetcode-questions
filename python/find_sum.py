import pandas as pd
import numpy as np

# create test df
data = {
    'some_data': [20.5, 21.0, 'str', 22.1, 19.8, None],
    'other_data': [55, 60, 65, 'str', 70, 75],
    'more_data': [5.5, True, 3.3, 4.4, 2.2, 6.6],
    'data_with_nan': [5, 0.2, 0.1, np.nan, 0.0, 0.3],
}

# create df
test_data = pd.DataFrame(data)

def is_col(col_name, df):
    """
       Takes name of column and dataframe
       as arguments and returns whether col
       is in the passed dataframe
    """
    if col_name in df.columns:
        return True
    else:
        print(f"{col_name} is not valid column in dataframe")
        return False

def is_num(val):
    """
       This helper checks whether the val
       that is passed in is a float or an integer
       we are not considering complex numbers as valid
       also need to check for booleans since isinstance will
       evaluate to true if the bool is true regardless
       of the value we are checking for
    """
    if isinstance(val, bool):
        return 0
    elif isinstance(val, (float, int)):
        return val
    else:
        return 0

def find_col_sum(col_name, df):
    """
       This function takes the name of a col
       and returns the sum of the column as
       a single value
    """
    if is_col(col_name, df):
        return sum(is_num(val) for val in df[col_name] if not pd.isna(val))
    else:
        return 0
    
# test outputs
print("Invalid Column Example:")
find_col_sum("fake_column", test_data)
print("-----------------------------")
print("Other Column Sums:")
col_sums = {
    col_name: find_col_sum(col_name, test_data) for col_name in test_data.columns
    }
print(col_sums)