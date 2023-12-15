import tkinter as tk
from tkinter import filedialog

def save_text():
    save_path = filedialog.asksaveasfile(title = "Сохранить файл", filetypes = (("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    if save_path:
        save_path = save_path.name + ".txt"
        with open(save_path, 'w') as f:
            f.write(text_box.get("1.0", 'end-1c'))



window = tk.Tk()
window.title("Текстовый редактор")

text_box = tk.Text(window)
text_box.pack(fill = "both", expand = True)

save_button = tk.Button(window, text = "Сохранить", command = save_text)
save_button.pack()

window.mainloop()