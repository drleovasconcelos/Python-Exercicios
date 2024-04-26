# Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python.
# O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@",
# ou seja, realizar uma tela de login com restrições de e-mail e senha.

import tkinter as tk
from tkinter import messagebox

def fazer_login():
    email = entrada_email.get()
    senha = entrada_senha.get()

    if len(senha) < 6:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
        return

    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
        return

    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

# Criar janela principal
root = tk.Tk()
root.title("Login")

# Criar rótulos e campos de entrada
label_email = tk.Label(root, text="E-mail:")
label_email.pack()
entrada_email = tk.Entry(root)
entrada_email.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack()

# Criar botão de login
botao_login = tk.Button(root, text="Login", command=fazer_login)
botao_login.pack()

# Iniciar loop principal
root.mainloop()
