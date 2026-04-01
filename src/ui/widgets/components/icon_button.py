from typing import Self

import flet as ft

from ui.styles import AppColors


class IconBtn(ft.IconButton):
    def __init__(self, label: str, icon: ft.IconData, color: str = AppColors.BG_400) -> None:
        super().__init__()
        self.color = color
        self.icon_color = color
        self.icon = icon
        self.tooltip = label
        self.icon_size = 16
        self.width = 28
        self.height = 28
        self.padding = 0
        self.callback_func = None
        self.on_click = self._on_click_internal_handler

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            shadow_color=ft.Colors.TRANSPARENT,
        )

    def _on_click_internal_handler(self, e) -> None:  # noqa: ANN001
        """Handles callback functions and state changes, on click."""
        if hasattr(self, "selected_icon") and self.selected_icon:
            self.selected = not self.selected

        # If the button has business logic, run it
        if self.callback_func:
            self.callback_func(e)

        self.update()

    def with_border(self, color: str = AppColors.BG_400) -> Self:
        self.style.side = ft.BorderSide(0.5, color)
        return self

    def with_callback(self, func: callable) -> Self:
        """Sets the actual business logic (e.g., save to DB)."""
        self.callback_func = func
        return self

    def with_bgcolor(self, color: str) -> Self:
        self.bgcolor = color
        return self

    def with_size(self, size: int, icon_size: int = 16) -> Self:
        self.width = size
        self.height = size
        self.icon_size = icon_size
        return self

    def with_active_state(self, active_icon: ft.IconData, is_selected: bool = False) -> Self:
        """Set a selected state for the button."""
        self.selected = is_selected
        self.selected_icon = active_icon
        self.selected_icon_color = self.color

        return self

    def with_badge(self, value: int = 0) -> Self:
        self.badge = ft.Badge(
            label=str(value),
            bgcolor=AppColors.PRIMARY_500,
            text_style=ft.TextStyle(
                decoration=None,
                color=AppColors.BG_50,
                size=10,
            ),
        )
        return self
