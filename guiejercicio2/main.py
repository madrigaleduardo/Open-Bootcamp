import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="¿Qué producto deseas comprar?")
        self.label.pack()

        self.lista_productos = ["Procesador", "Tarjeta madre", "Memoria RAM", "Disco duro", "Tarjeta de video"]
        self.producto_seleccionado = tk.StringVar()
        self.lista = tk.Listbox(self.master, listvariable=self.producto_seleccionado)
        for producto in self.lista_productos:
            self.lista.insert(tk.END, producto)
        self.lista.pack()

root = tk.Tk()
app = App(root)
root.mainloop()
