import flet as ft
from src.pages.login.index import Login
from src.pages.cadastro.index import Cadastro

def main(page: ft.Page):
    page.window_resizable = False
    page.window_maximizable = False
    page.window_width = 370
    page.window_height = 750
    page.window_max_width = 370
    def route_change(route):
        troute = ft.TemplateRoute(page.route)
        page.views.clear()
        if troute.match('/') or troute.match('/login'):
            page.views.append(
                ft.View(route='/login', controls=[Login(page=page)], padding=0)
                )
        if troute.match('/cadastro'):
            page.views.append(
                ft.View(route='/cadastro', controls=[Cadastro(page=page)],padding=0)
            )
        page.update()

    page.update()
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, port=8550, host="localhost", assets_dir='assets')
