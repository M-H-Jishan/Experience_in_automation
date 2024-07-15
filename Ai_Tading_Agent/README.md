# AI-Powered Trading Bot

An intelligent trading bot that leverages sentiment analysis of news headlines to make trading decisions on the stock market. Built with Python, it uses the Lumibot library for strategy implementation and integrates with the Alpaca trading platform.

## Overview

This trading bot employs the following key components:

1. **Sentiment Analysis**: Utilizes the FinBERT model to analyze sentiment from recent news headlines.
2. **Trading Strategy**: Implements a strategy based on sentiment scores to make buy/sell decisions.
3. **Risk Management**: Uses bracket orders with predefined take-profit and stop-loss levels.
4. **Backtesting**: Capabilities to test the strategy on historical data.

## Project Structure

- `paper_trading.py`: Main script containing the `MLTrader` strategy class and backtesting setup.
- `finbert_utils.py`: Utility functions for sentiment analysis using FinBERT.

## Dependencies

- Python 3.7+
- lumibot
- alpaca-trade-api
- transformers
- torch
- timedelta
- Other standard Python libraries

## Configuration

1. Alpaca API Credentials:
   Create a `.env` file in the project root with your Alpaca API credentials:

2. Trading Parameters:
Adjust the following parameters in `paper_trading.py`:
- `symbol`: The stock symbol to trade (default is "SPY")
- `cash_at_risk`: Fraction of cash to risk per trade (default is 0.5)

## Key Components

### MLTrader Strategy

The `MLTrader` class in `paper_trading.py` defines the trading strategy:

- `initialize()`: Sets up initial parameters and Alpaca API connection.
- `position_sizing()`: Calculates the quantity of shares to trade based on available cash and risk parameters.
- `get_sentiment()`: Retrieves recent news and analyzes sentiment using FinBERT.
- `on_trading_iteration()`: Main trading logic executed on each iteration.

### Sentiment Analysis

The `finbert_utils.py` file contains functions for sentiment analysis:

- Uses the ProsusAI/finbert model for financial sentiment analysis.
- `estimate_sentiment()`: Processes news headlines and returns sentiment probability and label.

## Trading Logic

1. Retrieves news headlines for the past three days.
2. Analyzes sentiment of the headlines.
3. If sentiment is positive with high probability (>0.999):
- Places a buy order if not already in a long position.
4. If sentiment is negative with high probability (>0.999):
- Places a sell order if not already in a short position.
5. Uses bracket orders with:
- Take-profit at 20% above buy price or 20% below sell price.
- Stop-loss at 5% below buy price or 5% above sell price.

## Backtesting

The script includes a backtesting setup using YahooDataBacktesting:

- Default period: January 1, 2020 to December 31, 2023
- Modify the `start_date` and `end_date` in `paper_trading.py` to change the backtesting period.

To run a backtest, execute the `paper_trading.py` script.

## Live Trading

To switch to live trading:

1. Ensure your Alpaca API credentials are set up for a live trading account.
2. Uncomment the following lines at the end of `paper_trading.py`:
```python
# trader = Trader()
# trader.add_strategy(strategy)
# trader.run_all()

Customization

Adjust the sleeptime in initialize() to change the trading frequency.
Modify the sentiment probability threshold in on_trading_iteration() for more or less frequent trading.
Customize the take-profit and stop-loss percentages in the order creation.

Disclaimer
This trading bot is for educational and research purposes only. It is not financial advice. Use caution and consult with a qualified financial advisor before engaging in real-world trading.
License
This project is licensed under the MIT License.   