from __future__ import annotations

import flet as ft

from ui.styles import Colors, Radius, Sizes
from ui.widgets import IconBtn


class NavBar(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.bgcolor = Colors.BG_100
        self.padding = ft.Padding.only(left=12, right=12, top=8)
        self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=1, color=Colors.BG_300)

        # Stack the navbar rows separatly
        self.subnav = SubNav()
        self.topnav = TopNav()
        self.content = ft.Column(controls=[self.topnav, self.subnav], spacing=3)

        self.border = ft.Border(bottom=ft.BorderSide(Sizes.BORDER_SM, color=Colors.BG_300))


class TopNav(ft.Row):
    def __init__(self) -> None:
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.spacing = 40

        self.title = Title("Hello World", "Personal")

        # fmt: off
        self.actions = ft.Row(
            controls=[
                IconBtn("Favorites", ft.Icons.BOOKMARKS_OUTLINED)
                    .with_border(),
                IconBtn("All Projects", ft.Icons.SPACE_DASHBOARD_OUTLINED)
                    .with_border(),
                IconBtn("Eisenhower Inbox", ft.Icons.MOVE_TO_INBOX_ROUNDED)
                    .with_border()
                    .with_badge(5),
                IconBtn("Archive", ft.Icons.HISTORY_ROUNDED)
                    .with_border(),
                ft.VerticalDivider(width=1, color=Colors.BG_500),
                IconBtn("User Settings", ft.Icons.PERSON_ROUNDED, color=Colors.BG_50)
                    .with_size(icon_size=Sizes.ICON_MD)
                    .with_bgcolor(Colors.BG_800, hover_color=Colors.BG_600)
                    .with_border(color=Colors.BG_800)
                    .with_radius(Radius.RADIUS_FULL),
            ],
            spacing=12,
        )

        self.controls = [
            self.title,
            self.actions,
        ]


class SubNav(ft.Row):
    def __init__(self) -> None:
        super().__init__()
        self.spacing = 20
        self.alignment = ft.MainAxisAlignment.START

        self.tabs = [
            BottomLineTextButton("Kanban", ft.Icons.VIEW_KANBAN_OUTLINED, self.handle_click),
            BottomLineTextButton("Tasks", ft.Icons.CHECKLIST_ROUNDED, self.handle_click),
            BottomLineTextButton("Calendar", ft.Icons.CALENDAR_MONTH_OUTLINED, self.handle_click),
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


class Title(ft.Row):
    def __init__(self, project_name: str, tag_name: str) -> None:
        super().__init__()
        self.spacing = 5
        self.margin = ft.Margin(left=8, right=8)
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        # fmt: off
        self.actions = ft.Row(
                controls=[
                    IconBtn("Menu", ft.Icons.MENU_ROUNDED)
                        .with_border(),
                    IconBtn("Home", ft.Icons.HOME_FILLED, color=Colors.BG_50)
                        .with_bgcolor(Colors.BG_800, hover_color=Colors.BG_600)
                        .with_border(),
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # fmt: off
        self.controls = [
            self.actions,
            ft.VerticalDivider(width=1, color=Colors.BG_500),
            ft.Text(tag_name, size=Sizes.TEXT_SM, color=Colors.BG_500, margin=8),
            ft.Icon(ft.Icons.CHEVRON_RIGHT_ROUNDED, size=Sizes.ICON_SM, color=Colors.BG_300),
            ft.Text(project_name, size=Sizes.TEXT_SM, color=Colors.BG_800, margin=8, font_family="Open-Sans-Bold"),
            IconBtn("Add to Favorites", ft.Icons.BOOKMARK_ADD_OUTLINED, ft.Colors.AMBER_500)
                .with_active_state(ft.Icons.BOOKMARK_ADDED),
        ]


class BottomLineTextButton(ft.Column):
    def __init__(self, text: str, icon: ft.IconData, on_change: callable) -> None:
        super().__init__()
        self.on_change = on_change
        self.active_color = Colors.BG_800
        self.inactive_color = Colors.BG_500
        self.text = ft.Text(text, size=Sizes.TEXT_SM, color=self.inactive_color)

        self.component = ft.Container(
            content=ft.TextButton(
                content=self.text,
                icon=icon,
                icon_color=self.inactive_color,
                style=ft.ButtonStyle(
                    padding=ft.Padding.only(bottom=20, top=16, left=12, right=12),
                    shape=ft.RoundedRectangleBorder(radius=Radius.RADIUS_XS),
                    mouse_cursor=ft.MouseCursor.CLICK,
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
                    width=Sizes.BORDER_MD,
                    color=Colors.PRIMARY_500,
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
