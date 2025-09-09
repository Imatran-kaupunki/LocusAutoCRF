# LocusAutoCRF generator for exporting

This Python script converts data from `Lajiryhmäeditori.csv` into a custom tab-separated format with quoted values.  

## Input

The script expects a CSV file named **`Lajiryhmäeditori.csv`** with a `;` delimiter.  
Relevant columns in the CSV are:

- **Tunnus** → numeric ID  
- **Nimi** → name/identifier  

Example CSV snippet:

```csv
Tunnus;Nimi;Kuvaus;Huomautus;Muutospäivä;Tyyppi
1;aj_tonttijakoindeksi;Imatra;;="2024-10-15T12:15:01";Ryhmä
2;venepaikat;;;;="2019-05-10T10:05:02";Ryhmä
3;aj_vp_talvisailytys;;;;="2019-05-10T10:05:02";Ryhmä
