import pandas as pd
import re

# Load CSV with ; as delimiter
df = pd.read_csv("Lajiryhmäeditori.csv", delimiter=";")

# Function to decide "Line" or "Point"
def choose_type(row):
    taulun_nimi = str(row.get("Taulun nimi", "")).lower()
    if "viiva" in taulun_nimi:
        return "Line"
    elif "teksti" in taulun_nimi:
        return "Text"
    return "Symbol"

# Apply function to each row
df["Const"] = df.apply(choose_type, axis=1)

# Filter out rows where Tyyppi == "Ryhmä" (case-insensitive)
df = df[df["Tyyppi"].str.lower() != "ryhmä"]

# Clean the "Nimi" column
def clean_name(name):
    if pd.isna(name):
        return ""
    name = str(name).strip()
    # Remove Excel-style leading ="..."
    if name.startswith("=\"") and name.endswith("\""):
        name = name[2:-1]
    # Keep only letters, numbers, underscore, and space
    name = re.sub(r"[^A-Za-z0-9_ ]", "", name)
    return name

df["Nimi"] = df["Nimi"].apply(clean_name)

# Select needed columns
df_out = df[["Tunnus", "Const", "Nimi"]]

# Write to file with header lines
with open("output.crf", "w", encoding="utf-8") as f:
    # Add the required two lines
    f.write("ClassId\tGeometry\tLayer\n")
    f.write("#\n")
    # Add the content
    for _, row in df_out.iterrows():
        f.write(f"\"{row['Tunnus']}\"\t\"{row['Const']}\"\t\"{row['Nimi']}\"\n")
