from __future__ import annotations

import flet as ft

from ui.styles import AppColors


class SubNav(ft.Row):
    def __init__(self) -> None:
        super().__init__()
        self.spacing = 20
        self.alignment = ft.MainAxisAlignment.START

        self.tabs = [
            BottomLineTextButton("Kanban", ft.Icons.VIEW_KANBAN_OUTLINED, self.handle_click),
            BottomLineTextButton("Tasks", ft.Icons.CHECKLIST_ROUNDED, self.handle_click),
            BottomLineTextButton("Configuration", ft.Icons.SETTINGS_OUTLINED, self.handle_click),
        ]

        # Activate the first tab for default view
        self.tabs[0].activate()

        self.controls = [
            *self.tabs,
        ]

    def handle_click(self, clicked_tab: BottomLineTextButton) -> None:
        for tab in self.tabs:
            if tab is clicked_tab:
                tab.activate()
            else:
                tab.deactivate()
            tab.update()


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
            bottom=(
                ft.BorderSide(
                    width=2,
                    color=AppColors.PRIMARY_500,
                    stroke_align=ft.BorderSideStrokeAlign.OUTSIDE,
                )
            ),
        )
        self.text.color = self.active_color
        self.component.content.icon_color = self.active_color

    def deactivate(self) -> None:
        self.component.border = None
        self.text.color = self.inactive_color
        self.component.content.icon_color = self.inactive_color
