"""INTERPRETER - represent a grammar as classes and evaluate sentences.
Use when: expression evaluators, rule engines.  Exercise: add a Multiply node."""
class Num:
    def __init__(self, v): self.v = v
    def eval(self): return self.v
class Add:
    def __init__(self, l, r): self.l, self.r = l, r
    def eval(self): return self.l.eval() + self.r.eval()
class Sub:
    def __init__(self, l, r): self.l, self.r = l, r
    def eval(self): return self.l.eval() - self.r.eval()

def demo():
    e = Sub(Add(Num(5), Num(3)), Num(2)); print(e.eval()); assert e.eval() == 6

if __name__ == "__main__": demo()
