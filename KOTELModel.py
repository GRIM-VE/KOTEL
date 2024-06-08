import numpy as np
class KOTEL:
    def __init__(self, Cp = 0, Hp = 0, Op = 0, Np = 0, Sp = 0,
                 Ap = 0, Wp = 0, alpha = 0, g_CB = 0, T_t = 0,
                 T_B = 0, K = 0):
        self.__Cp = Cp
        self.__Hp = Hp
        self.__Op = Op
        self.__Np = Np
        self.__Sp = Sp
        self.__Ap = Ap
        self.__Wp = Wp

        self.__alpha = alpha
        self.__g_CB = g_CB
        self.__T_t = T_t
        self.__T_B = T_B
        self.__K = K

        self.__results = []
    @property
    def Cp(self):
        return self.__Cp
    @property
    def Hp(self):
        return self.__Hp
    @property
    def Op(self):
        return self.__Op
    @property
    def Np(self):
        return self.__Np
    @property
    def Sp(self):
        return self.__Sp
    @property
    def Ap(self):
        return self.__Ap
    @property
    def Wp(self):
        return self.__Wp


    @property
    def alpha(self):
        return self.__alpha
    @property
    def g_CB(self):
        return self.__g_CB
    @property
    def T_t(self):
        return self.__T_t
    @property
    def T_B(self):
        return self.__T_B
    @property
    def K(self):
        return self.__K

    @property
    def results(self):
        return self.__results

    @Cp.setter
    def Cp(self,Cp):
        self.__Cp = Cp

    @Hp.setter
    def Hp(self, Hp):
        self.__Hp = Hp

    @Op.setter
    def Op(self, Op):
        self.__Op = Op

    @Np.setter
    def Np(self, Np):
        self.__Np = Np

    @Sp.setter
    def Sp(self, Sp):
        self.__Sp = Sp

    @Ap.setter
    def Ap(self, Ap):
        self.__Ap = Ap

    @Wp.setter
    def Wp(self, Wp):
        self.__Wp = Wp

    @alpha.setter
    def alpha(self, alpha):
        self.__alpha = alpha

    @g_CB.setter
    def g_CB(self, g_CB):
        self.__g_CB = g_CB

    @T_t.setter
    def T_t(self, T_t):
        self.__T_t = T_t

    @T_B.setter
    def T_B(self, T_B):
        self.__T_B = T_B

    @K.setter
    def K(self, K):
        self.__K = K

    #def _set_constants(self):
    def sumP(self):
        return(self.__Cp+self.__Hp+self.__Op+self.__Np+self.__Sp+self.__Ap+self.__Wp)
    def calcKOTEL(self):
        # Расчет количества воздуха, необходимого для сжигания 1 кг мазута.
        V_O2 = float(0.01 * (1.867 * self.__Cp + 5.6 * self.__Hp + 0.7 * self.__Sp - 0.7 * self.__Op))
        V_O2_ = round(V_O2, 4)
        L0_CB = float(V_O2 * (1 + self.__K))
        L0_CB_ = round(L0_CB, 4)
        L0_BB = float(L0_CB * (1 + 0.00124 * self.__g_CB))
        L0_BB_ = round(L0_BB, 4)
        Ld_BB = float(self.__alpha * L0_BB)
        Ld_BB_ = round(Ld_BB, 4)
        # Расчет объемного количества и состава продуктов горения мазута при alpha=1.
        V0_CO2 = float(0.01 * 1.867 * self.__Cp)
        V0_CO2_ = round(V0_CO2, 4)
        V0_SO2 = float(0.01 * 0.7 * self.__Sp)
        V0_SO2_ = round(V0_SO2, 4)
        V0_H2O = float(0.01 * (11.2 * self.__Hp + 1.244 * self.__Wp))
        V0_H2O_ = round(V0_H2O, 4)
        V0_N2 = float(0.01 * 0.8 * self.__Np + self.__K * V_O2)
        V0_N2_ = round(V0_N2, 4)
        V0 = float(V0_CO2 + V0_SO2 + V0_H2O + V0_N2)
        V0_ = round(V0, 4)
        # Расчет объемного количества и состава продуктов горения при заданной alpha.
        Vd_CO2 = float(V0_CO2)
        Vd_CO2_ = round(Vd_CO2, 4)
        Vd_SO2 = float(V0_SO2)
        Vd_SO2_ = round(Vd_SO2, 4)
        Vd_H2O = float(V0_H2O + 0.00124 * self.__g_CB * (self.__alpha - 1) * L0_CB)
        Vd_H2O_ = round(Vd_H2O, 4)
        Vd_N2 = float(V0_N2 + self.__K * (self.__alpha - 1) * V_O2)
        Vd_N2_ = round(Vd_N2, 4)
        V_O2_izb = float((self.__alpha - 1) * V_O2)
        V_O2_izb_ = round(V_O2_izb, 4)
        V_d = float(Vd_CO2 + Vd_SO2 + Vd_H2O + Vd_N2 + V_O2_izb)
        V_d_ = round(V_d, 4)
        # Низшая теплота сгорания мазута.
        Q_H_P = float(339 * self.__Cp + 1030 * self.__Hp + 109 * (self.__Op - self.__Sp) - 25 * (9 * self.__Hp + self.__Wp))
        Q_H_P_ = round(Q_H_P, 2)
        # Расчет температуры горения
        i_x = float(Q_H_P / V_d)
        i_x_ = round(i_x, 4)
        # Интерполяция для средней теплоемкостью воздуха Cp_B
        t_tab_v = np.arange(0,1400,100).tolist()
        Cp_B_tab = [1.298, 1.302, 1.306, 1.315, 1.327, 1.344, 1.357, 1.369, 1.382, 1.398, 1.411, 1.424, 1.432,
                    1.444]
        Cp_B = np.interp(self.__T_B, t_tab_v, Cp_B_tab)
        i_B = float((Cp_B * self.__T_B * Ld_BB) / V_d)
        i_B_ = round(i_B, 4)
        # Интерполяция для теплоемкости мазута Cp_T
        t_tab_m = [20, 100]
        Cp_T_tab = [1.88, 2.28]
        Cp_T = np.interp(self.__T_t, t_tab_m, Cp_T_tab)
        i_T = float((Cp_T * self.__T_t) / V_d)
        i_T_ = round(i_T, 4)
        i_sum = float(i_x + i_B + i_T)
        i_sum_ = round(i_sum, 4)
        V_L = float(((Ld_BB - L0_BB) / V_d) * 100)
        V_L_ = round(V_L, 2)
        self.__results =  [V_O2_, L0_CB_,
                          L0_BB_, Ld_BB_, V0_CO2_, V0_SO2_, V0_H2O_,
                          V0_N2_, V0_, Vd_CO2_, Vd_SO2_, Vd_H2O_,
                          Vd_N2_, V_O2_izb_, V_d_, Q_H_P_, i_x_,
                          i_B_, i_T_, i_sum_, V_L_]
