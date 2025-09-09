import pandas as pd

# Load CSV with ; as delimiter
df = pd.read_csv("Lajiryhmäeditori.csv", delimiter=";")

# Function to decide "POLYLINEZ" or "POINTZ"
def choose_type(row):
    taulun_nimi = str(row.get("Taulun nimi", "")).lower()
    if "viiva" in taulun_nimi:
        return "POLYLINEZ"
    return "POINTZ"

# Apply function to each row
df["Const"] = df.apply(choose_type, axis=1)

# Filter out rows where Tyyppi == "Ryhmä"
df = df[df["Tyyppi"] != "Ryhmä"]

# Select needed columns
df_out = df[["Tunnus", "Const", "Nimi"]]

# Write to file in required format (tab-separated, quoted)
with open("output.crf", "w", encoding="utf-8") as f:
    for _, row in df_out.iterrows():
        f.write(f"\"{row['Tunnus']}\"\t\"{row['Const']}\"\t\"{row['Nimi']}\"\n")
