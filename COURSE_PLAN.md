# Suggested teaching plan (4 sessions x ~60 min)

Each pattern: (1) show the *problem* with naive if/else code, (2) live-code the pattern, (3) students do the
"Exercise" line at the top of the file, (4) 2 discussion questions: *what changes if a new variant is added? what is the cost of this pattern?*

| Session | Patterns | Case study to draw on the board |
|---|---|---|
| 1 Creational | Singleton, Factory Method, Abstract Factory, Builder, Prototype | Notification service, UI theme kit |
| 2 Structural | Adapter, Facade, Decorator, Composite, Proxy, Bridge, Flyweight | Coffee shop, file explorer |
| 3 Behavioral I | Strategy, Observer, Command, State, Template Method | Payment checkout, vending machine, text editor |
| 4 Behavioral II + LLD | Iterator, Chain, Mediator, Memento, Visitor, Interpreter + mini LLD (Parking Lot / Elevator) | Combine 3+ patterns |

Common confusions to address: Strategy vs State (who changes the behavior?), Factory Method vs Abstract Factory
(one product vs a family), Decorator vs Proxy (add behavior vs control access), Adapter vs Facade (convert vs simplify).
Anti-pattern warning: don't force patterns; Singleton is often a global in disguise.
