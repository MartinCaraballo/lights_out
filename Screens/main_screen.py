import tkinter as tk


class MainScreen:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry('300x400')
        self.root.configure(background='#F3CC86')
        self.root.title('Lights Out!')

        lbl = tk.Label(self.root,
                       text='Ingrese el tamaño del tablero:',
                       background='#F3CC86',
                       font=("Monospace", 11),
                       pady=10)
        lbl.pack()

        tk.Entry(self.root, font=("Monospace", 10)).pack()

        start_button = tk.Button(self.root,
                                 text='Start!',
                                 fg='black',
                                 bg='#CFA862',
                                 font=("Monospace", 10))
        start_button.pack(pady=10)
