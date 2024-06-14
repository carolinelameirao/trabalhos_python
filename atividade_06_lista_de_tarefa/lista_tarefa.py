import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        self.label = tk.Label(root, text="Digite a tarefa:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", font=("Helvetiva", 10, "bold"), command = self.add_task)
        self.add_button.pack(pady=5)
        
        self.listbox = tk.Listbox(root, width=50, height=10)  
        self.listbox.pack(pady=10)
        
        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.tasks = []
    
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