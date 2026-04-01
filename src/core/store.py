from ui import themes
from ui.styles import ThemePalette


class AppState:
    def __init__(self) -> None:
        self.theme = ThemePalette(themes.LightTheme)


state = AppState()
