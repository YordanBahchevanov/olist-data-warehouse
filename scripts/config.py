from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

ORIGINAL_DATA = BASE_DIR / "datasets" / "original"
MESSY_DATA = BASE_DIR / "datasets" / "messy"

MESSY_DATA.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Random Seed
# -----------------------------

RANDOM_SEED = 42

# -----------------------------
# Percentages
# -----------------------------

MISSING_RATE = 0.03            # 3%
DUPLICATE_RATE= 0.01            # 1%
SPACE_RATE = 0.05               # 5%
UPPERCASE_RATE = 0.05           # 5%
CORRUPTED_DATE_RATE = 0.05           # 5%

NEGATIVE_VALUE_RATE = 0.002     # 0.2%
BROKEN_FK_RATE = 0.005          # 0.5%