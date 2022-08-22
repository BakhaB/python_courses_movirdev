# *args

# def summa (*sonlar):
#     """Kiritilgan sonlarning yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
#
# print (summa(1,2))
# print (summa(1,2,3,4,5))
# print (summa(4,5,6,7))
# print (summa(125,-89,-968,1025))


# def summa (x,y,*sonlar):
#     """Kiritilgan sonlarning yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print (summa(1,2))
# print (summa(1,2,3,4,5))
# print (summa(4,5,6,7))
# print (summa(125,-89,-968,1025))
# # print (summa(2))



# **kwargs keywords
# def avto_info (kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at kurinishida qaytaruvchi funksiya"""
#     malumotlar ['kompaniya'] = kompaniya
#     malumotlar ['model'] = model
#     return malumotlar
#
# avto1 = avto_info('GM', 'Malibu', rang = 'qora', yil = 2018)
# avto2 = avto_info('Kia', 'K5', rang = 'qizil', yil = 2020, narh = 35000)
# print (avto1)
# print (avto2)


# def multiplication (*numbers):
#     x=1
#     for number in numbers:
#         x*=number
#     return x
# print (multiplication(1,5,8))
# print (multiplication(5,-4,6))
# print (multiplication(5,-4))


# def talabalar (ism, familiya, **malumotlar):
#     malumotlar ['ism'] = ism
#     malumotlar ['familiya'] = familiya
#     return malumotlar
# talaba1 = talabalar ('Hasan', 'Molov', yil = 1992, bahosi = 4)
# talaba2 = talabalar ('Olim', 'Kirov', yil = 1993, bahosi = 3)
# talaba3 = talabalar ('Vali', 'Turonov', yil = 1991, bahosi = 5, pul = 'yoq')
# talaba4 = talabalar ('Magamed', 'Ozdoev', yil = 1990, bahosi = 2, pul = 'bor')
#
# print (talaba1)
# print (talaba2)
# print (talaba3)
# print (talaba4)


def talaba_info (ism, familiya, **kwargs):
    kwargs ['ism'] = ism
    kwargs ['familiya'] = familiya
    return kwargs
talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')
print (talaba)
