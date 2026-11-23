"""ABSTRACT FACTORY - create families of related objects without naming concrete classes.
Use when: UI themes, cross-platform widgets.  Exercise: add a 'Mac' family."""
class WinButton:  render = lambda self: "[Win button]"
class WinCheck:   render = lambda self: "[Win checkbox]"
class WebButton:  render = lambda self: "<button>"
class WebCheck:   render = lambda self: "<input type=checkbox>"

class WinFactory:
    def button(self): return WinButton()
    def checkbox(self): return WinCheck()
class WebFactory:
    def button(self): return WebButton()
    def checkbox(self): return WebCheck()

def build_ui(f):  # client only knows the factory interface
    return [f.button().render(), f.checkbox().render()]

def demo():
    print(build_ui(WinFactory()), build_ui(WebFactory()))
    assert build_ui(WebFactory())[0] == "<button>"

if __name__ == "__main__": demo()
