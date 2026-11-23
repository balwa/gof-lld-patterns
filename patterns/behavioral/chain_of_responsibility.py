"""CHAIN OF RESPONSIBILITY - pass a request along handlers until one handles it.
Use when: ATM cash dispensing, middleware, support escalation.  Exercise: add a Director level."""
class Handler:
    def __init__(self, nxt=None): self.nxt = nxt
    def handle(self, amt):
        if self.can(amt): return f"{self.__class__.__name__} approved {amt}"
        if self.nxt: return self.nxt.handle(amt)
        return "rejected"
class Manager(Handler):
    def can(self, a): return a <= 1000
class VP(Handler):
    def can(self, a): return a <= 10000

def demo():
    chain = Manager(VP())
    print(chain.handle(500), "|", chain.handle(5000), "|", chain.handle(99999))
    assert chain.handle(5000).startswith("VP")

if __name__ == "__main__": demo()
