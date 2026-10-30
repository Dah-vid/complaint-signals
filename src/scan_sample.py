import pandas as pd #im importing pandas

PATH = "data/raw/CCDB_Export_21_August_2026.zip" #changinbg the path but why, also why data, why raw
df = pd.read_csv(PATH, nrows=1000)

print(df.shape) # check shape 
print(df.dtypes) #check data types

narrative_count = df["Consumer complaint narrative"]. notna().sum()
print("Non-empty narratives:", narrative_count)
print(df["Product"].value_counts())