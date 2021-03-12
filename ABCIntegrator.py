# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:58:36 2021

@author: Павел Ермаков / Дмитрий Гиренко
"""
from abc import ABCMeta, abstractmethod
from ABCMathModel import ABCMathModel
import numpy as np
class ABCIntegrator():
    __metaclass__=ABCMeta
    def __init__(self, initTime, initY, TEnd, Tau):
        self._t = initTime
        self._y = initY
        self.__tEnd = TEnd
        self._tau = Tau
        # Списки времени моделирования и значений функции
        self.__time = []
        self.__Y = []
        self.__time.append(self._t)
        self.__Y.append(self._y)
        
    @abstractmethod
    def _increment_(self, ABCMathModel):
        pass
    
    def Run(self, ABCMathModel):
         while self._t < self.__tEnd:
                  # Расчет значения функции
                  self._y = self._y + self._increment_(ABCMathModel)
                  # Приращение времени
                  self._t = self._t + self._tau 
                  # Заполнение массива времени и значений функции
                  self.__time.append(self._t) 
                  self.__Y.append(self._y)       
         return np.array(self.__time), np.array(self.__Y)