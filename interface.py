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


task_frame = ttk.Frame(tabs)
task_frame.pack(expand=True)
tabs.add(task_frame, text='Задача')


graph_frame = ttk.Frame(tabs)
graph_frame.pack(expand=True)
tabs.add(graph_frame, text='Графический метод')

simplex_frame = ttk.Frame(tabs)
simplex_frame.pack(expand=True)
tabs.add(simplex_frame, text='Симплекс метод')


# Matrix label
bazis_var = tk.BooleanVar()
demention = tk.IntVar(value=5)

graph_settings_lbl = ttk.Label(master=task_frame, text="Размерность матрицы")
graph_settings_lbl.pack(anchor='nw',padx=10, pady=10)

matrix_scale = tk.Scale(master=task_frame, orient='horizontal', length=310, from_=1.0, to=16, variable=demention)
matrix_scale.pack(anchor='nw', padx=15, pady=10)

bazis_checkbutton = tk.Checkbutton(master=task_frame, text="Задать базис", variable=bazis_var)
bazis_checkbutton.place(anchor='nw', x=450, y=25)


#Entrys for bazis

bazis_entrys = []

def create_entry(kolichestvo):
    global bazis_entrys
    bazis_entrys = []
    for i in range(kolichestvo):
        entry = ttk.Entry(master=task_frame, width=4)
        bazis_entrys.append(entry)
        entry.place(x=i*40+400, y=75)


def delete_entrys(entrys):
    for entry in entrys:
        entry.destroy()
    

def update_entrys():
    global bazis_entrys
    delete_entrys(bazis_entrys)
    create_entry(demention.get())



def on_change_scale(var, index, mode):
    if bazis_var.get():
        update_entrys()


def on_change_checkbox(var, index, mode):
    global bazis_entrys
    update_entrys()
    status = bazis_var.get()
    if status:
        for i in range(len(bazis_entrys)):
            bazis_entrys[i].place(x=i*40+400, y=75)
    else:
        for i in range(len(bazis_entrys)):
            bazis_entrys[i].place_forget()



bazis_var.trace_add('write',on_change_checkbox)
demention.trace_add('write',on_change_scale)






root.config(menu=main_menu)
tk.mainloop()
