import tkinter.filedialog as fd
import pandas as pd
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
        self.view._demonstrate_data_from_file_cylinder_parameters()


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
