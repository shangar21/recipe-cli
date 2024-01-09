from textual.app import ComposeResult, RenderResult
from textual.widgets import Footer, Input, TextArea, Select, Button, SelectionList
from textual.containers import Horizontal
from textual.screen import Screen, ModalScreen
from query import models

title = ''
description = ''
ingredients_units = {}

def get_units():
    items = []
    results = models.session.query(models.Unit).all()
    for unit in results:
        items.append((unit.name, unit.id))
    return items

class AddIngredient(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Ingredient", type="text", id='ingredient')
        yield Select(get_units())
        yield Button("Submit", variant='primary')

class AddRecipes(Screen):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'add_ingredient':
            self.app.push_screen(AddIngredient())

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Recipe Title", type="text", id="title")
        yield Input(placeholder="Recipe Description", type="text", id="description")
        yield Button("Add Ingredients", variant="default", id='add_ingredient')
        yield Footer()

