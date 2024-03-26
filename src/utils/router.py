import flet as ft

from src.components.base_components.scaffold import Scaffold
from src.screens.config import config
from src.screens.home import home
from src.screens.login import login
from src.utils.enums import Routes


class Router:
    def __init__(self, page: ft.Page, fts):
        self.page = page
        self.ft = fts
        self.routes = {
            Routes.HOME.value: home(),
            Routes.LOGIN.value: login(),
            Routes.CONFIG.value: config()
        }
        self.body = Scaffold(page, content=self.routes[Routes.HOME.value])

    def route_change(self, route):
        self.body.content = self.routes[route.data]
        self.page.update()
