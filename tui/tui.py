from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import ScrollableContainer
from tui import bindings, modes

class RecipeCLI(App):
    BINDINGS = bindings.MAIN_MENU_BINDINGS
    MODES = modes.MODES
    debug = True

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

