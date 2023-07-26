import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from datetime import datetime
from dotenv import dotenv_values

# Carregar as variáveis de ambiente do arquivo .env
env_vars = dotenv_values(".env")

# Obter os servidores disponíveis a partir do valor da variável LIST_SERVERNAME no arquivo .env
servidores_disponiveis = env_vars.get("LIST_SERVERNAME", "").split(",")


# Função para controlar a seleção do servidor
def select_servidor(var):
    for v in servidor_vars:
        if v is not var:
            v.set(False)


# Função para controlar a seleção da pasta de aplicação
def select_pasta_aplicacao(var):
    for v in pasta_aplicacao_vars:
        if v is not var:
            v.set(False)


# Função para gerar as URLs
def generate_urls():
    # Verificar se um servidor foi selecionado
    servidor = ""
    for i, var in enumerate(servidor_vars):
        if var.get():
            servidor = servidores_disponiveis[i]
            break

    if not servidor:
        messagebox.showerror("Erro", "Selecione um servidor.")
        return

    # Verificar se uma pasta de aplicação foi selecionada
    pasta_da_aplicacao = ""
    for i, var in enumerate(pasta_aplicacao_vars):
        if var.get():
            pasta_da_aplicacao = pasta_aplicacao_opts[i]
            break

    if not pasta_da_aplicacao:
        messagebox.showerror("Erro", "Selecione uma pasta de aplicação.")
        return

    # # Obter o diretório dos arquivos de entrada
    # input_folder_path = filedialog.askdirectory(title="Selecione o diretório dos arquivos de entrada")
    # if not input_folder_path:
    #     return

    # Obter o arquivo de lista de combos
    combo_file_path = filedialog.askopenfilename(title="Selecione o arquivo de lista de combos")
    if not combo_file_path:
        return

    # Obter o diretório de saída
    output_folder_path = filedialog.askdirectory(title="Selecione o diretório de saída")
    if not output_folder_path:
        return

    # Criar o nome do arquivo de saída
    combo_file_name = Path(combo_file_path).name
    current_date = datetime.now().strftime("%m%d%y")
    output_file_name = f"urls_{combo_file_name}_{current_date}"
    output_file_path = Path(output_folder_path) / output_file_name

    with open(combo_file_path, 'r') as combo_file:
        with open(output_file_path, 'w') as output_file:
            for line in combo_file:
                string_combo = line.strip()
                url = f"http://{servidor}/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&" \
                      f"BIP_folder=IBFS:/WFC/Repository/{pasta_da_aplicacao}/procedures/combos/&BIP_item={string_combo}\n"
                output_file.write(url)

    messagebox.showinfo("Sucesso", "URLs geradas com sucesso!")


# Criação da janela principal
window = tk.Tk()
window.title("Gerador de URLs para Consulta de Combos")
window.geometry("400x400")

# Vetores para armazenar os valores selecionados
servidor_vars = []
pasta_aplicacao_vars = []

# Criação dos widgets
server_label = tk.Label(window, text="Servidor:")
server_label.pack()

for servidor in servidores_disponiveis:
    servidor_var = tk.BooleanVar()
    servidor_checkbox = tk.Checkbutton(window, text=servidor, variable=servidor_var,
                                       command=lambda sv=servidor_var: select_servidor(sv))
    servidor_checkbox.pack()
    servidor_vars.append(servidor_var)

app_folder_label = tk.Label(window, text="Pasta da Aplicação:")
app_folder_label.pack()

pasta_aplicacao_opts = env_vars.get("LIST_APPLICATION", "").split(",")
for pasta_aplicacao in pasta_aplicacao_opts:
    pasta_aplicacao_var = tk.BooleanVar()
    pasta_aplicacao_checkbox = tk.Checkbutton(window, text=pasta_aplicacao, variable=pasta_aplicacao_var,
                                              command=lambda pa=pasta_aplicacao_var: select_pasta_aplicacao(pa))
    pasta_aplicacao_checkbox.pack()
    pasta_aplicacao_vars.append(pasta_aplicacao_var)

generate_button = tk.Button(window, text="Gerar URLs", command=generate_urls)
generate_button.pack()

# Loop principal da interface gráfica
window.mainloop()
