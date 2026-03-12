# Crypto Price App - Versão Web

## Descrição
O **Crypto Price App** é uma aplicação web desenvolvida em Python usando **Flask** que permite consultar o preço de criptomoedas em **USD** e **BRL** em tempo real, utilizando a API da [CoinGecko](https://www.coingecko.com/).  

O usuário digita o nome da criptomoeda (como `bitcoin` ou `ethereum`) e a aplicação retorna os preços correspondentes. Se a moeda não existir, uma mensagem de erro é exibida.

---

## Funcionalidades

- Consulta de preço em **USD** e **BRL**.  
- Mensagem de aviso quando a moeda não é encontrada.  
- Interface simples e intuitiva, responsiva para web.  
- Estilização básica com CSS para melhor experiência do usuário.  

---

## Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **Requests**
- **HTML/CSS**

---

## Estrutura do Projeto

crypto_price_app/
│
├─ app.py
├─ requirements.txt
└─ templates/
└─ index.html

- **app.py**: arquivo principal da aplicação Flask.  
- **requirements.txt**: lista de dependências necessárias.  
- **templates/index.html**: página web principal do app.

---