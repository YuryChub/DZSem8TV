# 2) Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np

IQ = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
sumIQ = sum(IQ)
meanIQ = sumIQ/len(IQ)
sumprestdIQ = 0
for i in range(len(IQ)):
    prestdIQ = (IQ[i] - meanIQ)
    sumprestdIQ = sumprestdIQ + prestdIQ**2
    stdIQ = (sumprestdIQ/(len(IQ)-1))**0.5
t = 2.26215716274 # по таблице Стьюдента для Объема выборки 10 - 1 = 9,
# и доверительной вероятности 0,95

print('Доверительный интервал')
print(meanIQ - t * stdIQ / np.sqrt(len(IQ)), meanIQ + t * stdIQ / np.sqrt(len(IQ)))
