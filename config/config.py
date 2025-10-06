"""
config.py — load .env & expose constants
"""
import os
from dotenv import load_dotenv

# project root = parent dari folder src
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(ROOT_DIR, ".env")

if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)
else:
    load_dotenv()

DATA_FILE = os.getenv("DATA_FILE", "../data/raw/Proporsi_SMP_komputer_2024.xlsx")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "../reports/figures")
FIGURE_DPI = int(os.getenv("FIGURE_DPI", "200"))
YEAR = int(os.getenv("YEAR", "2024"))

os.makedirs(OUTPUT_DIR, exist_ok=True)