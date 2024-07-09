import flet as ft
from src.style.botao import estilo_botao_principal
from src.components.textinput import TextInput
def logar_com_google(e):
    print('Olá mundo')

def logar_com_apple(e):
    print('Olá mundo')



email = TextInput(label='E-mail', hint_text='Digite seu email: ', prefix_icon=ft.icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL)


senha = TextInput(label='Senha', hint_text='Digite seu senha: ', password=True, can_reveal_password=True, prefix_icon=ft.icons.PASSWORD_SHARP, keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD)

botao = ft.ResponsiveRow(
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        ft.ElevatedButton(
            text='Fazer Login',
            col=5,
            style=estilo_botao_principal
        )
    ]
)
def entrar_com(on_click, src: str, text:str):
    return ft.Container(
            bgcolor=ft.colors.GREY_300,
            padding=ft.padding.symmetric(vertical=5, horizontal=10),
            border_radius=10,
            on_click=on_click,
            content=ft.ResponsiveRow(
                spacing=25,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=src, col=2, height=25, width=25),
                    ft.Text(text, color=ft.colors.BLACK, size=16, col=8)
                ]
            )
        )
google = entrar_com(on_click=logar_com_google, src='images/google_logo.png', text='Logar com o Google')
apple = entrar_com(on_click=logar_com_apple, src='images/apple_logo.png', text='Logar com a Apple')



def coluna(page: ft.Page): 
    linha = ft.ResponsiveRow(
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=0,
    run_spacing=0,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[
        ft.Text(value='Crie sua conta com e-mail ',color=ft.colors.BLACK, col=7, text_align=ft.TextAlign.RIGHT),
        ft.TextButton(text='aqui', col=2, on_click=lambda _: page.go('/cadastro') , style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: ft.colors.BLUE,
                ft.MaterialState.HOVERED: ft.colors.BLUE_200
            },
            bgcolor=ft.colors.TRANSPARENT,
            padding=0,
            
        ))
    ]
)
    return ft.Column(
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Text(value='LOGIN', weight=ft.FontWeight.W_900, color=ft.colors.BLACK),
            email,
            senha,
            google,
            apple,
            botao,
            linha
        ]
    )