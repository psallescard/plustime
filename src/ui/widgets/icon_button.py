from typing import Self

import flet as ft

from core.store import state
from ui.styles import Radius, Sizes


class IconBtn(ft.IconButton):
    def __init__(self, label: str, icon: ft.IconData, color: str = state.theme.BG_400) -> None:
        super().__init__()
        self.color = color
        self.icon_color = color
        self.icon = icon
        self.tooltip = label
        self.icon_size = Sizes.ICON_SM
        self.width = Sizes.BTN_MD
        self.height = Sizes.BTN_MD
        self.padding = 0
        self.callback_func = None
        self.on_click = self._on_click_internal_handler

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=Radius.RADIUS_XS),
            padding=ft.Padding.all(0),
            shadow_color=ft.Colors.TRANSPARENT,
            mouse_cursor=ft.MouseCursor.CLICK,
        )

    def _on_click_internal_handler(self, e) -> None:  # noqa: ANN001
        """Handles callback functions and state changes, on click."""
        if hasattr(self, "selected_icon") and self.selected_icon:
            self.selected = not self.selected

        # If the button has business logic, run it
        if self.callback_func:
            self.callback_func(e)

        self.update()

    def with_border(self, width: float = Sizes.BORDER_XS, color: str = state.theme.BG_400) -> Self:
        self.style.side = ft.BorderSide(width, color)
        return self

    def with_callback(self, func: callable) -> Self:
        """Sets the actual business logic (e.g., save to DB)."""
        self.callback_func = func
        return self

    def with_bgcolor(self, color: str, hover_color: str | None = None) -> Self:
        self.bgcolor = color
        if hover_color:
            self.hover_color = hover_color
        return self

    def with_size(self, size: int = Sizes.BTN_MD, icon_size: int = Sizes.ICON_SM) -> Self:
        self.width = size
        self.height = size
        self.icon_size = icon_size
        return self

    def with_radius(self, radius: int = Radius.RADIUS_XS) -> Self:
        self.style.shape = ft.RoundedRectangleBorder(radius=radius)
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
            bgcolor=state.theme.PRIMARY_500,
            text_style=ft.TextStyle(
                decoration=None,
                color=state.theme.BG_50,
                size=Sizes.TEXT_XS,
            ),
        )
        return self
