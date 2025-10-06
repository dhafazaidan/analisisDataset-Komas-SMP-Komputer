"""
utils/io.py — helper I/O untuk Excel multi-header & normalisasi angka
"""
import pandas as pd
from typing import Optional, List

def read_excel_multiheader(filepath: str, header_start: int = 2, sheet_name: Optional[str] = None) -> pd.DataFrame:
    """
    Baca Excel yang kemungkinan punya 2 baris header (multiindex),
    lalu flatten jadi 1 baris nama kolom.
    """
    xls = pd.ExcelFile(filepath)
    if sheet_name is None:
        sheet_name = xls.sheet_names[0]

    df = pd.read_excel(filepath, sheet_name=sheet_name, header=[header_start, header_start+1])
    df.columns = [" ".join([str(x) for x in tup if str(x) != 'nan']).strip() for tup in df.columns.values]
    return df

def normalize_numeric_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Robust normalizer untuk kolom persentase:
    1) Bersihkan spasi & simbol persen
    2) Sisakan digit, koma, titik, tanda +/- dan notasi e/E
    3) Asumsikan locale Indonesia: '.' = thousand sep, ',' = decimal
    4) Konversi ke float
    5) Rescale berbasis MAX sampai rentang 0–100
    6) Clamp ke [0, 100] sebagai guard-rail
    """
    import re
    for c in columns:
        if c not in df.columns:
            continue

        # --- cleaning & parsing
        s = (
            df[c].astype(str)
            .str.strip()
            .str.replace('%', '', regex=False)
            .apply(lambda x: re.sub(r"[^0-9,.\-eE+]", "", x))  # keep digits/.,eE+-
        )
        # locale: buang thousand '.', lalu koma -> titik (decimal)
        s = s.str.replace('.', '', regex=False)   # "1.234" -> "1234"
        s = s.str.replace(',', '.', regex=False)  # "45,67" -> "45.67"
        df[c] = pd.to_numeric(s, errors='coerce')

        # --- rescale by MAX (bukan median), supaya outlier kebawa turun
        # contoh: 4596 -> 459.6 -> 45.96 (loop bagi 10 sampai max <= 100)
        max_val = df[c].max(skipna=True)
        while pd.notna(max_val) and max_val > 100:
            df[c] = df[c] / 10.0
            max_val = max(df[c].max(skipna=True), 0)

        # --- clamp safety ke [0, 100]
        df[c] = df[c].clip(lower=0, upper=100)

    return df