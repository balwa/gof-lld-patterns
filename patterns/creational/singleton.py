"""SINGLETON - ensure a class has exactly one instance with a global access point.
Use when: config, logger, connection pool.  Caveat: hidden global state; hard to test.
Exercise: make it thread-safe (hint: lock / module-level instance)."""
class Config:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

def demo():
    a, b = Config(), Config()
    a.settings["theme"] = "dark"
    print(b.settings, a is b)
    assert a is b and b.settings["theme"] == "dark"

if __name__ == "__main__": demo()
