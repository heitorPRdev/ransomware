# RANSOMWARE

Esse projeto permite você criptografar dados usando uma malware chamado: **RAMSOWARE**.
----
## Como funciona?
Você pode criar um arquivo ou utilizar os arquivos __text1.txt__ ou __text2.txt__, e mudar as informações se for do seu agrado.

### Instalação

    git clone https://github.com/heitorPRdev/ransomware.git
    

### Inicialização
Se for **Windows**
    
    python .\main.py

Se for **Linux**
    
    python3 .\main.py

### Ao Inicializar

Ao inicializar aparecerá uma tela, terá dois botões

#### Cryptografar

Esse botão criará uma nova chave e enviará ao arquivo chave.key (se o arquivo não existir ele criará), depois ele criptografará os dados escritos nos arquivos criados exceto o arquivo __chave.key__,__main.py__ e __README.md__

#### Descryptografar

Esse botão descriptografará os arquivos criptografados com a key criada