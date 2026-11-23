"""ADAPTER - make an incompatible interface fit the one clients expect.
Use when: wrapping legacy/3rd-party code.  Exercise: adapt a CelsiusSensor too."""
class FahrenheitSensor:
    def read_f(self): return 98.6

class TempSensor:  # target interface: read() -> Celsius
    def read(self): raise NotImplementedError

class FahrenheitAdapter(TempSensor):
    def __init__(self, s): self.s = s
    def read(self): return round((self.s.read_f() - 32) * 5 / 9, 1)

def demo():
    t = FahrenheitAdapter(FahrenheitSensor()).read(); print(t); assert t == 37.0

if __name__ == "__main__": demo()
