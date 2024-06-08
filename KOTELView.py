import KOTELController
import KOTELModel
#Импорт билиотек
from customtkinter import *
#Настройки цветовой гаммы
set_appearance_mode("light")  # Modes: system (default), light, dark
set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
#Функция глобальной кнопки ввода
class MyTabView(CTkTabview):
    def __init__(tab_of_window, master, **kwargs):
        super().__init__(master, **kwargs)
        tab_of_window.controller = KOTELController.KOTELController(view=tab_of_window, model=KOTELModel.KOTEL())
        tab_of_window.Block1_enter = []
        tab_of_window.Block2_enter = []
        tab_of_window.listOfRes = []
        tab_of_window.check = 0
        tab_of_window.namesOfResultsTabs = ["Результаты 1","Результаты 2","Результаты 3","Результаты 4","Результаты 5"]
        tab_of_window.add("Экран приветствия")

        #Экран приветсвия
        CTkLabel(tab_of_window.tab("Экран приветствия"),
                               text='Расчет температуры горения топлива',
                               font=("default", 18)).pack(padx=20, pady=10)
        CTkButton(tab_of_window.tab("Экран приветствия"),
                                text='Выбрать файл с исходными данными для расчёта', hover_color="grey",
                                font=("default", 18), command=lambda m=0: tab_of_window.controller._choose_file(m)).pack(padx=20, pady=5)
        CTkLabel(tab_of_window.tab("Экран приветствия"),
                               text='или',
                               font=("default", 18)).pack(padx=20, pady=10)
        CTkButton(tab_of_window.tab("Экран приветствия"),
                                text='Ввести данные вручную', hover_color="grey",
                                font=("default", 18), command=tab_of_window._kotel_parameters).pack(padx=20,
                                                                                                         pady=5)

    def _kotel_parameters(tab_of_window):
        # 1 Блок ввода

        nameOfTab1 = "Исходные данные: состав топлива"
        list_1 = ['Количество углерода в топливе, C, %', 'Количество водорода в топливе, H, %',
                  'Количество кислорода в топливе, O, %',
                  'Количество азота в топливе, N, %',
                  'Количество серы в топливе, S, %',
                  'Количество золы в топливе, A, %',
                  'Количество влаги в топливе, W, %']
        tab_of_window.add(nameOfTab1)
        tab_of_window.tab(nameOfTab1).grid_rowconfigure(7, weight=1)
        tab_of_window.tab(nameOfTab1).grid_columnconfigure((0, 10), weight=1)
        for i in range(len(list_1)):
            CTkLabel(tab_of_window.tab(nameOfTab1),
                     text=list_1[i], font=("default", 18)).grid(row=i, column=0, sticky="n", padx=5)
            tab_of_window.Block1_enter.append(CTkEntry(tab_of_window.tab(nameOfTab1)))
            tab_of_window.Block1_enter[i].grid(row=i, column=1, sticky="n")
        tab_of_window.label = CTkLabel(tab_of_window.tab(nameOfTab1),
                 text="",
                 font=("default", 18))
        tab_of_window.label.grid(row=len(list_1) + 2, column=0, sticky="n", padx=5)
        CTkButton(tab_of_window.tab(nameOfTab1), text="Сохранить состав топлива",
                  font=("default", 18), command=tab_of_window._kotel_parameters2).grid(
            row=len(list_1), column=1, sticky="n")

    def _kotel_parameters2(tab_of_window):

        tab_of_window.controller.Enter_Block1()
        nameOfTab1 = "Исходные данные: состав топлива"
        nameOfTab2 = "Исходные данные: параметры"
        list_1 = ['Количество углерода в топливе, C, %', 'Количество водорода в топливе, H, %',
                  'Количество кислорода в топливе, O, %',
                  'Количество азота в топливе, N, %',
                  'Количество серы в топливе, S, %',
                  'Количество золы в топливе, A, %',
                  'Количество влаги в топливе, W, %']
        list_2 = ['Коэффициент изыбтка воздуха альфа, alpha [-]',
                  'Влажность воздуха, g_CB [г/см3]',
                  'Температура мазута, T_t [град]',
                  'Температура подогрева воздуха, T_B [град]',
                  'Соотношение азота и кислорода в атмосфере, K [-]']
        try:
            tab_of_window.Block2_enter = []
            tab_of_window.delete(nameOfTab2)

        except Exception:
            pass
        try:
            for name in tab_of_window.namesOfResultsTabs:
                tab_of_window.delete(name)

        except Exception:
            pass
        if (tab_of_window.check):
            tab_of_window.label.configure(text = "")
            textCheck = 'Химический состав топлива введен верно'
            tab_of_window.add(nameOfTab2)
            tab_of_window.tab(nameOfTab2).grid_rowconfigure(7, weight=1)
            tab_of_window.tab(nameOfTab2).grid_columnconfigure((0, 10), weight=1)
            for i in range(len(list_2)):
                CTkLabel(tab_of_window.tab(nameOfTab2),
                         text=list_2[i], font=("default", 18)).grid(row=i, column=0, sticky="n", padx=5)
                tab_of_window.Block2_enter.append(CTkEntry(tab_of_window.tab(nameOfTab2)))
                tab_of_window.Block2_enter[i].grid(row=i, column=1, sticky="n")
            CTkButton(tab_of_window.tab(nameOfTab2), text="Начать расчет",
                      font=("default", 18), command=tab_of_window.print_results).grid(
                row=len(list_2), column=1, sticky="n")
        else:
            textCheck = 'Химический состав топлива введен неверно'
        tab_of_window.label.configure(text=textCheck)

    def print_results(tab_of_window):
        tab_of_window.controller.Enter_Block2()
        tab_of_window.controller.start_calc()
        tab_of_window.controller.Results()
        labelsForTabs = ["Определение количества воздуха, необходимого для сжигания 1 кг мазута",
         "Определение объёмного количества и состава продуктов горения мазута при α = 1",
         "Определение объёмного количества и состава продуктов горения мазута при заданной α",
         "Низшая теплота сгорания мазута",
         "Расчет температуры горения мазута"]

        try:
            for name in tab_of_window.namesOfResultsTabs:
                tab_of_window.add(name)
        except Exception:
            for name in tab_of_window.namesOfResultsTabs:
                for widgets in tab_of_window.tab(name).winfo_children():
                    widgets.destroy()

        listOfNamesOfListsForPrint = [["Количество кислорода, окисляющего все горючие компоненты мазута, Vo_O2, м3/кг",
                                       "Теоретический расход сухого атмосферного воздуха, Lo_CB, м3/кг",
                                       "Теоретический расход влажного воздуха, Lo_BB, м3/кг",
                                       "Действительный расход влажного воздуха, Ld_BB, м3/кг"],
                                      ["Объемное количество диоксида углерода, Vo_CO2, м3/кг",
                                       "Объемное количество диоксида серы, Vo_SO2, м3/кг",
                                       "Объемное количество водяных паров, Vo_H2O, м3/кг",
                                       "Объемное количество азота, Vo_N2, м3/кг",
                                       "Общий объем продуктов сгорания, Vo, м3/кг"],
                                      ["Объемное количество диоксида углерода, Vd_CO2, м3/кг",
                                       "Объемное количество диоксида серы, Vd_SO2, м3/кг",
                                       "Объемное количество водяных паров (увеличится за счет влаги избыточного воздуха), Vd_H2O, м3/кг",
                                       "Объемное количество азота (увеличится за счет избыточного воздуха), Vd_N2, м3/кг",
                                       "Объемное количество избыточного воздуха, V_O2_izb, м3/кг",
                                       "Общий объём продуктов горения при заданной α, Vd, м3/кг"],
                                      ["Низшая теплота сгорания, Q_H_P, кДж/кг"],
                                      ["Энтальпия единицы объёма дымовых газов за счёт химической энергии мазута, i_x, кДж/м3",
                                       "Подогретый воздух вносит в один кубометр отходящих газов, i_B, кДж/м3",
                                       "За счёт подогрева мазута единица продуктов горения получает, i_T, кДж/м3",
                                       "Общее теплосодержание продуктов горения мазута без учёта диссоциации, i_sum, кДж/м3",
                                       "Относительное содержание избыточного воздуха в единице продуктов горения мазута, V_L, кДж/м3"]]

        for i in range(len(tab_of_window.namesOfResultsTabs)):
            tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]).grid_rowconfigure(10, weight=1)
            tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]).grid_columnconfigure((0, 10), weight=1)
            CTkLabel(tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]),
                     text=labelsForTabs[i], font=("default", 18)).grid(row=1, column=0, sticky="n", padx=5)
            CTkLabel(tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]),
                     text="", font=("default", 18)).grid(row=2, column=0, sticky="n", padx=5)
            for j in range(len(listOfNamesOfListsForPrint[i])):
                CTkLabel(tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]),
                             text=listOfNamesOfListsForPrint[i][j], font=("default", 18)).grid(row=j+3, column=0, sticky="n", padx=5)
                CTkLabel(tab_of_window.tab(tab_of_window.namesOfResultsTabs[i]),
                             text=tab_of_window.listOfRes[i][j], font=("default", 18)).grid(row=j+3, column=1, sticky="n", padx=5)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('KOTEL')
        self.geometry("1000x400")
        self.tab_view = MyTabView(master=self)
        self.tab_view.pack(fill=BOTH, expand = True)

app=App()
app.mainloop()