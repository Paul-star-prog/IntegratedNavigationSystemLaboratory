# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:30:11 2021

@author: Павел Ермаков / Дмитрий Гиренко
"""
from ABCIntegrator import ABCIntegrator
class RungeKutt4(ABCIntegrator):
    """
    Класс,реализующий численное интегрирование методом Рунге-Кутты 4
    """
    def __init__(self,initTime, initY, TEnd, Tau):
        ABCIntegrator.__init__(self,initTime, initY, TEnd, Tau) 
    def _increment_(self, ABCMathModel):
        k1 = ABCMathModel.RightPart(self._t, self._y)
        k2 = ABCMathModel.RightPart(self._t + 0.5 * self._tau, self._y + 0.5 * k1 * self._tau)
        k3 = ABCMathModel.RightPart(self._t + 0.5 * self._tau, self._y + 0.5 * k2 * self._tau)
        k4 = ABCMathModel.RightPart(self._t + self._tau, self._y + k3 * self._tau)
        return (k1 + 2 * k2 + 2 * k3 + k4) * self._tau / 6     