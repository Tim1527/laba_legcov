import tkinter as tk
import tkinter.ttk as ttk
import time


class Interface:

    def __init__(self):
        
        self.create_window()
        self.tk_init()
        self.root.mainloop()
        
    def tk_init(self):
        
        self.bazis_entrys = []
        self.matrix = []
        self.columns_process = None
        self.rows_process = None
        
        self.__make_bazis_entrys()
        self.__make_matrix_entrys()

        self.bazis_var.trace_add('write',self.__on_change_checkbox)
        self.demension_columns.trace_add('write', self.__on_change_demension_columns)
        self.demension_rows.trace_add('write', self.__on_change_demension_rows)

    def create_window(self):
        
    #Создание и настройка главного окна приложения
        self.root = tk.Tk()

        self.root.title("Simplex")
        self.root.geometry('1080x720')
        self.root.update_idletasks()

    # Меню
        self.main_menu = tk.Menu()
        self.main_menu.add_cascade(label="Сохранить")
        self.main_menu.add_cascade(label="Загрузить")
        self.main_menu.add_cascade(label="Справка")
 

    # Main tabs
        '''
        Создание трёх вкладок
        task_frame - вкладка для ввода данных задачи
        graph_frame - вкладка с графическим решением задачи
        simplex_frame - вкладка с решением с помощью симплекс метода
        '''

        self.tabs = ttk.Notebook()
        self.tabs.pack(fill='both',side='top', expand=True, padx=5, pady=5)


        self.task_frame = ttk.Frame(self.tabs)
        self.task_frame.pack(expand=True)
        self.tabs.add(self.task_frame, text='Задача')


        self.graph_frame = ttk.Frame(self.tabs)
        self.graph_frame.pack(expand=True)
        self.tabs.add(self.graph_frame, text='Графический метод')

        self.simplex_frame = ttk.Frame(self.tabs)
        self.simplex_frame.pack(expand=True)
        self.tabs.add(self.simplex_frame, text='Симплекс метод')


    # Matrix label - настройки исходной задачи - размерность, и задание базиса
        
        
        self.bazis_var = tk.BooleanVar(value=False)
        self.demension_columns = tk.IntVar(value=5)
        self.demension_rows = tk.IntVar(value=5)

        self.graph_settings_lbl = ttk.Label(master=self.task_frame, text="Размерность матрицы")
        self.graph_settings_lbl.pack(anchor='nw',padx=10, pady=10)

        self.matrix_columns = tk.Scale(master=self.task_frame, orient='horizontal', length=310, from_=1, to=16, variable=self.demension_columns)
        self.matrix_columns.pack(anchor='nw', padx=15, pady=10)
        
        self.matrix_rows = tk.Scale(master=self.task_frame, orient="horizontal", length=310, from_=1, to=16, variable=self.demension_rows)
        self.matrix_rows.pack(anchor='nw', padx=15, pady=0)

        self.bazis_checkbutton = tk.Checkbutton(master=self.task_frame, text="Задать базис", variable=self.bazis_var)
        self.bazis_checkbutton.place(anchor='nw', x=450, y=25)
            

        self.root.config(menu=self.main_menu)






    def __make_bazis_entrys(self):
        '''
        Создаем строку полей для ввода базиса
        '''
        for i in range(16):
            entry = ttk.Entry(master=self.task_frame, width=4)
            self.bazis_entrys.append(entry)
 
    def show_bazis_entrys(self):
        cols = self.demension_columns.get()
        for i in range(cols):
            self.bazis_entrys[i].place(x=360+i*40, y=75)

    def hide_bazis_entrys(self):
        for entry in self.bazis_entrys:
            entry.place_forget()

        
    def update_bazis_entrys(self):
        self.hide_bazis_entrys()
        self.show_bazis_entrys()

    def __make_matrix_entrys(self):
        '''
        Создаем строку для ввода функции (максимум 16)
        '''
        row_of_entrys = []
        for i in range(16):
            entry = ttk.Entry(master=self.task_frame, width=4)
            row_of_entrys.append(entry)
        self.matrix.append(row_of_entrys)
        '''
        Создаем матрицу для ввода коэффицентов (максимум 16 +1 для столбца значений B)
        '''
        for row in range(16):
            row_of_entrys = []
            for col in range(16+1):
                entry = ttk.Entry(master=self.task_frame, width=4)
                row_of_entrys.append(entry)
            self.matrix.append(row_of_entrys)

        self.show_matrix_entrys()

    def show_matrix_entrys(self):
        cols = self.demension_columns.get()+1
        rows = self.demension_rows.get()+1
            
        for col in range(cols-1):
            self.matrix[0][col].place(x=15+col*40, y=200)

        for row in range(1,rows):
            for col in range(cols):
                self.matrix[row][col].place(x=15+col*40, y=200+25+row*25)


    def hide_matrix_entrys(self):
        matrix = self.matrix
        cols = len(matrix[1])
        rows = len(matrix)
            
        for col in range(cols-1):
            self.matrix[0][col].place_forget()

        for row in range(1,rows):
            for col in range(cols):
                self.matrix[row][col].place_forget()


    def update_matrix_entrys(self):
        self.hide_matrix_entrys()
        self.show_matrix_entrys()



 
    #коллбек функция, срабатывает при изменении demension_columns
    def __on_change_demension_columns(self, var, index, mode):
        if self.columns_process is not None:
            self.root.after_cancel(self.columns_process)
        
        if self.bazis_var.get():
            self.columns_process = self.root.after(500,self.update_bazis_entrys)


        if self.rows_process is not None:
            self.root.after_cancel(self.rows_process)

        self.rows_process = self.root.after(500,self.update_matrix_entrys)




    def __on_change_demension_rows(self, var, index, mode):
        if self.rows_process is not None:
            self.root.after_cancel(self.rows_process)

        self.rows_process = self.root.after(500,self.update_matrix_entrys)
    
    #коллбек функция, срабатывает при изменении значения bazis_var (чекбокс задать базис)
    def __on_change_checkbox(self, var, index, mode):       
        status = self.bazis_var.get()
        if status:
            self.show_bazis_entrys()
        else:
            self.hide_bazis_entrys()
















Interface()   
