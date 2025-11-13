from pathlib import Path
import sys
import pandas as pd
import numpy as np
import glob

#!/usr/bin/env python3
"""
memmola_main.py

Find and load an "orders" dataset (CSV/XLSX) with pandas, check and fix common data types
(notably date/time columns), and print a short report.

Usage:
    python memmola_main.py [path/to/file]
If no path is given the script will try to auto-discover files with "order" in their name
in the current directory.
"""



def find_orders_file(start_dir: str = "."):
        p = Path(start_dir)
        # exact path provided?
        if p.is_file():
                return str(p.resolve())
        # try to find files containing "order" or "orders"
        patterns = ["**/*order*.csv", "**/*orders*.csv", "**/*order*.xlsx", "**/*orders*.xlsx",
                                "**/*order*.xls", "**/*orders*.xls"]
        matches = []
        for pat in patterns:
                matches.extend(glob.glob(str(Path(start_dir) / pat), recursive=True))
        matches = sorted(set(matches))
        return matches[0] if matches else None


def read_file(path: str) -> pd.DataFrame:
        path = Path(path)
        if path.suffix.lower() in [".csv", ".txt"]:
                # Try to read CSV; let pandas determine separators, but use common options
                return pd.read_csv(path, low_memory=False)
        elif path.suffix.lower() in [".xlsx", ".xls"]:
                return pd.read_excel(path)
        else:
                raise ValueError(f"Unsupported file type: {path.suffix}")


def detect_date_columns(df: pd.DataFrame, sample_size: int = 1000):
        candidates = []
        text_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
        # heuristics based on column names
        name_hits = [c for c in df.columns if any(k in c.lower() for k in ("date", "time", "timestamp", "created", "at"))]
        # sample values for other columns that might be date-like
        sample = df[text_cols].head(sample_size)
        for col in text_cols:
                # if name already suspicious, add as candidate
                if col in name_hits:
                        candidates.append(col)
                        continue
                # try to coerce sample to datetime and see ratio of non-NaT
                coerced = pd.to_datetime(sample[col], errors="coerce", infer_datetime_format=True)
                non_na_ratio = coerced.notna().mean()
                if non_na_ratio >= 0.8:
                        candidates.append(col)
        # remove duplicates while preserving order
        seen = set()
        candidates = [c for c in candidates if not (c in seen or seen.add(c))]
        return candidates


def coerce_columns(df: pd.DataFrame):
        report = {"converted_to_datetime": [], "converted_to_numeric": [], "unchanged": []}
        df = df.copy()
        # detect date-like columns
        date_cols = detect_date_columns(df)
        for col in date_cols:
                coerced = pd.to_datetime(df[col], errors="coerce", infer_datetime_format=True)
                non_na_ratio = coerced.notna().mean()
                if non_na_ratio >= 0.5:
                        df[col] = coerced
                        report["converted_to_datetime"].append((col, non_na_ratio))
                else:
                        report["unchanged"].append(col)
        # numeric detection for object columns not already converted
        for col in df.select_dtypes(include=["object", "string"]).columns:
                if col in [c for c, _ in report["converted_to_datetime"]]:
                        continue
                coerced = pd.to_numeric(df[col], errors="coerce")
                non_na_ratio = coerced.notna().mean()
                # require a high ratio to convert to numeric
                if non_na_ratio >= 0.9:
                        # if integers only, convert to Int64 (nullable)
                        if np.all(np.mod(coerced.dropna(), 1) == 0):
                                df[col] = coerced.astype("Int64")
                        else:
                                df[col] = coerced.astype(float)
                        report["converted_to_numeric"].append((col, non_na_ratio))
                else:
                        report["unchanged"].append(col)
        return df, report


def summarize(df: pd.DataFrame, report: dict):
        print("=== Dataframe info ===")
        df.info(show_counts=True)
        print("\n=== Conversion report ===")
        if report["converted_to_datetime"]:
                print("Date/time columns converted:")
                for col, ratio in report["converted_to_datetime"]:
                        print(f" - {col}: {ratio:.2%} values parsed as datetime")
        else:
                print("No date/time columns converted.")
        if report["converted_to_numeric"]:
                print("Numeric columns converted:")
                for col, ratio in report["converted_to_numeric"]:
                        print(f" - {col}: {ratio:.2%} values parsed as numeric")
        if report["unchanged"]:
                print("Unchanged object/string columns (kept as-is):")
                for col in report["unchanged"]:
                        print(f" - {col}")


def main(path_arg: str = None):
        path = path_arg or find_orders_file(".")
        if not path:
                print("No orders file found in current directory. Provide a path as argument.")
                return
        print(f"Loading file: {path}")
        df = read_file(path)
        print(f"Loaded dataframe with shape: {df.shape}")
        # initial quick info
        print("\nInitial dtypes:")
        print(df.dtypes)
        df_fixed, report = coerce_columns(df)
        print("\nAfter attempting coercion:")
        summarize(df_fixed, report)
        # Optionally, save a copy with fixed dtypes next to original
        out_path = Path(path).with_name(Path(path).stem + "_typed" + Path(path).suffix)
        try:
                if out_path.suffix.lower() in [".csv", ".txt"]:
                        df_fixed.to_csv(out_path, index=False)
                else:
                        df_fixed.to_excel(out_path, index=False)
                print(f"\nSaved typed copy to: {out_path}")
        except Exception as e:
                print(f"Could not save typed copy: {e}")


if __name__ == "__main__":
        arg = sys.argv[1] if len(sys.argv) > 1 else None
        # Enhanced CLI behavior: load file, identify & remove empty/wrong/null columns, then continue processing.
        arg = sys.argv[1] if len(sys.argv) > 1 else None
        path = arg or find_orders_file(".")
        if not path:
            print("No orders file found in current directory. Provide a path as argument.")
            sys.exit(0)

        print(f"Loading file: {path}")
        df = read_file(path)
        print(f"Loaded dataframe with shape: {df.shape}")

        # PREPROCESS: identify & remove empty / wrong / largely-null columns.
        # Decisions (implemented conservatively):
        #  - Treat purely-empty or whitespace-only strings as NA before analysis.
        #  - Drop columns that are entirely NA (no information).
        #  - Drop columns with very high NA ratio (>= 98%) as likely useless metadata/garbage.
        #  - Drop pandas-created index columns named "Unnamed: ..." automatically.
        #  - Do NOT drop columns with a single non-NA value (constant) automatically — these might be meaningful flags.
        #
        # Rationale: fully-empty columns are always safe to remove. Very-high-NA columns often come from malformed exports
        # and usually don't carry useful information. We err on the side of caution for constant columns and partially-empty
        # columns so we don't accidentally remove relevant identifiers or business fields.
        df_prep = df.copy()
        # normalize empty strings/whitespace to NA so they count as missing
        df_prep = df_prep.replace(r"^\s*$", pd.NA, regex=True)

        # detect columns that are entirely NA
        all_na_cols = [c for c in df_prep.columns if df_prep[c].isna().all()]

        # detect columns with very high NA ratio (>= 98%)
        high_na_threshold = 0.98
        high_na_cols = [c for c in df_prep.columns if c not in all_na_cols and df_prep[c].isna().mean() >= high_na_threshold]

        # detect pandas "Unnamed" index-like columns
        unnamed_cols = [c for c in df_prep.columns if str(c).lower().startswith("unnamed")]

        # assemble drops (conservative union)
        to_drop = sorted(set(all_na_cols + high_na_cols + unnamed_cols))

        # Report findings
        if not to_drop:
            print("\nNo empty/wrong/null columns identified for removal.")
        else:
            print("\nColumns identified for removal and reasons:")
            for c in to_drop:
                reason = []
                if c in all_na_cols:
                    reason.append("all NULL")
                if c in high_na_cols:
                    reason.append(f">{int(high_na_threshold*100)}% NULL")
                if c in unnamed_cols:
                    reason.append("Unnamed/index-like")
                print(f" - {c}: {', '.join(reason)}")
            # perform drop
            df_prep = df_prep.drop(columns=to_drop)
            print(f"\nDropped {len(to_drop)} columns. New shape: {df_prep.shape}")

        # continue with existing coercion and summary logic on the cleaned dataframe
        df_fixed, report = coerce_columns(df_prep)
        print("\nAfter attempting coercion:")
        summarize(df_fixed, report)

        # save typed copy next to original (as main did)
        out_path = Path(path).with_name(Path(path).stem + "_typed" + Path(path).suffix)
        try:
            if out_path.suffix.lower() in [".csv", ".txt"]:
                df_fixed.to_csv(out_path, index=False)
            else:
                df_fixed.to_excel(out_path, index=False)
            print(f"\nSaved typed copy to: {out_path}")
        except Exception as e:
            print(f"Could not save typed copy: {e}")