import tkinter as tk
import tkinter.ttk as ttk



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
        
        
        self.bazis_var = tk.BooleanVar()
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




    #Entrys for bazis ///////////////////////////////////////////////////////////////////////////
    
    #создает поля ввода для значений базиса, очищает список старых полей
    def __create_entry(self,kolichestvo):
        self.bazis_entrys = []
        for i in range(kolichestvo):
            entry = ttk.Entry(master=self.task_frame, width=4)
            self.bazis_entrys.append(entry)
        self.condition_entrys()
    
    #удаляет все поля ввода из списка
    def __delete_entrys(self):
        for entry in self.bazis_entrys:
            entry.destroy()
   
   #отрисовывает все поля ввода если поставлена галочка (bazis_var == true) и скрывает их в обратном случае
    def condition_entrys(self):
        status = self.bazis_var.get()
        bazis_entrys = self.bazis_entrys
        if status:
            for i in range(len(bazis_entrys)):
                bazis_entrys[i].place(x=i*40+400, y=75)
        else:
            for i in range(len(bazis_entrys)):
                bazis_entrys[i].place_forget()


    '''сначала удаляет все поля ввода а потом создает новые, создавать поля следует только через
    эту функцию чтобы не потерять доступ к полям ввода из self.bazis_entrys, если вызвать
    create до delete то список полей обновится и старые поля уже нельзя булет удалить
    '''

    def update_entrys(self):
        self.__delete_entrys()
        self.__create_entry(self.demension_columns.get())

        #////////////////////////////////////////////////////////////////////////////////////////

    #Entrys matrix for equasion


    def __create_matrix(self):
        cols = self.demension_columns.get()
        rows = self.demension_rows.get()
        self.matrix = []
        for row in range(rows+1):
            entrys_row = []
            for col in range(cols):
                entry = ttk.Entry(master=self.task_frame, width=4)
                entrys_row.append(entry)
                entry.place(x=col*40+10,y=row*30+150)
            self.matrix.append(entrys_row)
        
    
    def __delete_matrix(self):
        matrix = self.matrix
        if len(matrix)>0:
            rows = len(matrix)
            cols = len(matrix[0])
            for row in range(rows):
                for col in range(cols):
                    self.matrix[row][col].destroy()
    
    def update_matrix(self):
        self.__delete_matrix()
        self.__create_matrix()


    #коллбек функция, срабатывает при изменении demension_columns
    def __on_change_demension_columns(self, var, index, mode):
        if self.columns_process is not None:
            self.root.after_cancel(self.columns_process)

        self.columns_process = self.root.after(500,self.update_entrys)


        if self.rows_process is not None:
            self.root.after_cancel(self.rows_process)

        self.rows_process = self.root.after(500,self.update_matrix)




    def __on_change_demension_rows(self, var, index, mode):
        if self.rows_process is not None:
            self.root.after_cancel(self.rows_process)

        self.rows_process = self.root.after(500,self.update_matrix)


    
    #коллбек функция, срабатывает при изменении значения bazis_var (чекбокс задать базис)
    def __on_change_checkbox(self, var, index, mode):
        self.condition_entrys()        

















Interface()   
