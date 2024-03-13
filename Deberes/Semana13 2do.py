
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI")

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Agregar", command=self.add_info)
        self.add_button.pack()

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

        self.clear_button = tk.Button(self.root, text="Limpiar", command=self.clear_info)
        self.clear_button.pack()

    def add_info(self):
        info = self.entry.get()
        self.listbox.insert(tk.END, info)
        self.entry.delete(0, tk.END)

    def clear_info(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()