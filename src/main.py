import flet as ft

from ui.layouts.main_layout import MainLayout
from ui.styles import AppColors


def main(page: ft.Page) -> None:
    # 1. Window Management: Fill the monitor
    page.window.maximized = True
    page.title = "+Time"

    # 2. Visual Reset: CSS-like normalization
    page.padding = 0
    page.spacing = 0
    page.bgcolor = AppColors.BG_50

    # 3. Theme Configuration: Applying your Indigo palette globally
    page.theme = ft.Theme(
        color_scheme_seed=AppColors.PRIMARY_500,
        visual_density=ft.VisualDensity.COMPACT,
        font_family="Open-Sans",
    )

    # 4. Font Registration (Assuming files are in assets/fonts/)
    page.fonts = {
        "Geist": "fonts/Geist-Regular.ttf",
        "Geist-Bold": "fonts/Geist-Bold.ttf",
        "Geist-SemiBold": "fonts/Geist-SemiBold.ttf",
        "Geist-Medium": "fonts/Geist-Medium.ttf",
        "Geist-Light": "fonts/Geist-Light.ttf",
        "Open-Sans": "fonts/OpenSans-Regular.ttf",
        "Open-Sans-Bold": "fonts/OpenSans-Bold.ttf",
        "Open-Sans-ExtraBold": "fonts/OpenSans-ExtraBold.ttf",
        "Open-Sans-SemiBold": "fonts/OpenSans-SemiBold.ttf",
        "Open-Sans-Medium": "fonts/OpenSans-Medium.ttf",
        "Open-Sans-Light": "fonts/OpenSans-Light.ttf",
    }

    # 5. Root Component
    # We instantiate the MainLayout which contains your
    # Two-Row Navbar and the Content Body.
    app_layout = MainLayout()

    # 6. Final Assembly
    page.add(app_layout)


if __name__ == "__main__":
    # Ensure the assets folder is recognized for fonts/images
    ft.run(main, assets_dir="assets")
