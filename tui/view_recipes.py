from textual.app import ComposeResult, RenderResult
from textual.widgets import Footer, ListItem, ListView, Label, Static
from textual.screen import Screen
from query import models

class RecipeItem(ListItem):
    def __init__(self, recipe):
        super(ListItem, self).__init__(Label(recipe.name))
        self.recipe = recipe

class ViewRecipeInfo(Screen):
    def __init__(self, listitem):
        super(Screen, self).__init__()
        self.recipe = listitem.recipe

    def render(self) -> RenderResult:
        return f"Recipe Name: {self.recipe.name} \nRecipe Description: {self.recipe.description} \nRecipe Instructions: {self.recipe.instructions}"

class ViewRecipes(Screen):
    def generate_items(self):
        items = []
        results = models.session.query(models.Recipe).all()
        for recipe in results:
            items.append(RecipeItem(recipe))
        return items

    def action_select_cursor(self):
        self.push_screen(ViewRecipeInfo(ListView.Selected.item))

    def compose(self) -> ComposeResult:
        yield ListView(*self.generate_items())
        yield Footer()

