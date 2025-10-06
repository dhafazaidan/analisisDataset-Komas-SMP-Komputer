# aktifkan venv dulu (kalau belum)
.venv\Scripts\Activate.ps1

# install paket (kalau belum)
pip install -r requirements.txt

# generate grafik
python -m src.main
# atau
python scripts\make_charts.py
