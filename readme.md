# Locus Automatic CRF generator 

This Python script converts types from `Lajiryhmäeditori.csv` into a cross reference file where each type is it's seperate layer. You can export the CSV from Locus Cloud's admin tools.

---

## Input

The script expects a CSV file named **`Lajiryhmäeditori.csv`** with a `;` delimiter.  
Relevant columns in the CSV are:

- **Tunnus** → numeric ID  
- **Nimi** → name/identifier  
- **Tyyppi** → name/identifier 

---

Example CSV snippet:

```csv
Tunnus;Nimi;Kuvaus;Huomautus;Muutospäivä;Tyyppi;Taulun numero;Taulun nimi;Lajityyppi
1;aj_tonttijakoindeksi;Imatra;;"=""2024-10-15T12:15:01""";Ryhmä;;;
2;venepaikat;;;"=""2019-05-10T10:05:02""";Ryhmä;;;
3;aj_vp_talvisailytys;;;"=""2019-05-10T10:05:02""";Ryhmä;;;
153008;"=""reunakivi yläreuna""";;"=""Imatran kaupungin lisäämä""";"=""2025-03-03T11:41:42""";Laji;202;Maastoviiva;Xcity
195951603;"=""os5_joen nimi""";;;"=""2019-03-26T15:36:50""";Laji;105;Maastoteksti;Xcity
260350043;aak_Palloviiva;;;"=""2019-03-26T15:36:50""";Laji;210;"=""Asemakaavan viiva""";Xcity