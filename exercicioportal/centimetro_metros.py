
# Claro, aqui está um exemplo de código usando Tkinter para converter centímetros para metros:

import tkinter as tk

def converter_cm_para_m():
    try:
        cm = float(entrada_cm.get())
        metros = cm / 100
        resultado_label.config(text=f"{cm} cm equivalem a {metros} metros.")
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")
janela.geometry("300x150")

# Criando os widgets
titulo_label = tk.Label(janela, text="Digite o valor em centímetros:")
titulo_label.pack()

entrada_cm = tk.Entry(janela)
entrada_cm.pack()

converter_btn = tk.Button(janela, text="Converter", command=converter_cm_para_m)
converter_btn.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Iniciando o loop principal da janela
janela.mainloop()
