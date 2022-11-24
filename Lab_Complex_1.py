# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:53:46 2021

@author: Павел Ермаков
"""
import numpy as np
import matplotlib.pyplot as plt
from RungeKutt4 import RungeKutt4
from AirfoilBoatModel import AirfoilBoatModel

model = AirfoilBoatModel()
# начальные условия
yo = np.array([40.8, 0., 0., 1.568, 0., 0.10821032])
integrator = RungeKutt4(0, yo, 500, 1e-1)
t, y = integrator.Run(model)
# Визуализация 
# График скорости экраноплана
plt.plot(t, y[:,0], linewidth=2)
plt.title("Зависимость скорости экраноплана от времени")
plt.xlabel('Время t, с')
plt.ylabel('Скорость V, м/с')
plt.show()
# График скорости экраноплана
plt.plot(t, y[:,1] * 180 / np.pi, linewidth=2)
plt.title("Зависимость угла наклона траектории экраноплана от времени")
plt.xlabel('Время t, с')
plt.ylabel('Угол наклона траектории Theta, град')
plt.show()
# График высоты экраноплана
plt.plot(t, y[:,3], linewidth=2)
plt.title("Зависимость высоты экраноплана от времени")
plt.xlabel('Время t, с')
plt.ylabel('Высота H, м')
plt.show()
# График угла тангажа экраноплана
plt.plot(t, y[:,5] * 180 / np.pi, linewidth=2)
plt.title("Зависимость угла тангажа экраноплана от времени")
plt.xlabel('Время t, с')
plt.ylabel('Угол тангажа экранопалана, град')
plt.show()
