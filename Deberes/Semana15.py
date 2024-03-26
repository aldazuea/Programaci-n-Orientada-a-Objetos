import tkinter as tk


class TaskListApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Task List App')

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        self.task_list = tk.Listbox(self.root, width=50)
        self.task_list.pack()

        self.tasks = []

        self.task_entry.bind("<Return>", self.add_task_event)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            task_name = task["task"]
            if task["completed"]:
                task_name += " (Completada)"
            self.task_list.insert(tk.END, task_name)

    def add_task_event(self, event):
        self.add_task()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskListApp(root)
    root.mainloop()
