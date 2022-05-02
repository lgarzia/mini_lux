__version__ = 0.1

import pandas as pd

global originalDF
# Keep variable scope of original pandas df
originalDF = pd.core.frame.DataFrame

class MiniLuxDataFrame(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        super(MiniLuxDataFrame, self).__init__(*args, **kwargs)
        self.mini_lux_attribute = 'Luke Garzia'

override_pandas = True

if override_pandas:
    pd.DataFrame = MiniLuxDataFrame
    