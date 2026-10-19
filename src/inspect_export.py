import pandas as pd

PATH = "data/raw/CCDB_Export_21_August_2026.zip"

# 1. Read a sample, not the whole 177 MB file
df = pd.read_csv(PATH, nrows=1000)

# 2. What columns exist, and what type pandas gave each one
print(df.columns.tolist())
print(df.dtypes)

# 3. Find the narrative and product columns by name
narr_col = [c for c in df.columns if "narrative" in c.lower()][0]
prod_col = [c for c in df.columns if c.lower() == "product"][0]

# 4. Count usable narratives: not missing AND not just whitespace
text = df[narr_col]
usable = text.notna() & (text.astype(str).str.strip() != "")
print(f"Usable narratives: {usable.sum()} of {len(df)}")

# 5. Which products dominate
print(df[prod_col].value_counts().head(10))
