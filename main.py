import flet as ft

from flet import Page
from flet_core import colors
from src.utils.router import Router
from src.components.base_components.app_bar import app_bar

if __name__ == "__main__":
    def main(page: Page):
        my_router = Router(page, ft)
        page.title = "POE Trello App"
        page.padding = 0
        page.appbar = app_bar(page)
        page.bgcolor = colors.BLUE_GREY_200
        page.theme_mode = "dark"
        page.on_route_change = my_router.route_change
        page.add(my_router.body)
        page.go('/')


    ft.app(target=main)
