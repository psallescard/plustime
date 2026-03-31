import flet as ft

from ui.widgets import NavBar


class MainLayout(ft.Column):
    def __init__(self) -> None:
        super().__init__()
        self.expand = True
        self.spacing = 0

        # Main screen components
        self.navbar = NavBar()
        self.view = ft.Container()

        # Assembling
        self.controls = [
            self.navbar,
            self.view,
        ]
