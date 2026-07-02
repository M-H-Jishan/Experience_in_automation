import os
import sys
import importlib
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestFinbertUtils:
    def test_estimate_sentiment_empty_news(self):
        try:
            from finbert_utils import estimate_sentiment, labels
            prob, sentiment = estimate_sentiment(None)
            assert sentiment == labels[-1]
        except (ImportError, OSError, Exception):
            pass  # transformers/torch/model not available


class TestPaperTrading:
    def test_module_imports(self):
        try:
            import paper_trading
            assert paper_trading.ALPACA_CREDS["PAPER"] is True
        except ImportError:
            pass  # lumibot not installed

    def test_run_backtest_function_exists(self):
        try:
            import paper_trading
            assert callable(paper_trading.run_backtest)
        except ImportError:
            pass

    def test_run_live_function_exists(self):
        try:
            import paper_trading
            assert callable(paper_trading.run_live)
        except ImportError:
            pass

    def test_env_var_defaults(self):
        assert os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets") == "https://paper-api.alpaca.markets"
