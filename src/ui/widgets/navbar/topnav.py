import flet as ft

from ui.styles import AppColors

from .buttons import FavoriteButton, SquaredIconButton, SubMenuTextButton, UserLink


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
