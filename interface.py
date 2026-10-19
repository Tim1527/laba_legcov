import tkinter as tk
import tkinter.ttk as ttk
print(10)

root = tk.Tk()

root.title("Simplex")
root.geometry('1080x720')
root.update_idletasks()

# Menu
main_menu = tk.Menu()
main_menu.add_cascade(label="Сохранить")
main_menu.add_cascade(label="Загрузить")
main_menu.add_cascade(label="Справка")
 

# Main tabs
tabs = ttk.Notebook()
tabs.pack(fill='both',side='top', expand=True, padx=5, pady=5)

graph_frame = ttk.Frame(tabs)
graph_frame.pack(expand=True)
tabs.add(graph_frame, text='Графический метод')

simplex_frame = ttk.Frame(tabs)
simplex_frame.pack(expand=True)
tabs.add(simplex_frame, text='Симплекс метод')


# Matrix label
bazis = tk.BooleanVar()

graph_settings_lbl = ttk.Label(master=graph_frame, text="Размерность матрицы")
graph_settings_lbl.pack(anchor='nw',padx=10, pady=10)

matrix_scale = tk.Scale(master=graph_frame, orient='horizontal', length=310, from_=1.0, to=16)
matrix_scale.pack(anchor='nw', padx=15, pady=10)

bazis_checkbutton = tk.Checkbutton(master=graph_frame, text="Задать базис", variable=bazis)
bazis_checkbutton.pack(anchor='nw', padx=350)









root.config(menu=main_menu)
tk.mainloop()
