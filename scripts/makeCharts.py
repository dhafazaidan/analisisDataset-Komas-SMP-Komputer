import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import main

if __name__ == "__main__":
    main()
    print("Selesai.")