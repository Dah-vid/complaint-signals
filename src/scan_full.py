import pandas as pd


PATH = "data/raw/CCDB_Export_13_September_2025_through_October_2025.zip"
df = pd.read_csv(PATH)

#print(len(df))

#print("Non-empty narratives:", df["Consumer complaint narrative"].notna().sum())






has_narratives = df["Consumer complaint narrative"]. notna()

contains_narratives = df[has_narratives]

print(len(contains_narratives))
print(contains_narratives["Product"].value_counts())
