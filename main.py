import flet as ft

def main(pageMain):
    title = ft.Text("NyphChat")
    
    name_user = ft.TextField(label="Nome de usuario")
    message_container = ft.TextField(label="Enviar Mensagem")
    chat = ft.Column()

    def submit_backend(inf):
        chat.controls.append(ft.Text(inf))
        pageMain.update()

    pageMain.pubsub.subscribe(submit_backend)

    def submit_message(event):
        message = f"{name_user.value}: {message_container.value}"
        pageMain.pubsub.send_all(message)
        message_container.value = ""
        pageMain.update()

    message_button = ft.ElevatedButton("Enviar", on_click=submit_message)
    linha = ft.Row([message_container, message_button])

    def enter_chat(event):
        popup.open = False
        pageMain.remove(buttonInit)
        pageMain.add(chat)
        pageMain.add(linha)
        pageMain.pubsub.send_all(f"{name_user.value} Entrou no Chat")
        pageMain.update()

    popup = ft.AlertDialog(
        open=True,
        modal=False,
        title=ft.Text("Entrar no Chat"),
        content=name_user,
        actions=[ft.ElevatedButton("Entrar", on_click=enter_chat)]
        )

    def init_chat(event):
        pageMain.dialog = popup
        popup.open = True
        pageMain.update()

    buttonInit = ft.ElevatedButton("Entrar", on_click=init_chat)

    pageMain.add(title)
    pageMain.add(buttonInit)

ft.app(main, view=ft.WEB_BROWSER, port=8000)
