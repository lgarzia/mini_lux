# %%
import imp
import mini_lux
import pandas as pd
from datetime import datetime

data = {
        "inty_integers": [1, 2, 3] * 7,
        "floaty_floats": [1.234_523_45, 2.456_234, None] * 7,
        "stringy_strings": ["rabbit", "leopard", None] * 7,
        "datie_dates":[datetime(2020,1,1), datetime(2021,2,3), None]*7,
        "all_nulls":[None, None, None] *7,
        "mostly_nulls": [None, None, None]*6 + [None, None, 'Not Null']

    }
#df = LuxDataFrame(data)
df = pd.DataFrame(data)
print(type(df))
# %%
from mini_lux import MiniLuxDataFrame
import pandas as pd
from datetime import datetime

data = {
        "inty_integers": [1, 2, 3] * 7,
        "floaty_floats": [1.234_523_45, 2.456_234, None] * 7,
        "stringy_strings": ["rabbit", "leopard", None] * 7,
        "datie_dates":[datetime(2020,1,1), datetime(2021,2,3), None]*7,
        "all_nulls":[None, None, None] *7,
        "mostly_nulls": [None, None, None]*6 + [None, None, 'Not Null']

    }
df = MiniLuxDataFrame(data)
#df = pd.DataFrame(data)
print(type(df))
# %%
