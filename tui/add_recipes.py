from textual.app import ComposeResult, RenderResult
from textual.widgets import Footer, Input, TextArea, Select, Button
from textual.containers import Horizontal
from textual.screen import Screen, ModalScreen
from query import models

def get_units():
    items = []
    results = models.session.query(models.Unit).all()
    for unit in results:
        items.append((unit.name, unit.id))
    return items

class AddRecipes(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Recipe Title", type="text")
        yield Input(placeholder="Recipe Description", type="text")
        yield TextArea(language="markdown")
        yield Horizontal (
            Input(placeholder="ingredient", type="text"),
            Select(get_units()),
            Button("Add Ingredient")
        )
        yield Footer()

