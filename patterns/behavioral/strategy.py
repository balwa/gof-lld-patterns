"""STRATEGY - interchangeable algorithms behind one interface, chosen at runtime.
Use when: payment methods, sorting, pricing.  Exercise: add a UPI strategy."""
from typing import Protocol
class Payment(Protocol):
    def pay(self, amt: int) -> str: ...
class Card:
    def pay(self, amt): return f"card paid {amt}"
class Wallet:
    def pay(self, amt): return f"wallet paid {amt}"
class Cart:
    def __init__(self, strategy: Payment): self.strategy = strategy
    def checkout(self, amt): return self.strategy.pay(amt)

def demo():
    c = Cart(Card()); print(c.checkout(100)); c.strategy = Wallet(); print(c.checkout(100))
    assert c.checkout(1) == "wallet paid 1"

if __name__ == "__main__": demo()
