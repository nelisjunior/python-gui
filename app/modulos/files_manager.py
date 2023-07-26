import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def replace_files_content(directory, text):
    try:
        path = Path(directory)
        for file_path in path.glob('**/*'):
            if file_path.is_file():
                file_name = file_path.stem
                file_extension = file_path.suffix
                new_content = f"{text}{file_name}{file_extension}"
                with open(file_path, 'w') as f:
                    f.write(new_content)
        message_box.insert(tk.END, "Substitution completed successfully!\n")
    except Exception as e:
        message_box.insert(tk.END, f"An error occurred: {str(e)}\n")


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        files_dir_entry.delete(0, tk.END)
        files_dir_entry.insert(0, directory)


def submit():
    files_dir = files_dir_entry.get()
    text_user = text_entry.get()

    if not files_dir or not text_user:
        message_box.insert(tk.END, "Please enter a directory and text.\n")
        return

    replace_files_content(files_dir, text_user)


# Configurar janela
window = tk.Tk()
window.title("Gerenciamento de Arquivos de Texto")
window.geometry("400x400")

# Rótulo e entrada para diretório dos arquivos
files_dir_label = tk.Label(window, text="Diretório dos arquivos:")
files_dir_label.pack()
files_dir_entry = tk.Entry(window)
files_dir_entry.pack()

# Botão para selecionar o diretório
select_dir_button = tk.Button(window, text="Selecionar diretório", command=select_directory)
select_dir_button.pack()

# Rótulo e entrada para o texto personalizado
text_label = tk.Label(window, text="Texto personalizado:")
text_label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

# Botão para enviar o formulário
submit_button = tk.Button(window, text="Enviar", command=submit)
submit_button.pack()

# Caixa de mensagem
message_box = tk.Text(window)
message_box.pack()

# Iniciar a janela
window.mainloop()
