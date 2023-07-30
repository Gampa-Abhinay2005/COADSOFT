from tkinter import *

def print_todo_list():
    todo_list_text.config(state=NORMAL)  # Enable editing temporarily to update the content
    todo_list_text.delete("1.0", END)
    for idx, task in enumerate(todo_list, start=1):
        todo_list_text.insert(END, f"{idx}. {task}\n")
    todo_list_text.config(state=DISABLED)  # Disable editing again after printing

def add_task():
    task = new_task_entry.get()
    if task:
        todo_list.append(task)
        new_task_entry.delete(0, END)
        print_todo_list()

def edit_task():
    index = int(edit_task_index.get()) - 1
    if 0 <= index < len(todo_list):
        new_task = new_task_entry_edit.get()
        if new_task:
            todo_list[index] = new_task
            edit_task_index.delete(0, END)
            new_task_entry_edit.delete(0, END)
            print_todo_list()

def delete_task():
    index = int(delete_task_index.get()) - 1
    if 0 <= index < len(todo_list):
        deleted_task = todo_list.pop(index)
        delete_task_index.delete(0, END)
        print_todo_list()

def exit_app():
    window.destroy()

todo_list=[]

window=Tk()
window.geometry("350x530")
window.title("To-Do List")

# Heading
heading_label = Label(window, text="         To-Do List          ", font=("Arial", 16, "bold"),fg=" blue",justify="center")
heading_label.pack(pady=10)

# Instructional text for adding tasks
add_task_label = Label(window, text="Enter a new task:", font=("Arial", 10))
add_task_label.pack()

# Entry and buttons for adding tasks
new_task_entry = Entry(window, width=30)
new_task_entry.pack(pady=5)
add_task_button = Button(window, text="Add Task", command=add_task,fg="green",bg="lightgreen")
add_task_button.pack()

# Separator line between input section and To-Do list display
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

# Instructional text for editing tasks
edit_task_label = Label(window, text="Enter task number and new text:", font=("Arial", 10))
edit_task_label.pack()

# Entry and buttons for editing tasks
edit_task_index = Entry(window, width=10)
edit_task_index.pack()
new_task_entry_edit = Entry(window, width=20)
new_task_entry_edit.pack()
edit_button = Button(window, text="Edit Task", command=edit_task,bg="orange",fg="red")
edit_button.pack()

# Instructional text for deleting tasks
delete_task_label = Label(window, text="Enter task number to delete:", font=("Arial", 10))
delete_task_label.pack()

# Entry and buttons for deleting tasks
delete_task_index = Entry(window, width=10)
delete_task_index.pack()
delete_button = Button(window, text="Delete Task", command=delete_task,bg="red",fg="white")
delete_button.pack()

# To-Do list display
todo_list_text = Text(window, height=10, width=40, wrap=WORD, state=DISABLED, bg="lightgreen", fg="blue")
todo_list_text.pack(pady=10)

# Exit button
exit_button = Button(window, text="Close", command=exit_app,fg="red",bg="white")
exit_button.pack(pady=10)

window.mainloop()
