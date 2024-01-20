# NyphChat - Chat em Tempo Real

Bem-vindo ao NyphChat, um projeto de chat em tempo real desenvolvido utilizando o framework Flet.

## Descrição do Projeto
NyphChat é uma aplicação de chat simples e eficiente que permite aos usuários se comunicarem em tempo real. Este projeto utiliza o framework Flet para criar um servidor web que suporta comunicação em tempo real entre os usuários.

## Funcionalidades Principais
- **Entrar no Chat:** Os usuários podem fornecer um nome de usuário e entrar no chat clicando no botão "Entrar".
- **Enviar Mensagens:** Após entrar no chat, os usuários podem enviar mensagens digitando-as na caixa de texto e clicando no botão "Enviar".
- **Atualizações em Tempo Real:** Todas as mensagens enviadas são exibidas instantaneamente para todos os usuários conectados, proporcionando uma experiência de chat em tempo real.

## Pré-requisitos
Certifique-se de ter o Python e o Flet instalados em seu ambiente de desenvolvimento antes de executar o projeto.

```bash
pip install flet```

## Executando o Projeto
Execute o seguinte script Python para iniciar o servidor do NyphChat:

```python
import flet as ft

def main(pageMain):
    # ... (Código do seu chat)

ft.app(main, view=ft.WEB_BROWSER, port=8000)
```

Acesse o chat pelo navegador em `http://localhost:8000`.

## Estrutura do Código
O código utiliza o framework Flasklet para a criação da interface de usuário. A função `main` define os elementos da interface, como caixas de texto, botões e a área de exibição do chat. A comunicação em tempo real é gerenciada através do uso do `pubsub` do flet.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou fornecer feedback para melhorar o NyphChat.

Divirta-se usando o NyphChat e conectando-se em tempo real com outros usuários!