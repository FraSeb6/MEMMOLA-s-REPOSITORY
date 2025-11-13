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