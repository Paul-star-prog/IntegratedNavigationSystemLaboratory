# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:05:24 2021

@author: Павел Ермаков
"""

from ABCMathModel import ABCMathModel
import numpy as np
from scipy import interpolate, genfromtxt
class AirfoilBoatModel(ABCMathModel):
    """
    Класс,реализующий математическую модель экраноплана (продольный канал)
    """
    def __init__(self):
        # Вектор - сотояния модели
        self._dY = np.zeros([6])
        # Константы модели
        self.__g = 9.81
        self.__Jz = 30376.11
        self.__B = 7.84
        self.__S = 37.66
        self.__m = 4200
        self.__P = 3400
        self.__delta_RV = 1e-1
        self.__delta_ZCP = 1e-2
        self.__delta_ZEL = 1e-2
        # Список названий файлов данных
        FileDataName = ["AltitudeTheta.txt","AirDensityAltitude.txt", "Cx.txt", "dCxdHdt.txt",\
                        "Cy.txt", "dCydRV.txt","dCydHdt.txt", "dCydOmz.txt", "Mz.txt",\
                        "dMzdRV.txt", "dMzdHt.txt", "dMzdOmz.txt"]
        # Список таблиц данных
        self.__ListTable = []
        for i in range(len(FileDataName)):
            self.__ListTable.append(genfromtxt(FileDataName[i], delimiter = " "))
    def RightPart(self, t, y):
         # y[0] - Скорость, м / сек
         # y[1] - Угол наклона траектории, рад
         # y[2] - Координата X, м
         # y[3] - Высота, м
         # y[4] - Угловая скорость вращения экраноплана по OZ, рад / сек
         # y[5] - Угол тангажа, рад 
         # Плотность воздуха на высоте, кг / м^3
         Ro = interpolate.interp1d(self.__ListTable[1][:,1], self.__ListTable[1][:,0], fill_value='extrapolate')(y[3])
         # Относительная высота, м
         hrelative = y[3] / self.__B
         # Список а/д коэффициентов модели
         Coeff = []
         for i in range(2, len(self.__ListTable)):
             Coeff.append(interpolate.interpn((self.__ListTable[0][:,0], self.__ListTable[0][:,1]), self.__ListTable[i], (hrelative, y[5]), method = 'linear',bounds_error=False,fill_value=None)[0])
         # Угол наклона вектора тяги, рад
         alpha = y[5] - y[1]
         # Правые части модели
         # dV / dt, м / сек^2
         self._dY[0] = (-self.__m * self.__g * np.sin(y[1]) + self.__P - 0.5 * (Coeff[0] + Coeff[1] * self.__delta_ZCP) * Ro * self.__S * y[0]**2) / self.__m 
         # dTheta / dt, рад / сек
         self._dY[1] = (-self.__m * self.__g * np.cos(y[1]) + self.__P * np.sin(alpha) + 0.5 * (Coeff[2] + Coeff[3] * self.__delta_RV + Coeff[4] * self.__delta_ZCP +  Coeff[5] * self.__delta_ZEL) * Ro * self.__S * y[0]**2) / (self.__m * y[0])
         # dX / dt, м / сек
         self._dY[2] = y[0] * np.cos(y[1])
         # dH / dt, м / сек
         self._dY[3] = y[0] * np.sin(y[1])
         # dOmegaZ / dt, рад / сек^2
         self._dY[4] = (0.5 * (Coeff[6] + Coeff[7] * self.__delta_RV + Coeff[8] * self.__delta_ZCP + Coeff[9] * self.__delta_ZEL) * Ro * self.__S * self.__B * y[0]**2) / self.__Jz
         # dPitch / dt, рад / сек
         self._dY[5] = y[4]
         return self._dY 
