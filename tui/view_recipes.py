from textual.app import ComposeResult, RenderResult
from textual.widgets import Footer, ListItem, ListView, Label, Static, TabbedContent, Markdown
from textual.screen import Screen
from query import models

class RecipeItem(ListItem):
    def __init__(self, recipe):
        super(ListItem, self).__init__(Label(recipe.name))
        self.recipe = recipe

class ViewRecipeInfo(Screen):
    def __init__(self, listitem: RecipeItem):
        super(Screen, self).__init__()
        self.recipe = listitem.recipe

    def compose(self) -> ComposeResult:
        with TabbedContent(self.recipe.name, "Ingredients"):
            yield Markdown(f"# {self.recipe.name} \n ## Recipe Description \n {self.recipe.description} \n ## Recipe Instructions \n {self.recipe.instructions}")
            yield Markdown("")


class ViewRecipes(Screen):
    ALLOW_SELECTOR_MATCH = {'item'}

    def generate_items(self):
        items = []
        results = models.session.query(models.Recipe).all()
        for recipe in results:
            items.append(RecipeItem(recipe))
        return items

    def on_list_view_selected(self, event: ListView.Selected):
        self.app.push_screen(ViewRecipeInfo(event.item))

    def compose(self) -> ComposeResult:
        yield ListView(*self.generate_items())
        yield Footer()

