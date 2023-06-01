# Даны значения величины заработной платы заемщиков банка (zp) и значения 
# их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, 
# а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных 
# отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import pandas as pd
import numpy as np


zp  = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 83])

cov1 = np.mean(zp*ks) - np.mean(zp) * np.mean(ks)
print ('cov1 =', cov1)

cov2 = np.cov(zp, ks, ddof = 0)
print ('cov2 =', cov2)

corr1 = cov1 / (np.std(zp) * np.std(ks))
print ('corr1 =', corr1)

corr2 = np.corrcoef(zp, ks)
print ('corr2 =', corr2)

df = pd.DataFrame(zp)
df['zp'] = pd.DataFrame(zp)
X = df['zp']

df = pd.DataFrame(ks)
df['ks'] = pd.DataFrame(ks)
Y = df['ks']
print('corr3 =', X. corr(Y))

