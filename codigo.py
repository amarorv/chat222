# Estruturar telas para definir melhor o aplicativo

import flet as ft

# criar uma função principal para rodar o seu app

def main(pagina):
    # colocar o que a função irá fazer
    # titulo
    titulo = ft.Text("Hashzap")

    # websocket é um tunel de comunicação entre 2 usuários
    def enviar_mensagem_tunel(mensagem):
        #executar tudo o que eu quero que aconteça para todos os usuários
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        
        # limpar caixa de mensagem
        campo_enviar_mensagem.value = ""
        
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click= enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar popup
        popup.open = False
        # sumir com titulo
        pagina.remove(titulo)
        # sumir com o botao iniciar chat
        pagina.remove(botao)
        # carregar chat
        pagina.add(chat)
        # carregar campo de enviar mensagem e botao enviar
        pagina.add(linha_enviar)

        # adicionar mensagem de quem entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat!"
        pagina.pubsub.send_all(mensagem)
    
        pagina.update()

    # criar pop up
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                           actions=[botao_popup])

    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # COlocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)
    

# executar essa função com o flet
ft.app(main, view=ft.AppView.WEB_BROWSER)

# para disponibilizar para todos, utilizar flet.deploy