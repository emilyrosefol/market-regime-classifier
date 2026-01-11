"""
generate_dataset.py

Creates a labeled dataset of market regimes by:
1) loading historical price data (CSV)
2) computing indicators (RSI, MACD, ATR)
3) applying rule-based regime classification
4) saving a new CSV with features + regime labels

Output: data/market_regimes.csv
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

# Import your existing indicator + rule logic
# Adjust these imports if your function names differ.
from indicators import add_rsi, add_macd, add_atr
from regime_rules import classify_regime


# ---------- Config ----------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

INPUT_CSV = DATA_DIR / "raw_prices.csv"        # <-- put your input file name here
OUTPUT_CSV = DATA_DIR / "market_regimes.csv"   # <-- this will be created

# Expected columns in the input CSV (edit if yours differ)
COL_TIME = "timestamp"
COL_OPEN = "open"
COL_HIGH = "high"
COL_LOW = "low"
COL_CLOSE = "close"


def validate_input(df: pd.DataFrame) -> None:
    """Raise a helpful error if required columns are missing."""
    required = {COL_TIME, COL_OPEN, COL_HIGH, COL_LOW, COL_CLOSE}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing required columns in input CSV: {sorted(missing)}\n"
            f"Found columns: {list(df.columns)}\n"
            "Fix: rename your CSV headers or update COL_* names in generate_dataset.py"
        )


def main() -> None:
    # 1) Load
    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Input CSV not found at: {INPUT_CSV}\n"
            "Fix: place your historical price file in /data and name it raw_prices.csv "
            "or update INPUT_CSV."
        )

    df = pd.read_csv(INPUT_CSV)

    # Basic cleanup
    df.columns = [c.strip().lower() for c in df.columns]
    validate_input(df)

    # Sort by time (important for indicators)
    df = df.sort_values(COL_TIME).reset_index(drop=True)

    # 2) Compute indicators (using your existing functions)
    # These should add columns like: rsi, macd, atr
    df = add_rsi(df, close_col=COL_CLOSE)
    df = add_macd(df, close_col=COL_CLOSE)
    df = add_atr(df, high_col=COL_HIGH, low_col=COL_LOW, close_col=COL_CLOSE)

    # 3) Apply regime rules
    # classify_regime should return a label like:
    # "TRENDING_HIGH_VOL", "RANGING_LOW_VOL", etc.
    df["regime"] = df.apply(classify_regime, axis=1)

    # 4) Save (keep it clean: only useful columns)
    out_cols = [COL_TIME, COL_OPEN, COL_HIGH, COL_LOW, COL_CLOSE, "rsi", "macd", "atr", "regime"]
    df[out_cols].to_csv(OUTPUT_CSV, index=False)

    print(f"✅ Saved labeled dataset to: {OUTPUT_CSV}")
    print("Sample rows:")
    print(df[out_cols].head(5))


if __name__ == "__main__":
    main()

