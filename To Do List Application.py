import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.description} - {'Done' if self.completed else 'Not Done'}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack()

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.mark_button = tk.Button(self.button_frame, text="Mark as Completed", command=self.mark_completed)
        self.mark_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            task = Task(task_description)
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task description.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_description = self.task_entry.get()
            if new_description:
                self.tasks[selected_task_index].description = new_description
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index].completed = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
