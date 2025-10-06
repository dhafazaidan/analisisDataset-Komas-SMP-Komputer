"""
src/main.py — entry point: load .env, baca dataset, preprocess, buat grafik
"""
import os
import pandas as pd
from config.config import DATA_FILE, OUTPUT_DIR, FIGURE_DPI, YEAR
from src.utils.io import read_excel_multiheader, normalize_numeric_columns
from src.analysis.visualize import bar_total_per_provinsi, grouped_negeri_swasta_topn

def detect_columns(df: pd.DataFrame):
    """
    Deteksi kolom penting secara robust berbasis substring.
    Return dict: {provinsi, negeri, swasta, total}
    """
    def pick(pattern: str):
        lp = pattern.lower()
        for c in df.columns:
            if lp in str(c).lower():
                return c
        return None

    prov_col = pick("provinsi")
    total_col = pick("total")

    negeri_col = None
    swasta_col = None
    for c in df.columns:
        lc = str(c).lower()
        if "status satuan pendidikan" in lc and "negeri" in lc:
            negeri_col = c
        if "status satuan pendidikan" in lc and "swasta" in lc:
            swasta_col = c

    return {"provinsi": prov_col, "negeri": negeri_col, "swasta": swasta_col, "total": total_col}

def preprocess(df: pd.DataFrame, cols: dict) -> pd.DataFrame:
    """
    - Normalisasi angka
    - Trim teks provinsi
    - Drop baris 'Indonesia' & 'Luar Negeri'
    - Tambah kolom gap (jika memungkinkan)
    """
    num_cols = [cols.get("negeri"), cols.get("swasta"), cols.get("total")]
    num_cols = [c for c in num_cols if c is not None]
    df = normalize_numeric_columns(df, num_cols)

    if cols.get("provinsi") in df.columns:
        df[cols["provinsi"]] = df[cols["provinsi"]].astype(str).str.strip()
        mask = ~df[cols["provinsi"]].str.contains("Indonesia", case=False, na=False) & \
               ~df[cols["provinsi"]].str.contains("Luar Negeri", case=False, na=False)
        df = df[mask].copy()

    if cols.get("negeri") in df.columns and cols.get("swasta") in df.columns:
        df["Gap_Negeri_minus_Swasta"] = df[cols["negeri"]] - df[cols["swasta"]]

    return df

def main():
    print(f"Loading: {DATA_FILE}")
    # dataset lo ada di sheet "data" dan header mulai baris ke-3 (0-based index 2)
    df = read_excel_multiheader(DATA_FILE, header_start=2, sheet_name="data")
    cols = detect_columns(df)

    for r in ["provinsi", "total"]:
        if cols.get(r) is None:
            raise ValueError(f"Kolom wajib tidak ditemukan: {r}")

    df = preprocess(df, cols)
    print(df[[c for c in [cols.get("total"), cols.get("negeri"), cols.get("swasta")] if c]].describe())


    # Output charts
    chart1 = os.path.join(OUTPUT_DIR, "chart1_total_per_provinsi.png")
    chart2 = os.path.join(OUTPUT_DIR, "chart2_negeri_vs_swasta_top10.png")

    bar_total_per_provinsi(df, cols["provinsi"], cols["total"], chart1, dpi=FIGURE_DPI, year=YEAR)

    if cols.get("negeri") and cols.get("swasta"):
        grouped_negeri_swasta_topn(
            df, cols["provinsi"], cols["total"], cols["negeri"], cols["swasta"],
            chart2, topn=10, dpi=FIGURE_DPI, year=YEAR
        )
        print(f"[OK] Charts saved ->\n- {chart1}\n- {chart2}")
    else:
        print(f"[OK] Chart saved ->\n- {chart1}\n[WARN] Kolom Negeri/Swasta tidak lengkap, chart2 dilewati.")

if __name__ == "__main__":
    main()
