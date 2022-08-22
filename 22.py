# Lyambda funksiya
#
# import math
# lambda argument:ifoda

# uzunlik = lambda pi, r : 2*pi*r
# print (uzunlik(math.pi,10))


# kvadrat = lambda x,y:x**y
# print (kvadrat(2,3))

#
# def daraja(n):
#     return lambda x : x**n
# print (daraja(3))
# kvadrat = daraja(2)
# print (kvadrat(14))
# kub = daraja(3)
# print (kub(14))
# print (kub(5))
# print (f"3 ning kvadrati {kvadrat(3)} ga, kubi esa {kub(3)} ga teng!")


# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print (ildizlar)

# Тоже самое можно написать следующим образом!!!
# ildizlar = []
# for son in sonlar:
#     ildizlar.append(sqrt(son))
# print (ildizlar)

# def daraja2(x):
#     return x*x
# print (list(map(daraja2,sonlar)))

# Тоже самое можно написать следующим образом!!!
# kvadratlar = list (map(lambda x:x*x,sonlar))
# print (kvadratlar)
# Тоже самое можно написать следующим образом!!!

# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print (kvadratlar)


# a = [4,5,6]
# b = [7,8,9]
# a_plus_b = list(map(lambda x,y: x+y,a,b))
# print (a_plus_b)

import random as r
# sonlar = r.sample(range(100),10)
# print (sonlar)
# def juftmi(x):
#     """x juft bo'lsa TRUE, aks holda FALSE qaytaruvchi funksiya"""
#     return x%2==0
#
# juft_sonlar = list(filter(juftmi,sonlar))
# print (juft_sonlar)


# Тоже самое можно написать следующим образом!!!
# juft_sonlar = list(filter(lambda x:x%2==0,sonlar))
# print (juft_sonlar)



mevalar = ['olma','anor','anjir','shaftoli',"o'rik", 'tarvuz', 'qovun', 'banan']
# harf = 'o'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
# print (mevalar_b)
mevalar2 = list(filter(lambda meva:len(meva)<=5,mevalar))
print (mevalar2)
