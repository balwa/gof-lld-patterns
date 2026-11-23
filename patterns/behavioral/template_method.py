"""TEMPLATE METHOD - fixed algorithm skeleton; subclasses fill in steps.
Use when: frameworks, report generators.  Exercise: add a JSON exporter."""
from abc import ABC, abstractmethod
class Exporter(ABC):
    def export(self, rows):           # the template
        return self.header() + "".join(self.row(r) for r in rows)
    @abstractmethod
    def header(self): ...
    @abstractmethod
    def row(self, r): ...
class CSV(Exporter):
    def header(self): return "id,name\n"
    def row(self, r): return f"{r[0]},{r[1]}\n"
class HTML(Exporter):
    def header(self): return "<table>"
    def row(self, r): return f"<tr><td>{r[0]}</td><td>{r[1]}</td></tr>"

def demo():
    print(CSV().export([(1, "a")])); assert HTML().export([(1, "a")]).startswith("<table>")

if __name__ == "__main__": demo()
