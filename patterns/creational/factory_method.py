"""FACTORY METHOD - subclasses decide which concrete product to create.
Use when: a class can't anticipate the objects it must create.
Exercise: add a Truck-less 'Bike' logistics."""
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str: ...
class Truck(Transport):
    def deliver(self): return "deliver by land"
class Ship(Transport):
    def deliver(self): return "deliver by sea"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport: ...   # the factory method
    def plan(self): return self.create_transport().deliver()
class RoadLogistics(Logistics):
    def create_transport(self): return Truck()
class SeaLogistics(Logistics):
    def create_transport(self): return Ship()

def demo():
    for l in (RoadLogistics(), SeaLogistics()): print(l.plan())
    assert SeaLogistics().plan() == "deliver by sea"

if __name__ == "__main__": demo()
