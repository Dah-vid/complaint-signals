#load file
#remove rows that are not narrative
#remove products that are not top 4
#convert date received frm text to date
#save cleaned file 

import pandas as pd

path = "data/raw/CCDB_Export_13_September_2025_through_October_2025.zip"

#df = read.csv had to check syntax

df = pd.read_csv(path)

#has_narratives = df had to check syntax

has_narratives = df["Consumer complaint narrative"].notna()

narratives = df[has_narratives]

#now how to remove theo ones that are top 4 and how to convert i don tnow 

print(narratives)