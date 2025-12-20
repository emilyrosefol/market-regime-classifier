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

    print("Market Regime:", regime["trend"])
    print("Volatility:", regime["volatility"])


if __name__ == "__main__":
    main()
