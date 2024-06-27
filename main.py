import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == 'main.py' or file == 'chave.key':
        continue
    if os.path.isfile(file):
        files.append(file)



while True:
    try:
        escolha = int(input('Escolha uma opção\n[1] Cryptografar\n[2] Descryptografar\n[3] Exit\n>> '))
        if escolha == 1:
            key = Fernet.generate_key()
            with open('chave.key', 'wb') as chave:            
                chave.write(key)
            for file in files:
                
                with open(file,'rb') as arquivo:
                    contents = arquivo.read()
                    
                contents_encryp = Fernet(key).encrypt(contents)
                
                with open(file, 'wb') as arquivo:
                    arquivo.write(contents_encryp)
                    print(f'\nArquivo {file} criptografado com sucesso\n')
        if escolha == 2:
            with open('chave.key','rb') as key:
                secretkey = key.read()
            for file in files:
                with open(file, 'rb') as thefile:
                    content = thefile.read()
                content_decrypt = Fernet(secretkey).decrypt(content)
                with open(file,'wb') as thefile:
                    thefile.write(content_decrypt)
                    print(f'\nArquivo {file} descriptografando com sucesso\n')
        if escolha == 3:
            break
    except ValueError:
        print('\ncoloque uma opção valida\n')