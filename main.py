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
    def cryptografando(e):
        key = Fernet.generate_key()
        with open('chave.key', 'wb') as chave:            
            chave.write(key)
            for file in files:
                    
                with open(file,'rb') as arquivo:
                    contents = arquivo.read()
                            
                contents_encryp = Fernet(key).encrypt(contents)
                        
                with open(file, 'wb') as arquivo:
                    arquivo.write(contents_encryp)
    def descryptografando(e):
        with open('chave.key','rb') as key:
            secretkey = key.read()
        for file in files:
            with open(file, 'rb') as thefile:
                content = thefile.read()
            content_decrypt = Fernet(secretkey).decrypt(content)
            with open(file,'wb') as thefile:
                thefile.write(content_decrypt)

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