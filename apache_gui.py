import os
import shutil
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()

APACHE_CONF_DIR = os.getenv("APACHE_CONF_DIR")
ARQUIVO_ATUAL = os.getenv("HTTPD_CONF")
ARQUIVOS_DISPONIVEIS = os.getenv("ARQUIVOS_DISPONIVEIS").split(",")


def mostrar_mensagem(mensagem):
    # Adiciona a mensagem ao widget de texto
    message_display.insert(tk.END, mensagem + "\n")
    # Rola a visualização para o final para exibir a mensagem mais recente
    message_display.see(tk.END)


def verificar_arquivos_existem():
    arquivos_ausentes = []
    # verifica se httpd.conf está presente
    if not os.path.exists(os.path.join(APACHE_CONF_DIR, ARQUIVO_ATUAL)):
        arquivos_ausentes.append(ARQUIVO_ATUAL)
    for arquivo in ARQUIVOS_DISPONIVEIS:
        if not os.path.exists(os.path.join(APACHE_CONF_DIR, f"httpd.conf.{arquivo}")):
            arquivos_ausentes.append(arquivo)
    return len(arquivos_ausentes) == 0, arquivos_ausentes


def mostrar_arquivos():
    return ARQUIVOS_DISPONIVEIS


def renomear_arquivo():
    arquivo_escolhido = listbox.get(tk.ACTIVE)
    caminho_arquivo = os.path.join(APACHE_CONF_DIR, f"httpd.conf.{arquivo_escolhido}")
    mostrar_mensagem(f"Arquivo {arquivo_escolhido} selecionado.")
    # Copiar uma cópia do arquivo escolhido para httpd.conf
    shutil.copy(caminho_arquivo, os.path.join(APACHE_CONF_DIR, ARQUIVO_ATUAL))
    # status_text.set(f"Arquivo renomeado para {ARQUIVO_ATUAL}")
    mostrar_mensagem(f"Arquivo renomeado para {ARQUIVO_ATUAL}")


def excluir_arquivo():
    caminho_arquivo = os.path.join(APACHE_CONF_DIR, ARQUIVO_ATUAL)
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
    # status_text.set(f"Arquivo {caminho_arquivo} excluído")
    mostrar_mensagem(f"Arquivo {caminho_arquivo} excluído")


def configurar_apache():
    excluir_arquivo()
    renomear_arquivo()


def atualizar_lista():
    listbox.delete(0, tk.END)
    for arquivo in ARQUIVOS_DISPONIVEIS:
        listbox.insert(tk.END, arquivo)

    status_ok, arquivos_ausentes = verificar_arquivos_existem()

    if status_ok:
        mostrar_mensagem("Todos os arquivos foram encontrados.")
    else:
        mostrar_mensagem(f"O arquivo {arquivos_ausentes} está faltando.")


def limpar_mensagem():
    message_display.delete(1.0, tk.END)


# Criação da janela principal
window = tk.Tk()
window.title("Manage Apache Server")
window.geometry("400x400")


# Criação dos elementos da GUI
label = tk.Label(window, text="MONITOR")
label.pack()

# Criação do widget de texto para exibir as mensagens
message_display = tk.Text(window, height=5, width=100)
message_display.pack()

# Criação dos elementos da GUI
label = tk.Label(window, text="Arquivos httpd.conf Cadastrados")
label.pack()

listbox = tk.Listbox(window, height=5, width=20)    # Lista de arquivos
listbox.pack()                # Adiciona a lista na janela

status_text = tk.StringVar()    # Variável de texto para o status
status_label = tk.Label(window, textvariable=status_text)   # Label para o status
status_label.pack()           # Adiciona o label na janela

# Atualiza a lista inicial
atualizar_lista()


# Criação do botão de atualizar
button1 = tk.Button(window, text="Atualizar", command=atualizar_lista)
button1.pack()

# Criação do botão de limpar
button2 = tk.Button(window, text="Limpar", command=limpar_mensagem)
button2.pack()

# Criação do botão de configurar
button3 = tk.Button(window, text="Configurar", command=configurar_apache)
button3.pack()

# Inicia o loop principal da janela
window.mainloop()