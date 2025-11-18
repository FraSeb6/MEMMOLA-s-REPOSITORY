import pandas as pd

try:
    from IPython.display import display
except Exception:
    display = None

# 1) Carica il dataset (metti il path giusto se non è nella stessa cartella)
df = pd.read_csv("raw_data_214.csv")

def _norm(s: str) -> str:
    return "".join(ch for ch in s.lower() if ch.isalnum())

colmap = { _norm(c): c for c in df.columns }
candidate_keys = ["valid_name", "validname", "valid-name", "valid name"]

col_valid = None
for key in candidate_keys:
    if _norm(key) in colmap:
        col_valid = colmap[_norm(key)]
        break

# fallback: cerca colonne che contengono "valid" e "name"
if col_valid is None:
    possibili = [c for c in df.columns if "valid" in c.lower() and "name" in c.lower()]
    if possibili:
        col_valid = possibili[0]

if col_valid is None:
    raise ValueError("Non trovo la colonna 'valid_name'. Colonne disponibili: " + ", ".join(df.columns))

print(f"Userò la colonna: {col_valid}")

# 3) Normalizza i valori (trim spazi, rimuovi doppi spazi, capitalizza) e ricava unici
serie_norm = (
    df[col_valid]
      .dropna()
      .astype(str).str.strip()
      .replace("", pd.NA).dropna()
      .str.replace(r"\s+", " ", regex=True)
      .str.title()
)

# 3a) Elenco dei tipi di piante (valori unici, ordinati)
tipi_unici = pd.DataFrame(
    sorted(serie_norm.unique()),
    columns=["valid_name"]
)

print(f"Numero di tipi (unici): {tipi_unici.shape[0]}")

# Mostra la tabella dei tipi unici (in Jupyter usa display, altrimenti stampa in testo)
if display:
    display(tipi_unici)
else:
    print(tipi_unici.to_string(index=False))

# Solo i nomi (uno per riga)
print("\nNomi unici (valid_name):")
for name in tipi_unici["valid_name"]:
    print(name)

# (Opzionale) Salva anche su CSV
tipi_unici.to_csv("valid_name_unici.csv", index=False)
print("\nElenco salvato in: valid_name_unici.csv")

# 3b) Frequenze per ciascun tipo (top 20 a schermo; togli .head(20) per tutte)
frequenze = (
    serie_norm.value_counts()
    .rename_axis("valid_name")
    .reset_index(name="count")
)
frequenze.head(20)

# 4) Filtra il dataset originale per le tre specie richieste
specie_interesse = [
    "Pinus Contorta",
    "Pinus Monticola",
    "Pseudotsuga Menziesii",
]

# Prendiamo gli indici delle righe che (dopo normalizzazione) corrispondono a queste specie
idx_specie = serie_norm[serie_norm.isin(specie_interesse)].index

# Tabella uguale all'originale ma solo con le osservazioni delle tre specie
df_tre_specie = df.loc[idx_specie].copy()

print("\nRighe totali per le tre specie:", df_tre_specie.shape[0])

# Mostra la tabella filtrata
if display:
    display(df_tre_specie)
else:
    print(df_tre_specie.head().to_string(index=False))

# (Opzionale) Salva la tabella filtrata su CSV
output_path = "raw_data_214_tre_specie.csv"
df_tre_specie.to_csv(output_path, index=False)
print("\nTabella filtrata salvata in:", output_path)

import matplotlib.pyplot as plt
import numpy as np

# --- FILTRO PER LE TRE SPECIE DI INTERESSE (stessa logica di prima) ---
specie_interesse = [
    "Pinus Contorta",
    "Pinus Monticola",
    "Pseudotsuga Menziesii",
]

# Uso la serie normalizzata che hai già creato (serie_norm)
idx_specie = serie_norm[serie_norm.isin(specie_interesse)].index

# Sottoinsieme del dataset originale solo con le tre specie
df_tre_specie = df.loc[idx_specie].copy()

# --- CALCOLO DEL TREND DI ABBONDANZA NEL TEMPO ---
# Sommo l'ABUNDANCE per anno e specie
trend = (
    df_tre_specie
      .groupby(["YEAR", "valid_name"], as_index=False)["ABUNDANCE"]
      .sum()
      .sort_values("YEAR")
)

# --- PLOT: LONG-TERM TREE ABUNDANCE HISTOGRAM (BARPLOT) ---
plt.figure(figsize=(12, 6))

# Anni ordinati
anni = sorted(trend["YEAR"].unique())
x = np.arange(len(anni))

# Specie presenti
specie = trend["valid_name"].unique()
n_specie = len(specie)

# Larghezza delle barre (divido lo spazio dell'anno tra le specie)
width = 0.8 / n_specie

for i, sp in enumerate(specie):
    sub = trend[trend["valid_name"] == sp]
    # Mappo year -> abundance e costruisco la lista allineata a "anni"
    mappa = dict(zip(sub["YEAR"], sub["ABUNDANCE"]))
    y = [mappa.get(a, 0) for a in anni]

    # Offset orizzontale per non sovrapporre le barre
    offset = (i - (n_specie - 1) / 2) * width
    plt.bar(x + offset, y, width, label=sp)

plt.xlabel("Year")
plt.ylabel("Total abundance (sum of ABUNDANCE)")
plt.title("Long-term tree abundance histogram per year and species")
plt.xticks(x, anni, rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

# --- PLOT MENSILE PER PINUS CONTORTA DAGLI ANNI '70 IN POI ---
# Filtra solo Pinus contorta (usando una normalizzazione semplice del nome)
df_pinus = df_tre_specie[
    df_tre_specie["valid_name"].astype(str).str.strip().str.title() == "Pseudotsuga Menziesii"
].copy()

# Tieni solo le osservazioni dagli anni '70 in poi (YEAR >= 1970)
df_pinus = df_pinus[df_pinus["YEAR"] >= 1970].copy()

# Costruisci una variabile year_month (usiamo il giorno 1 per tutti i mesi)
df_pinus["year_month"] = pd.to_datetime(
    {
        "year": df_pinus["YEAR"].astype(int),
        "month": df_pinus["MONTH"].astype(int),
        "day": 1,
    },
    errors="coerce",
)

# Raggruppa per mese e somma l'ABUNDANCE
trend_mensile = (
    df_pinus
        .groupby("year_month", as_index=False)["ABUNDANCE"]
        .sum()
        .sort_values("year_month")
)

plt.figure(figsize=(12, 6))
plt.plot(trend_mensile["year_month"], trend_mensile["ABUNDANCE"], marker="o")

plt.xlabel("Year-Month")
plt.ylabel("Total abundance (sum of ABUNDANCE)")
plt.title("Monthly abundance trend for Pseudotsuga Menziesii (from 1970 onwards)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()