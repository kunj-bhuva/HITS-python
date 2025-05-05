


from datetime import datetime

class Asset:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Market:
    def __init__(self):
        self.assets = {}

    def update_price(self, symbol, price):
        if symbol not in self.assets:
            self.assets[symbol] = Asset(symbol, price)
        else:
            self.assets[symbol].price = price

    def get_price(self, symbol):
        asset = self.assets.get(symbol)
        return asset.price if asset else None

class Transaction:
    def __init__(self, symbol, quantity, price, type, timestamp=None):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.type = type  # 'buy' or 'sell'
        self.timestamp = timestamp or datetime.now()

class Portfolio:
    def __init__(self, cash=10000):
        self.cash = cash
        self.holdings = {}
        self.transactions = []

    def buy(self, symbol, quantity, market):
        price = market.get_price(symbol)
        if price is None or price * quantity > self.cash or quantity <= 0:
            return False
        self.cash -= price * quantity
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append(Transaction(symbol, quantity, price, 'buy'))
        return True

    def sell(self, symbol, quantity, market):
        if symbol not in self.holdings or self.holdings[symbol] < quantity or quantity <= 0:
            return False
        price = market.get_price(symbol)
        if price is None:
            return False
        self.cash += price * quantity
        self.holdings[symbol] -= quantity
        self.transactions.append(Transaction(symbol, quantity, price, 'sell'))
        return True

    def get_value(self, market):
        total = self.cash
        for symbol, qty in self.holdings.items():
            price = market.get_price(symbol)
            if price:
                total += qty * price
        return total

    def get_position(self, symbol):
        return self.holdings.get(symbol, 0)

    def get_transactions(self, symbol=None, type=None):
        return [t for t in self.transactions if 
                (symbol is None or t.symbol == symbol) and 
                (type is None or t.type == type)]

    def risk_profile(self, market):
        total = self.get_value(market)
        invested = total - self.cash
        if total == 0:
            return "N/A"
        ratio = invested / total
        if ratio > 0.9:
            return "Aggressive"
        elif ratio > 0.6:
            return "Growth"
        elif ratio > 0.3:
            return "Balanced"
        elif ratio > 0:
            return "Conservative"
        else:
            return "Cash"

class Simulator:
    def __init__(self):
        self.market = Market()
        self.portfolio = Portfolio()

    def run_scenario(self):
        self.market.update_price("AAPL", 150)
        self.market.update_price("GOOG", 2700)
        self.portfolio.buy("AAPL", 10, self.market)
        self.market.update_price("AAPL", 155)
        self.portfolio.sell("AAPL", 5, self.market)
        self.market.update_price("GOOG", 2800)
        self.portfolio.buy("GOOG", 2, self.market)
        return {
            "cash": self.portfolio.cash,
            "value": self.portfolio.get_value(self.market),
            "risk": self.portfolio.risk_profile(self.market),
        }

      