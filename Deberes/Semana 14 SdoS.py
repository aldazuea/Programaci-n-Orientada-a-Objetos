import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        self.event_list = ttk.Treeview(self.root, columns=("Date", "Time", "Description"), show="headings")
        self.event_list.heading("Date", text="Date")
        self.event_list.heading("Time", text="Time")
        self.event_list.heading("Description", text="Description")
        self.event_list.pack()

        date_label = tk.Label(self.root, text="Date:")
        date_label.pack()
        self.date_entry = Calendar(self.root)
        self.date_entry.pack()

        time_label = tk.Label(self.root, text="Time:")
        time_label.pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()

        desc_label = tk.Label(self.root, text="Description:")
        desc_label.pack()
        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.pack()

        add_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        add_button.pack()

        delete_button = tk.Button(self.root, text="Delete Selected Event", command=self.delete_event)
        delete_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=root.quit)
        exit_button.pack()

    def add_event(self):
        date = self.date_entry.get_date()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        self.event_list.insert("", "end", values=(date, time, desc))

    def delete_event(self):
        selected_item = self.event_list.selection()[0]
        self.event_list.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()