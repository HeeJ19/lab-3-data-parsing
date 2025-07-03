import pandas as pd

def clean_strings(strings): 
    if not isinstance(strings, pd.Series):
        raise TypeError("Not a pandas Series")

    strings = strings.dropna()
    strings = strings.str.lower()
    strings = strings.str.strip()
    strings = strings.str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    return strings