import unittest
from c import Asset, Market, Transaction, Portfolio, Simulator
class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.market = Market()
        self.portfolio = Portfolio()

    def test_buy_success(self):
        self.market.update_price("AAPL", 150)
        self.assertTrue(self.portfolio.buy("AAPL", 5, self.market))
        self.assertEqual(self.portfolio.cash, 9250)
        self.assertEqual(self.portfolio.holdings["AAPL"], 5)

    def test_buy_insufficient_cash(self):
        self.market.update_price("AAPL", 150)
        self.assertFalse(self.portfolio.buy("AAPL", 100, self.market))
        self.assertEqual(self.portfolio.cash, 10000)
        self.assertNotIn("AAPL", self.portfolio.holdings)

    def test_buy_invalid_quantity(self):
        self.market.update_price("AAPL", 150)
        self.assertFalse(self.portfolio.buy("AAPL", -5, self.market))
        self.assertEqual(self.portfolio.cash, 10000)
        self.assertNotIn("AAPL", self.portfolio.holdings)

    def test_sell_success(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.assertTrue(self.portfolio.sell("AAPL", 3, self.market))
        self.assertEqual(self.portfolio.cash, 9700)
        self.assertEqual(self.portfolio.holdings["AAPL"], 2)

    def test_sell_insufficient_quantity(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.assertFalse(self.portfolio.sell("AAPL", 10, self.market))
        self.assertEqual(self.portfolio.cash, 8500)
        self.assertEqual(self.portfolio.holdings["AAPL"], 5)

    def test_sell_invalid_quantity(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.assertFalse(self.portfolio.sell("AAPL", -3, self.market))
        self.assertEqual(self.portfolio.cash, 8500)
        self.assertEqual(self.portfolio.holdings["AAPL"], 5)

    def test_get_value(self):
        self.market.update_price("AAPL", 150)
        self.market.update_price("GOOG", 2700)
        self.portfolio.buy("AAPL", 5, self.market)
        self.portfolio.buy("GOOG", 2, self.market)
        self.assertEqual(self.portfolio.get_value(self.market), 15300)

    def test_get_position(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.assertEqual(self.portfolio.get_position("AAPL"), 5)

    def test_get_transactions(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.portfolio.sell("AAPL", 3, self.market)
        self.assertEqual(len(self.portfolio.get_transactions("AAPL", "buy")), 1)
        self.assertEqual(len(self.portfolio.get_transactions("AAPL", "sell")), 1)

    def test_risk_profile(self):
        self.market.update_price("AAPL", 150)
        self.portfolio.buy("AAPL", 5, self.market)
        self.assertEqual(self.portfolio.risk_profile(self.market), "Growth")

if __name__ == '__main__':
    unittest.main()