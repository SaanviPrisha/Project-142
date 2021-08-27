import pandas as pd
import numpy as np

dataframe = pd.read_csv('articles.csv')
dataframe = dataframe.sort_values(['total_events'], ascending=[False])

output = dataframe[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()