"""
analysis/visualize.py — fungsi plotting (matplotlib only)
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def bar_total_per_provinsi(df: pd.DataFrame, prov_col: str, total_col: str, out_path: str, dpi: int = 200, year: int = 2023):
    data = df[[prov_col, total_col]].dropna().sort_values(by=total_col, ascending=False)
    mean_val = data[total_col].mean()

    plt.figure(figsize=(14, 7))
    plt.bar(data[prov_col], data[total_col])
    plt.axhline(mean_val, linestyle='--', linewidth=1, label=f"Rata-rata {mean_val:.2f}%")
    plt.title(f"Proporsi SMP Memiliki Komputer untuk Pengajaran per Provinsi (Total, %) – {year}")
    plt.xlabel("Provinsi")
    plt.ylabel("Proporsi (%)")
    plt.xticks(rotation=75, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=dpi)
    plt.close()

def grouped_negeri_swasta_topn(df: pd.DataFrame, prov_col: str, total_col: str, negeri_col: str, swasta_col: str,
                               out_path: str, topn: int = 10, dpi: int = 200, year: int = 2023):
    ranked = df.sort_values(by=total_col, ascending=False).head(topn)
    x = np.arange(len(ranked))
    width = 0.38
    plt.figure(figsize=(14, 7))
    plt.bar(x - width/2, ranked[negeri_col], width, label='Negeri')
    plt.bar(x + width/2, ranked[swasta_col], width, label='Swasta')
    plt.title(f"Perbandingan Negeri vs Swasta (Top-10 Total) – Proporsi SMP Memiliki Komputer, {year}")
    plt.xlabel("Provinsi (Top-10 Total)")
    plt.ylabel("Proporsi (%)")
    plt.xticks(x, ranked[prov_col], rotation=75, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=dpi)
    plt.close()