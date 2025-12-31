​You​
import pandas as pd

from indicators import rsi, macd, atr
from regime_rules import classify_regime


def main():
    # Load data (placeholder path)
    df = pd.read_csv("data/btc_1h.csv")

    # Calculate indicators
    df["rsi"] = rsi(df["close"])
    macd_line, signal_line, macd_hist = macd(df["close"])
    df["macd"] = macd_line
    df["macd_signal"] = signal_line
    df["macd_hist"] = macd_hist
    df["atr"] = atr(df)

    # Classify market regime
    regime = classify_regime(df)

# Asisgn regime labels to all rows (rule-based labeling)
df["trend_regime"] = regime["trend"]
df["volatility_regime"] = regime["volatility"]

# Export labeled dataset for downstream ML modeling
df.to_csv("data/labeled_market_regimes.csv", index=False)

print("Market Regime:", regime["trend"])
print("Volatility:", regime["volatility"])


if __name__ == "__main__":
    main()



