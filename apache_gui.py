import tkinter as tk
import os


# Função para listar os arquivos httpd.conf existentes
def listar_arquivos():
    dir_path = ""

    try:
        os.chdir(dir_path)
        files = [f for f in os.listdir(dir_path) if f.startswith("httpd.conf")]
        return files
    except Exception as e:
        return []


# Função para atualizar a lista de arquivos exibidos
def atualizar_lista():
    listbox.delete(0, tk.END)
    files = listar_arquivos()

    for file in files:
        listbox.insert(tk.END, file)


# Função para preencher as Entry com o nome atual e novo nome do arquivo selecionado
def preencher_entries(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_file = listbox.get(selected_index)
        entry_atual.delete(0, tk.END)
        entry_atual.insert(tk.END, selected_file)
        entry_novo.delete(0, tk.END)
        entry_novo.insert(tk.END, selected_file)
        selected_item_index[0] = selected_index[0]


# Função para renomear o arquivo selecionado
def renomear_arquivo():
    nome_atual = entry_atual.get()
    nome_novo = entry_novo.get()

    if selected_item_index[0] is not None:
        selected_index = selected_item_index[0]
        selected_file = listbox.get(selected_index)
        dir_path = ""

        try:
            os.chdir(dir_path)

            os.rename(selected_file, nome_novo)
            status_label["text"] = f"Arquivo {selected_file} renomeado para {nome_novo} com sucesso!"
            listbox.delete(selected_index)
            listbox.insert(selected_index, nome_novo)
            listbox.selection_set(selected_index)

        except Exception as e:
            status_label["text"] = f"Ocorreu um erro: {str(e)}"
    else:
        status_label["text"] = "Selecione um arquivo para renomear!"


# Criação da janela principal
window = tk.Tk()
window.title("Manage Apache Server ")
window.geometry("400x350")

# Variável para armazenar o índice do item selecionado
selected_item_index = [None]

# Criação dos elementos da GUI
label = tk.Label(window, text="Arquivos httpd.conf existentes:")
label.pack()

listbox = tk.Listbox(window)
listbox.pack()

label_atual = tk.Label(window, text="Nome atual:")
label_atual.pack()

entry_atual = tk.Entry(window)
entry_atual.pack()

label_novo = tk.Label(window, text="Novo nome:")
label_novo.pack()

entry_novo = tk.Entry(window)
entry_novo.pack()

listbox.bind("<<ListboxSelect>>", preencher_entries)

button_listar = tk.Button(window, text="Listar Arquivos", command=atualizar_lista)
button_listar.pack()

button_renomear = tk.Button(window, text="Renomear Arquivo", command=renomear_arquivo)
button_renomear.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Loop principal da GUI
window.mainloop()
