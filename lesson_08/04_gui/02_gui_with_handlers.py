import flet as ft


def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = "light"  # dark
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    info_label = ft.Text("Information")
    info_text_field = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)

    def update_label(event):
        info_label.value = info_text_field.value
        page.update()  # try without update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.HOME),
                ft.Icon(ft.icons.BACK_HAND),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                info_label,
                info_text_field
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="UPDATE LABEL", on_click=update_label),
                ft.Checkbox(label="Agree with conditions", value=True)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
