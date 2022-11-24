# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:32:59 2021

@author: Павел Ермаков
"""

from abc import ABCMeta, abstractmethod
import numpy as np
class ABCMathModel():
    __metaclass__=ABCMeta
    def __init__(self):
       self._dY = np.zeros(0)
    @abstractmethod
    def RightPart(self, t, y):
        pass
