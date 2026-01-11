# Market Regime Classifier

This project classifies market conditions into:
- Trending vs Ranging
- High vs Low Volatility

The goal is to demonstrate rule-based decision logic and feature
engineering relevant to applied machine learning and analytics roles.

## Why This Project Exists


This project was created to explore how market conditions can be systematically classified using interpretable, rule based logic. In many real world decision support systems, especially in finance and applied analytics, understanding why a decision is made is as important as the decision itself.

Rather than starting with a black box machine learning model, this project prioritizes transparency by using well-known technical indicators to define market regimes such as trending vs ranging and high vs low volatility. This approach mirrors how domain experts often reason about markets before introducing more complex models.

The long-term goal of this project is to use the rule-based regime labels as a foundation for supervised machine learning. These labels can serve as training targets or features, enabling a gradual transition from deterministic logic to data driven models while maintaining interpretability and control.

## Indicators Used
- RSI
- MACD
- ATR

## Status
Rule-based regime classification implemented with a focus on interpretability and feature logic. 
Current work emphasizes clear decision rules and feature design.
Next steps include dataset generation and supervised model training.

## Regime Classification Logic

Market regimes are determined using a combination of momentum and volatility indicators.

- RSI is used to assess directional momentum
- Volatility metrics are used to distinguish stable vs unstable conditions

Rules were chosen to prioritize interpretability over complexity, reflecting
real-world decision-support systems rather than black-box models.

The output of this process is a labeled market regime dataset that can be
used for downstream analysis or as training data for supervised models.
