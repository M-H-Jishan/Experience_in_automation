# AI Trading Agent

Sentiment-based ML trading agent using Lumibot, Alpaca, and FinBERT.

## Features

- FinBERT sentiment analysis on financial news
- ML-based trading strategy with bracket orders (take profit + stop loss)
- Backtesting with Yahoo Finance data
- Live paper trading via Alpaca
- Configurable symbol and cash-at-risk

## Quick Start

```bash
cp .env.example .env  # Add your Alpaca API keys
pip install -r requirements.txt

# Run backtest (default)
python paper_trading.py

# Run live paper trading
TRADING_MODE=live python paper_trading.py
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `ALPACA_API_KEY` | — | Alpaca API key |
| `ALPACA_API_SECRET` | — | Alpaca API secret |
| `ALPACA_BASE_URL` | `https://paper-api.alpaca.markets` | Alpaca base URL |
| `TRADING_MODE` | `backtest` | `backtest` or `live` |

## Strategy

The MLTrader strategy:
1. Fetches news headlines for the target symbol (last 3 days)
2. Runs FinBERT sentiment analysis on headlines
3. Buys if sentiment is positive with >99.9% confidence
4. Sells if sentiment is negative with >99.9% confidence
5. Uses bracket orders with 20% take profit and 5% stop loss

## Docker

```bash
docker build -t ai-trading-agent .
docker run --env-file .env ai-trading-agent
```

## Testing

```bash
pytest -v
```
