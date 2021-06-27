import pandas as pd
import os

df = pd.DataFrame()
df = pd.read_excel("F:\\ProjectDjango\\websiteanalyzer\\templates\Excel\main.xlsx",index_col=False)
print(list(df["InternalLinksName"]))
