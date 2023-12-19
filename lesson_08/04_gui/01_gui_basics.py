import flet as ft


def main(page: ft.Page):
    text_control = ft.Text(value="Hi There!", color='red', size=20)

    # page.controls.append(text_control)
    # page.update()

    # page.add(t)  it's a shortcut for page.controls.append(t) and then page.update()
    page.add(text_control)


ft.app(target=main)
