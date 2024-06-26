import tkinter.filedialog as fd
import pandas as pd
import itertools
class KOTELController:

    def __init__( self, model = None, view = None):
        self.__model = model
        self.__view = view
        self.__l1 = []
        self.__l2 = []
        self.__list_Ro = []

    @property
    def view( self ):
        return self.__view

    @property
    def model( self ):
        return self.__model

    @view.setter
    def view( self, view ):
        self.__view = view

    @model.setter
    def model( self, model ):
        self.__model = model

    def _Block1_filling(self, i):
        match i:
            case 0:
                try:
                    self.model.Cp = int(self.view.Block1_enter[i].get())
                except:
                    self.model.Cp = 0
            case 1:
                try:
                    self.model.Hp = float(self.view.Block1_enter[i].get())
                except:
                    self.model.Hp = 0
            case 2:
                try:
                    self.model.Op = float(self.view.Block1_enter[i].get())
                except:#добавить сообщение об ошибке
                    self.model.Op = 0
            case 3:
                try:
                    self.model.Np = float(self.view.Block1_enter[i].get())
                except:#добавить сообщение об ошибке
                    self.model.Np = 0
            case 4:
                try:
                    self.model.Sp = float(self.view.Block1_enter[i].get())
                except:#добавить сообщение об ошибке
                    self.model.Sp = 0
            case 5:
                try:
                    self.model.Ap = float(self.view.Block1_enter[i].get())
                except:#добавить сообщение об ошибке
                    self.model.Ap = 0
            case 6:
                try:
                    self.model.Wp = float(self.view.Block1_enter[i].get())
                except:#добавить сообщение об ошибке
                    self.model.Wp = 0

    def _clear_block1(self):
        self.model.Cp = 0
        self.model.Hp = 0
        self.model.Op = 0
        self.model.Np = 0
        self.model.Sp = 0
        self.model.Ap = 0
        self.model.Wp = 0

    def Enter_Block1(self):
        self._clear_block1()
        for i in range(len(self.view.Block1_enter)):
            self._Block1_filling(i)
        sumP = self.model.sumP()
        self.view.check = (1 if sumP == 100 else 0)
    def _clear_block2(self):
        self.model.alpha = 0
        self.model.g_CB = 0
        self.model.T_t = 0
        self.model.T_B = 0
        self.model.K = 0
    def _Block2_filling(self, i):
        match i:
            case 0:
                try:
                    self.model.alpha = float(self.view.Block2_enter[i].get())
                except:
                    self.model.alpha = 0
            case 1:
                try:
                    self.model.g_CB = float(self.view.Block2_enter[i].get())
                except:
                    self.model.g_CB = 0
            case 2:
                try:
                    self.model.T_t = float(self.view.Block2_enter[i].get())
                except:  # добавить сообщение об ошибке
                    self.model.T_t = 0
            case 3:
                try:
                    self.model.T_B = float(self.view.Block2_enter[i].get())
                except:  # добавить сообщение об ошибке
                    self.model.T_B = 0
            case 4:
                try:
                    self.model.K = float(self.view.Block2_enter[i].get())
                except:  # добавить сообщение об ошибке
                    self.model.K = 0
    def Enter_Block2(self):
        self._clear_block2()
        for i in range(len(self.view.Block2_enter)):
            self._Block2_filling(i)
    def _choose_file(self, m):  # v0. Оптимизировать
        if(m==0):
            filetypes = (("Файл Excel", "*.xlsx *.xls"),)
            filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                          filetypes=filetypes)
            file = pd.ExcelFile(filename)
            self.view.data = pd.read_excel(file)
        self.view._kotel_parameters()


    def start_calc(self):
        self.model.calcKOTEL()
    def Results(self):
        self.view.listOfRes = []
        sumOfPrev = 0
        numOfVar = [4, 5, 6, 1, 5]
        for i in range(len(numOfVar)):
            self.view.listOfRes.append([])
            for j in range(numOfVar[i]):
                self.view.listOfRes[i].append(sumOfPrev+self.model.results[j])
            sumOfPrev+=numOfVar[i]
    def _create_file(self):
        names_of_outputs = ['Определение количества воздуха, необходимого для сжигания 1 кг топлива',
                            'Определение объёмного количества и состава продуктов горения мазута (alpha = 1)',
                            'Определение объёмного количества и состава продуктов горения при заданной alpha',
                            'Низшая теплота сгорания топлива',
                            'Расчет теоретической температуры горения'
                            ]
        names_of_rows = [
'Количество кислорода, окисляющего все горючие компоненты мазута, V_O2',
'Теоретический расход сухого атмосферного воздуха, L0_св',
'Теоретический расход влажного воздуха, L0_вв',
'Действительный расход влажного воздуха, Ld_вв',

'Объёмное количество диоксида углерода, V0_CO2',
'Объёмное количество диоксида серы, V0_SO2',
'Объёмное количество водяных паров, V0_H2O',
'Количество азота, V0_N2',
'Общий объём продуктов горения(alpha=1), V0',

'Объёмное количество диоксида углерода, V0_CO2',
'Объёмное количество диоксида серы, V0_SO2',
'Объёмное количество водяных паров, V0_H2O',
'Количество азота, V0_N2',
'Объемное количество избыточного воздуха, V_O2_изб',
'Общий объём продуктов горения(alpha=1), V0',

'Низшая теплота сгорания, Q_н_р',

'Энтальпия единицы объёма дымовых газов за счёт химической энергии мазута, i_x',
'Подогретый до определенной температуры воздух, вносит в один кубометр отходящих газов, i_в',
'За счёт подогрева топлива единица продуктов горения получает, i_т',
'Общее теплосодержание продуктов горения мазута без учёта диссоциации, i_общ',
'Относительное содержание избыточного воздуха в единице продуктов горения мазута, V_L'

        ]
        sizes_of_outs = [4,5,6,1,5]
        df_list = []
        num_of_row = 0

        for size in sizes_of_outs:
            for i in range(num_of_row,num_of_row+size):
                df_list.append([])
                df_list[i].append(names_of_rows[i])
            num_of_row+=size

        rezults = list(itertools.chain.from_iterable(self.view.listOfRes))
        for i in range(len(self.model.results)):
                df_list[i].append(rezults[i])

        directoryname = fd.askdirectory(title="Сохранить файл в папке", initialdir="/")
        df1 = pd.DataFrame(df_list)
        df1.to_excel(directoryname+"/Результаты расчета.xlsx",startrow=1, header=False, index=False)

    def _create_file_start(self):
        names_of_rows_cylinder = ['Количество углерода в топливе, C (%)', 'Количество водорода в топливе, H (%)',
                                  'Количество кислорода в топливе, O (%)', 'Количество азота в топливе, N (%)',
                                  'Количество серы в топливе, S (%)',
                         'Количество золы в топливе, A (%)', 'Количество влаги в топливе, W (%)']
        names_of_rows_stages = ['Коэффициент избытка воздуха, alpha','Влажность воздуха, g_св', 'Температура топлива, T_т',
                                'Температура подогрева воздуха, T_в',
                                  'Соотношение азота и кислорода в атмосфере, K']
        df_list_cyl = []

        for i in range(len(names_of_rows_cylinder)):
            df_list_cyl.append([])
            df_list_cyl[i].append(names_of_rows_cylinder[i])

        for i in range(len(self.view.Block1_enter)):
            df_list_cyl[i].append(self.view.Block1_enter[i].get())
            df_list_cyl[i].append('')

        for i in range(len(names_of_rows_stages)):
            df_list_cyl.append([])
            df_list_cyl[i].append(names_of_rows_stages[i])

        for i in range(len(self.view.Block2_enter)):
            df_list_cyl[i].append(self.view.Block2_enter[i].get())
            df_list_cyl[i].append('')

        directoryname = fd.askdirectory(title="Сохранить файл в папке", initialdir="/")
        df1 = pd.DataFrame(df_list_cyl)
        df1.to_excel(directoryname+"/Исходные_данные_KOTEL.xlsx",startrow=1, header=False, index=False)