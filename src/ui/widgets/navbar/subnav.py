from __future__ import annotations

import flet as ft

from .buttons import BottomLineTextButton


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
