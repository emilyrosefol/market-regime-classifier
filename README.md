# Market Regime Classifier

This project classifies market conditions into:
- Trending vs Ranging
- High vs Low Volatility

The goal is to demonstrate rule-based decision logic and feature
engineering relevant to applied machine learning and analytics roles.

## Indicators Used
- RSI
- MACD
- ATR

## Status
## Status
Rule-based regime classification implemented.
Next steps include dataset generation and supervised model training.

## Regime Classification Logic

Market regimes are determined using a combination of momentum and volatility indicators.

- RSI is used to assess directional momentum
- Volatility metrics are used to distinguish stable vs unstable conditions

Rules were chosen to prioritize interpretability over complexity, reflecting
real-world decision-support systems rather than black-box models.

The output of this process is a labeled market regime dataset that can be
used for downstream analysis or as training data for supervised models.
