def classify_regime(df):
    """
    Classifies the current market regime based on technical indicators.

    Returns:
        dict: {
            'trend': 'TRENDING' or 'RANGING',
            'volatility': 'HIGH' or 'LOW'
        }
    """

    latest = df.iloc[-1]

    # Trend logic
    trending = (
        abs(latest['macd_hist']) >
        df['macd_hist'].rolling(20).mean().iloc[-1]
        and (latest['rsi'] > 55 or latest['rsi'] < 45)
    )

    # Volatility logic
    high_volatility = (
        latest['atr'] >
        df['atr'].rolling(20).mean().iloc[-1]
    )

    return {
        "trend": "TRENDING" if trending else "RANGING",
        "volatility": "HIGH" if high_volatility else "LOW"
    }
