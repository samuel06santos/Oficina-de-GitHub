from flet import *

def main(page=Page):
    page.title = "Oficina de GitHub"
    page.theme_mode = "dark"
    page.window_height = 500
    page.window_width = 580
    page.window_maximizable = False
    page.window_resizable = False
    page.window_center()

    page.add(

        Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                Text("Oficina de GitHub", size=32),
                Image(src=r"LabSC.png", width=200),
                Text("LabSC", size=48),
                Text("Laboratório de Segurança e Criptografia aplicada.", size=24)
            ]
        )
    )

app(target=main, assets_dir=r".images")