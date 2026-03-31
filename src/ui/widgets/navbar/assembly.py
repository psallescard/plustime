import flet as ft

from ui.styles import AppColors

from .subnav import SubNav
from .topnav import TopNav


class NavBar(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.bgcolor = AppColors.BG_100
        self.padding = ft.Padding.only(left=8, right=8, top=8)

        # Stack the navbar rows separatly
        self.content = ft.Column(controls=[TopNav(), SubNav()], spacing=0)

        self.border = ft.Border(bottom=ft.BorderSide(1, color=AppColors.BG_300))
