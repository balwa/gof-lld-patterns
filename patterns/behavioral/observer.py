"""OBSERVER - subscribers get notified when a subject changes (pub/sub).
Use when: events, stock tickers, UI.  Exercise: add unsubscribe + a second observer type."""
class Stock:
    def __init__(self): self._subs, self.price = [], 0
    def subscribe(self, fn): self._subs.append(fn)
    def set_price(self, p):
        self.price = p
        for fn in self._subs: fn(p)

def demo():
    log = []; s = Stock()
    s.subscribe(lambda p: log.append(f"A saw {p}")); s.subscribe(lambda p: log.append(f"B saw {p}"))
    s.set_price(101); print(log); assert len(log) == 2

if __name__ == "__main__": demo()
