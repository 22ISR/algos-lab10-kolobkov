import tkinter as tk
root = tk.Tk()
root.title("Список дел")
root.geometry("300x400")


def get_selected():
    new_language = textbox.get()
    if new_language:
        listbox.insert(tk.END, new_language)
        textbox.delete("0", tk.END)

select_button = tk.Button(root, text="Добавить", command=get_selected)
select_button.pack()

textbox = tk.Entry(root, font=("Arial", 16))
textbox.pack(padx=20, pady=20)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

listbox.insert(tk.END, "Элемент 1")
listbox.insert(tk.END, "Элемент 2")
listbox.insert(tk.END, "Элемент 3")

def delete_selected():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

delete_button = tk.Button(root, text="Удалить", command=delete_selected)
delete_button.pack()

root.mainloop()