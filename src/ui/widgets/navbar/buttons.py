import flet as ft

from ui.styles import AppColors


class BottomLineTextButton(ft.Column):
    def __init__(self, text: str, icon: ft.IconData, on_change: callable) -> None:
        super().__init__()
        self.on_change = on_change
        self.active_color = AppColors.BG_800
        self.inactive_color = AppColors.BG_500
        self.text = ft.Text(text, size=12, color=self.inactive_color)

        self.component = ft.Container(
            content=ft.TextButton(
                content=self.text,
                icon=icon,
                icon_color=self.inactive_color,
                style=ft.ButtonStyle(
                    padding=ft.Padding.only(bottom=20, top=16, left=12, right=12),
                    shape=ft.RoundedRectangleBorder(radius=5),
                ),
                on_click=self._on_click_handler,
            ),
            border=None,
        )

        self.controls = [
            self.component,
        ]

    def _on_click_handler(self, e) -> None:  # noqa: ANN001, ARG002
        """Pass the event to the father component to ensure all other tabs are deactivated."""
        if self.on_change:
            self.on_change(self)

    def activate(self) -> None:
        self.component.border = ft.Border.only(
            # Use BorderSideStrokeAllign.OUTSIDE to prevent layout shift on activation/deactivation
            bottom=(ft.BorderSide(width=2, color=AppColors.PRIMARY_500, stroke_align=ft.BorderSideStrokeAlign.OUTSIDE)),
        )
        self.text.color = self.active_color
        self.component.content.icon_color = self.active_color
        self.text.weight = ft.FontWeight.W_600

    def deactivate(self) -> None:
        self.component.border = None
        self.text.color = self.inactive_color
        self.component.content.icon_color = self.inactive_color
        self.text.weight = ft.FontWeight.NORMAL


class SubMenuTextButton(ft.SubmenuButton):
    def __init__(self, label: str, options: list[str], color: str) -> None:
        super().__init__()

        self.content = ft.Text(label, size=12, color=color)

        self.style = ft.ButtonStyle(
            padding=ft.Padding.symmetric(horizontal=8),
            shape=ft.RoundedRectangleBorder(radius=4),
        )

        self.controls = [
            ft.MenuItemButton(
                content=ft.Text(option, size=12),
                on_click=lambda e: print(f"Selected: {e.control.content.value}"),
            )
            for option in options
        ]


class UserLink(ft.Container):
    def __init__(self, text: str, color: str) -> None:
        super().__init__()
        self.content = ft.Text(text, size=12, color=AppColors.BG_50, weight=ft.FontWeight.W_600)
        self.bgcolor = color
        self.border_radius = 50
        self.width = 28
        self.height = 28
        self.alignment = ft.Alignment.CENTER


class FavoriteButton(ft.IconButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon = ft.Icons.BOOKMARK_ADD_OUTLINED
        self.selected_icon = ft.Icons.BOOKMARK_ADDED
        self.selected_icon_color = ft.Colors.AMBER_500
        self.icon_color = ft.Colors.AMBER_500
        self.tooltip = "Add to Favorites"
        self.icon_size = 16
        self.on_click = self._on_click_handler

    def _on_click_handler(self, e) -> None:  # noqa: ARG002, ANN001
        self.selected = not self.selected
        self.update()


class SquaredIconButton(ft.IconButton):
    def __init__(self, label: str, icon: ft.IconData, badge: int = 0) -> None:
        super().__init__()
        self.icon_color = ft.Colors.GREY_500
        self.icon = icon
        self.tooltip = label
        self.icon_size = 16
        self.width = 28
        self.height = 28
        self.padding = 0
        if badge:
            self.badge = ft.Badge(
                label=str(badge),
                bgcolor=AppColors.PRIMARY_500,
                text_style=ft.TextStyle(
                    decoration=None,
                    color=AppColors.BG_50,
                    size=10,
                ),
            )

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            shadow_color=ft.Colors.TRANSPARENT,
            side=ft.BorderSide(0.5, ft.Colors.GREY_400),
        )
