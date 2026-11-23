"""MEDIATOR - objects talk via a central mediator, not to each other.
Use when: chat rooms, air traffic control.  Exercise: add private messages."""
class ChatRoom:
    def __init__(self): self.users = []
    def send(self, sender, msg):
        for u in self.users:
            if u is not sender: u.inbox.append(f"{sender.name}: {msg}")
class User:
    def __init__(self, name, room): self.name, self.room, self.inbox = name, room, []; room.users.append(self)
    def say(self, m): self.room.send(self, m)

def demo():
    r = ChatRoom(); a, b = User("A", r), User("B", r); a.say("hi"); print(b.inbox)
    assert b.inbox == ["A: hi"] and a.inbox == []

if __name__ == "__main__": demo()
