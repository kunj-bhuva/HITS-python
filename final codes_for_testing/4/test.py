import unittest
from datetime import datetime

from c import Asset, Market, Transaction, Portfolio, Simulator

class TestAsset(unittest.TestCase):
    def test_new_asset(self):
        asset = Asset("AAPL", 150.00)
        self.assertEqual(asset.symbol, "AAPL")
        self.assertEqual(asset.price, 150.00)

class TestMarket(unittest.TestCase):
    def setUp(self):
        self.market = Market()

    def test_add_new_asset(self):
        self.market.update_price("AAPL", 150.00)
        self.assertEqual(self.market.assets["AAPL"].price, 150.00)

    def test_update_existing_asset_price(self):
        self.market.update_price("AAPL", 150.00)
        self.market.update_price("AAPL", 155.00)
        self.assertEqual(self.market.assets["AAPL"].price, 155.00)

    def test_add_new_asset_not_in_market(self):
        self.market.update_price("GOOG", 2000.00)
        self.assertEqual(self.market.assets["GOOG"].price, 2000.00)

    def test_update_existing_asset_negative_price(self):
        self.market.update_price("AAPL", 150.00)
        self.market.update_price("AAPL", -100.00)
        self.assertEqual(self.market.assets["AAPL"].price, -100.00)

    def test_update_existing_asset_zero_price(self):
        self.market.update_price("AAPL", 150.00)
        self.market.update_price("AAPL", 0.00)
        self.assertEqual(self.market.assets["AAPL"].price, 0.00)

class TestTransaction(unittest.TestCase):
    def test_new_transaction(self):
        transaction = Transaction("AAPL", 10, 150.00, 'buy')
        self.assertEqual(transaction.symbol, "AAPL")
        self.assertEqual(transaction.quantity, 10)
        self.assertEqual(transaction.price, 150.00)
        self.assertEqual(transaction.type, 'buy')
        self.assertIsInstance(transaction.timestamp, datetime)

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.market = Market()
        self.portfolio = Portfolio()

    def test_buy_asset(self):
        self.market.update_price("AAPL", 150.00)
        self.assertTrue(self.portfolio.buy("AAPL", 10, self.market))

    def test_sell_asset(self):
        self.market.update_price("AAPL", 150.00)
        self.portfolio.buy("AAPL", 10, self.market)
        self.assertTrue(self.portfolio.sell("AAPL", 5, self.market))

    def test_get_value(self):
        self.market.update_price("AAPL", 150.00)
        self.portfolio.buy("AAPL", 10, self.market)
        self.assertEqual(self.portfolio.get_value(self.market), 1500.00)

    def test_risk_profile(self):
        self.market.update_price("AAPL", 150.00)
        self.portfolio.buy("AAPL", 10, self.market)
        self.assertEqual(self.portfolio.risk_profile(self.market), "Conservative")

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = Simulator()

    def test_run_scenario(self):
        result = self.simulator.run_scenario()
        self.assertIsInstance(result, dict)
        self.assertIn("cash", result)
        self.assertIn("value", result)
        self.assertIn("risk", result)

if __name__ == '__main__':
    unittest.main()
