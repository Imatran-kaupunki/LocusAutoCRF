import pandas as pd

# Load CSV with ; as delimiter
df = pd.read_csv("Lajiryhmäeditori.csv", delimiter=";")

# Select needed columns
df_out = df[["Tunnus", "Nimi"]].copy()

# Add constant "Line" column
df_out.insert(1, "Const", "Line")

# Write to file in required format (tab-separated, quoted)
with open("output.txt", "w", encoding="utf-8") as f:
    for _, row in df_out.iterrows():
        f.write(f"\"{row['Tunnus']}\"\t\"{row['Const']}\"\t\"{row['Nimi']}\"\n")
