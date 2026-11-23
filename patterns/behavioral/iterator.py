"""ITERATOR - traverse a collection without exposing its structure.
Use when: custom collections, trees.  Exercise: add a reverse iterator."""
class Playlist:
    def __init__(self, *songs): self.songs = list(songs)
    def __iter__(self):
        i = 0
        while i < len(self.songs): yield self.songs[i]; i += 1

def demo():
    out = list(Playlist("a", "b", "c")); print(out); assert out == ["a", "b", "c"]

if __name__ == "__main__": demo()
