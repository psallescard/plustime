from __future__ import annotations

import flet as ft

from ui.styles import AppColors
from ui.widgets.components import IconBtn


class NavBar(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.bgcolor = AppColors.BG_100
        self.padding = ft.Padding.only(left=12, right=12, top=8)
        self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=1, color=AppColors.BG_300)

        # Stack the navbar rows separatly
        self.subnav = SubNav()
        self.topnav = TopNav()
        self.content = ft.Column(controls=[self.topnav, self.subnav], spacing=3)

        self.border = ft.Border(bottom=ft.BorderSide(1, color=AppColors.BG_300))


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
                IconBtn("All Projects", ft.Icons.CONTENT_PASTE_SEARCH_ROUNDED)
                    .with_border(),
                IconBtn("Eisenhower Inbox", ft.Icons.MOVE_TO_INBOX_ROUNDED)
                    .with_border()
                    .with_badge(5),
                IconBtn("Archive", ft.Icons.HISTORY_ROUNDED)
                    .with_border(),
                ft.VerticalDivider(width=1, color=AppColors.BG_500),
                IconBtn("User Settings", ft.Icons.PERSON_ROUNDED, color=AppColors.BG_50)
                    .with_size(icon_size=20)
                    .with_bgcolor(AppColors.BG_800, hover_color=AppColors.BG_600)
                    .with_border(color=AppColors.BG_800)
                    .with_radius(50),
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

        self.menu_bar = ft.MenuBar(
            style=ft.MenuStyle(bgcolor=ft.Colors.TRANSPARENT, shadow_color=ft.Colors.TRANSPARENT),
            controls=[
                SubMenuTextButton(
                    label=tag_name,
                    color=AppColors.BG_500,
                    options=[
                        SubMenuOption("Personal", ft.Icons.PERSON_OUTLINED),
                        SubMenuOption("College", ft.Icons.SCHOOL_OUTLINED),
                        SubMenuOption("Work", ft.Icons.WORK_OUTLINED),
                    ],
                ),
            ],
        )
        # fmt: off
        self.actions = ft.Row(
                controls=[
                    IconBtn("Menu", ft.Icons.MENU_ROUNDED)
                        .with_border(),
                    IconBtn("Home", ft.Icons.HOME_FILLED, color=AppColors.BG_50)
                        .with_bgcolor(AppColors.BG_800, hover_color=AppColors.BG_600)
                        .with_border(),
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # fmt: off
        self.controls = [
            self.actions,
            ft.VerticalDivider(width=1, color=AppColors.BG_500),
            self.menu_bar,
            ft.Icon(ft.Icons.CHEVRON_RIGHT_ROUNDED, size=16, color=AppColors.BG_300),
            ft.Text(project_name, size=12, color=AppColors.BG_800, margin=8, font_family="Open-Sans-Bold"),
            IconBtn("Add to Favorites", ft.Icons.BOOKMARK_ADD_OUTLINED, ft.Colors.AMBER_500)
                .with_active_state(ft.Icons.BOOKMARK_ADDED),
        ]


class SubMenuOption(ft.MenuItemButton):
    def __init__(self, label: str, icon: ft.IconData) -> None:
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(icon, color=AppColors.PRIMARY_500, size=16),
                ft.Text(label, size=12),
            ],
            alignment=ft.MainAxisAlignment.START,
            margin=ft.Margin(right=32),
        )
        self.on_click = lambda e: print(f"Selected: {e.control.content.value}")  # noqa: T201


class SubMenuTextButton(ft.SubmenuButton):
    def __init__(self, label: str, options: list[SubMenuOption], color: str) -> None:
        super().__init__()

        self.content = ft.Text(label, size=12, color=color)

        self.style = ft.ButtonStyle(
            padding=ft.Padding.symmetric(horizontal=8),
            shape=ft.RoundedRectangleBorder(radius=4),
        )

        self.controls = options


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
