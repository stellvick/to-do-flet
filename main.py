import flet
from flet import (
    Page,
    colors
)

from src.components.scaffold import TrelloApp

if __name__ == "__main__":
    def main(page: Page):
        page.title = "POE Trello App"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        page.update()
        app.build()
        app.initialize()


    flet.app(target=main, view=flet.WEB_BROWSER)
