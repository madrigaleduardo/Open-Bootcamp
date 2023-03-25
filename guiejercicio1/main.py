import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.var = tk.StringVar()
        self.var.set(None)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Selecciona una opción:").pack()
        tk.Radiobutton(self.master, text="Opción 1", variable=self.var, value="Opción 1").pack()
        tk.Radiobutton(self.master, text="Opción 2", variable=self.var, value="Opción 2").pack()
        tk.Radiobutton(self.master, text="Opción 3", variable=self.var, value="Opción 3").pack()
        tk.Button(self.master, text="Reiniciar", command=self.reset).pack()

    def reset(self):
        self.var.set(None)

root = tk.Tk()
app = App(root)
root.mainloop()
