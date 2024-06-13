import tkinter as tk
from tkinter import messagebox
from tkinter import *

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []
        
        self.label = tk.Label(root, text="Tarefa:", bg='gray', relief='flat', font=("Arial", 10, "bold"))
        self.label.grid(column=0, row=250, padx=10, pady=55)
        self.label.pack()
        
        self.entry = tk.Entry(root, width=50, font=("Arial", 10, "bold"))
        self.entry.place(height=25, width=395, x=12, y=85)
        self.entry.pack()
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", font=("Helvetiva", 10, "bold"), command = self.add_task)
        self.add_button.place(x=450, y=85, height=25, width=90)
        self.add_button.pack()
        
        self.listbox = tk.Listbox(root, width=60)
        self.listbox.place(height=55, width=395, x=12, y=125)   
        self.listbox.pack()
        
        self.remove_button = tk.Button(root, text="Remover Tarefa", font=("Helvetiva", 10, "bold"), command=self.remove_task)
        self.remove_button.place(x=450, y=122, height=25, width=90)
        self.remove_button.pack()
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa antes de adicionar.")

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
                
    def update_tasks_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()