import flet as ft

from ui.styles import AppColors

from .subnav import SubNav
from .topnav import TopNav


class NavBar(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.bgcolor = AppColors.BG_100
        self.padding = ft.Padding.only(left=12, right=12, top=8)
        self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=1, color=AppColors.BG_300)

        # Stack the navbar rows separatly
        self.subnav = SubNav()
        self.topnav = TopNav()
        self.content = ft.Column(controls=[self.topnav, self.subnav], spacing=0)

        self.border = ft.Border(bottom=ft.BorderSide(1, color=AppColors.BG_300))


__all__ = [
    "NavBar",
]
