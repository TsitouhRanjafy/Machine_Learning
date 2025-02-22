import pandas as pd
import numpy as np

ser = pd.Series()
print("pandas series:",ser)

data = np.array(['t','s','i','t','o'])

ser = pd.Series(data)
print(ser)

