import flet as ft

from ui.styles import AppColors


class TopNav(ft.Row):
    def __init__(self) -> None:
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.spacing = 40

        self.title = Title("Hello World", "Personal")
        self.actions = ft.Row(
            controls=[
                SquaredIconButton("Home", ft.Icons.HOME_FILLED),
                SquaredIconButton("Favorites", ft.Icons.BOOKMARKS_OUTLINED),
                SquaredIconButton("All Projects", ft.Icons.CONTENT_PASTE_SEARCH_ROUNDED),
                SquaredIconButton("Eisenhower Inbox", ft.Icons.MOVE_TO_INBOX_ROUNDED, badge=5),
                SquaredIconButton("Archive", ft.Icons.HISTORY_ROUNDED),
                ft.VerticalDivider(width=1, color=AppColors.BG_500),
                UserLink("P", ft.Colors.PINK),
            ],
            spacing=12,
        )

        self.controls = [
            self.title,
            self.actions,
        ]


class Title(ft.Row):
    def __init__(self, project_name: str, tag_name: str) -> None:
        super().__init__()
        self.spacing = 4

        # We wrap the buttons in a MenuBar to enable the cascading functionality
        self.controls = [
            ft.MenuBar(
                style=ft.MenuStyle(
                    bgcolor=ft.Colors.TRANSPARENT,
                    shadow_color=ft.Colors.TRANSPARENT,
                ),
                controls=[
                    SubMenuTextButton(
                        label=tag_name,
                        color=AppColors.BG_500,
                        options=["Personal", "Work", "College"],
                    ),
                ],
            ),
            ft.Icon(ft.Icons.CHEVRON_RIGHT_ROUNDED, size=16, color=AppColors.BG_300),
            ft.Text(project_name, weight=ft.FontWeight.W_900, size=12, color=AppColors.BG_800, margin=8),
            FavoriteButton(),
        ]


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
