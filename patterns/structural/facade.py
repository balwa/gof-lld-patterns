"""FACADE - one simple interface over a complex subsystem.
Use when: home-theater remote, SDK wrappers.  Exercise: add a stop() flow."""
class Projector:  on = lambda self: "projector on"
class Sound:      on = lambda self: "sound on"
class Player:     play = lambda self, m: f"playing {m}"

class HomeTheater:
    def __init__(self): self.p, self.s, self.pl = Projector(), Sound(), Player()
    def watch(self, movie): return [self.p.on(), self.s.on(), self.pl.play(movie)]

def demo():
    out = HomeTheater().watch("Inception"); print(out); assert len(out) == 3

if __name__ == "__main__": demo()
