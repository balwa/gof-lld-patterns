"""BUILDER - construct complex objects step by step.
Use when: many optional params (telescoping constructors).  Exercise: add validation in build()."""
class Pizza:
    def __init__(self, size, toppings, cheese): self.size, self.toppings, self.cheese = size, toppings, cheese
    def __repr__(self): return f"Pizza({self.size}, cheese={self.cheese}, {self.toppings})"

class PizzaBuilder:
    def __init__(self): self._size, self._toppings, self._cheese = "M", [], False
    def size(self, s): self._size = s; return self
    def topping(self, t): self._toppings.append(t); return self
    def extra_cheese(self): self._cheese = True; return self
    def build(self): return Pizza(self._size, self._toppings, self._cheese)

def demo():
    p = PizzaBuilder().size("L").topping("olives").topping("corn").extra_cheese().build()
    print(p); assert p.cheese and len(p.toppings) == 2

if __name__ == "__main__": demo()
