import pandas as pd


PATH = "data/raw/CCDB_Export_21_August_2026.zip" 
df = pd.read_csv(PATH)

print(len(df))

print("Non-empty narratives:", df["Consumer complaint narrative"].notna().sum())
