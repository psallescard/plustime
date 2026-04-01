from ui.themes import ThemeObject


class ThemePalette:
    def __init__(self, theme: ThemeObject) -> None:
        self.PRIMARY_100 = "#E8EAF6"
        self.PRIMARY_300 = "#7986CB"
        self.PRIMARY_500 = "#3F51B5"
        self.PRIMARY_800 = "#283593"
        self.update_theme(theme)

    def update_theme(self, theme: ThemeObject) -> None:
        self.BG_50 = theme.BG_50
        self.BG_100 = theme.BG_100
        self.BG_300 = theme.BG_300
        self.BG_400 = theme.BG_400
        self.BG_500 = theme.BG_500
        self.BG_600 = theme.BG_600
        self.BG_800 = theme.BG_800
        self.BG_900 = theme.BG_900


class Sizes:
    BTN_XS = 20
    BTN_SM = 24
    BTN_MD = 28
    BTN_LG = 36
    BTN_XL = 44

    ICON_XS = 12
    ICON_SM = 16
    ICON_MD = 20
    ICON_LG = 24
    ICON_XL = 28

    BORDER_XS = 0.5
    BORDER_SM = 1
    BORDER_MD = 2
    BORDER_LG = 4

    TEXT_XS = 10
    TEXT_SM = 12
    TEXT_MD = 14
    TEXT_LG = 16
    TEXT_XL = 18
    TEXT_XXL = 20


class Radius:
    RADIUS_XS = 5
    RADIUS_SM = 8
    RADIUS_MD = 12
    RADIUS_LG = 16
    RADIUS_XL = 24
    RADIUS_FULL = 500


class Spacing:
    pass
