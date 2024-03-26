from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    TextAlign,
    UserControl
)

from flet_core import Control
from src.components.base_components.app_layout import AppLayout
from src.utils.enums import Routes


class Scaffold(UserControl):
    def __init__(
            self,
            page: Page,
            content: Control = None,
    ):
        super().__init__()
        self.page = page
        self.layout = AppLayout(
            self,
            self.page,
            tight=True,
            expand=True,
            vertical_alignment="start",
            content=Container(content=content)
        )
        self.appbar_items = [
            PopupMenuItem(text="Configuração", on_click=lambda _: page.go(Routes.CONFIG.value)),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Sair", on_click=lambda _: page.go(Routes.HOME.value))
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("POE Trello App", size=32, text_align=TextAlign.LEFT),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
