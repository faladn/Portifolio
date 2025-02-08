import tkinter as tk

# Função para atualizar o visor da calculadora
def btn_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Função para calcular o resultado
def btn_equals():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para apagar o visor
def btn_clear():
    entry.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.geometry("376x439")  # Tamanho da janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Campo de entrada (visor)
entry = tk.Entry(root, width=16, font=("Arial", 24), bd=15, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky='ew')

# Botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('=', 4, 2),
    ('C', 5, 0), ('%', 5, 2)
]


# Adicionando os botões à janela

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), command=btn_equals)
        btn.grid(row=row, column=col, columnspan=2, sticky='snew')
    elif text == 'C':
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), command=btn_clear)
        btn.grid(row=row, column=col, columnspan=2, sticky='snew')
    elif text == '%':
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), command=lambda: btn_click('%'))
        btn.grid(row=row, column=col, columnspan=2, sticky='snew')
    else:
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), command=lambda value=text: btn_click(value))
        btn.grid(row=row, column=col, sticky='snew')

# Iniciando a interface gráfica
root.mainloop()