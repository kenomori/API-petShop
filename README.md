# API-petShop
Backend de uma aplicação para petshop, com foco na apredizagem.


## Dependências
Você precisa
- python 3 instalado 
- IDE da sua preferência
- git instalado


## Como construir 

Essas informções são um passo-a-passo educativo, afim de auxiliar novos programadores, 
as informações foram construidas com base no windwos 10.

- Abrir o Git bash na pasta desejada, execute o sequinte programa:


    git clone https://github.com/kenomori/API-petShop.git

Após o comando a uma pasta com os arquivos irá ser baixado para onde o branch foi execultado,
caso tenha dúvidas com o uso do GIT acesse esse [vídeo](https://www.youtube.com/watch?v=kB5e-gTAl_s).
 
- agora vamos instalar o `venv` para receber as libs do projeto, para isso abra o `Terminal`
com `prompt de comando`  na sua IDE:
    

    .\venv\scripts\activate.bat

Caso use o `PowerShell` o comando muda para:

    .\venv\scripts\activate.ps1

Caso fique com duvidas assista esse [vídeo](https://www.youtube.com/watch?v=m1TYpvIYm74).
 

- Com a pasta clonada e o `venv` instalado abra o projeto com sua IDE
- no `Terminal`  digite:


    pip install -r requerimentos.txt 



### o banco de dados

O pojeto do banco de dados é em SQlite, isso facilita a aprendisagem, 
já que requer de menos conhecimentos para o entendimento do funcionamento. 

## Como rodar a aplicação localmente

Com todas as atualizações de requerimento feitas, o programa pode ser execultado 
com um comando no `Terminal` 

    uvicorn main:app --reload


### Testes da API

Com o programa inicializado ele vai gerar o sequinte endereço para acesso: 

http://127.0.0.1:8000/docs

Caso toda a instalação estiver bem sucedida, ao acessar esse endereço ele vai abir o 
`FastAPI` com todas as funções de controle já aplicadas. 
