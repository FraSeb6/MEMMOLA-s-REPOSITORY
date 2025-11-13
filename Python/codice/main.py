#!/usr/bin/env python3
"""
Compute brand-level metrics from LLDB-data.csv:
- Average price per brand
- % of occasions with Feature on per brand
- % of occasions with Display on per brand

Assumes long-format data with one row per brand × occasion. If the file doesn't
already have a `Brand` column, we construct it from dummies:
  1=Tide, 2=Wisk, 3=Era, 4=Surf.
"""

from pathlib import Path
import argparse
import pandas as pd
import numpy as np
import sys

NA_TOKENS = ["", "NA", "N/A", "na", "n/a", "NULL", "Null", "null", "NaN", "nan", "-", "--", "?"]
BRAND_MAP = {1: "Tide", 2: "Wisk", 3: "Era", 4: "Surf"}

def read_lldb(path: Path) -> pd.DataFrame:
    """Read LLDB-data.csv with tuned import settings."""
    df = pd.read_csv(
        path,
        sep="|",
        encoding="utf-8-sig",
        skiprows=1,      # skip banner line
        header=0,
        index_col=0,     # drop the extraneous index column
        skipinitialspace=True,
        engine="c",
        na_values=NA_TOKENS,
        keep_default_na=True,
        low_memory=False,
    )
    # Ensure numeric
    for c in ["Price", "Feature", "Display", "Tide", "Wisk", "Era", "Choice"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def ensure_brand(df: pd.DataFrame) -> pd.DataFrame:
    """Add Brand column (1=Tide, 2=Wisk, 3=Era, 4=Surf) based on dummies."""
    for c in ["Tide", "Wisk", "Era"]:
        if c not in df.columns:
            df[c] = 0
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)
    df["Brand"] = np.select(
        [df["Tide"] == 1, df["Wisk"] == 1, df["Era"] == 1],
        [1, 2, 3],
        default=4
    ).astype(int)
    return df

def compute_brand_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Return a table with N, AvgPrice, PctFeature, PctDisplay by brand."""
    # Ensure relevant columns are numeric
    for c in ["Price", "Feature", "Display"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    grp = df.groupby("Brand", as_index=True)
    out = grp.agg(
        N=("Price", "size"),
        AvgPrice=("Price", "mean"),
        PctFeature=("Feature", lambda s: (s.fillna(0) > 0).mean() * 100.0),
        PctDisplay=("Display", lambda s: (s.fillna(0) > 0).mean() * 100.0),
    ).reindex([1,2,3,4])
    out = out.reset_index().rename(columns={"Brand":"BrandCode"})
    out["Brand"] = out["BrandCode"].map(BRAND_MAP)
    out = out[["BrandCode","Brand","N","AvgPrice","PctFeature","PctDisplay"]]
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", default="LLDB-data.csv", help="Path to LLDB-data.csv")
    ap.add_argument("--out", dest="out_path", default="LLDB-brand-metrics.csv", help="Path for metrics CSV")
    args = ap.parse_args()

    in_path = Path(args.in_path)
    if not in_path.exists():
        print(f"Error: input file not found: {in_path}", file=sys.stderr)
        sys.exit(2)

    df = read_lldb(in_path)
    df = ensure_brand(df)

    metrics = compute_brand_metrics(df)
    metrics.to_csv(args.out_path, index=False, encoding="utf-8")

    print("=== Brand-level metrics ===")
    print(metrics.to_string(index=False))
    print(f"\nSaved metrics → {Path(args.out_path).resolve()}")

if __name__ == "__main__":
    main()