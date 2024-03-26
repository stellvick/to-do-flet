from flet_core import AppBar, Icon, icons, Text, TextAlign, Container, PopupMenuButton, margin, colors, PopupMenuItem

from src.utils.enums import Routes


def app_bar(page):
    return AppBar(
        leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
        leading_width=100,
        title=Text("POE Trello App", size=32, text_align=TextAlign.LEFT),
        center_title=True,
        toolbar_height=75,
        bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        actions=[
            Container(
                content=PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Configuração", on_click=lambda _: page.go(Routes.CONFIG.value)),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(text="Sair", on_click=lambda _: page.go(Routes.HOME.value))
                    ]
                ),
                margin=margin.only(left=50, right=25)
            )
        ],
    )
