# def toliq_ism_yasa (ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     print (toliq_ism)
# toliq_ism_yasa ('bahodir', 'boliev')


# def toliq_ism_yasa (ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa ('bahodir', 'boliev')
# talaba2 = toliq_ism_yasa ('olim', 'hakimov')
#
# print (f"Darsga {talaba1} va {talaba2} kelishmadi!")
# print (f'{talaba1} darsga kechikib keldi!')


# def toliq_ism_yasa (ism, familiya, otasining_ismi = ''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa ('bahodir', 'boliev', 'bahriddin ugli')
# talaba2 = toliq_ism_yasa ('olim', 'hakimov')
#
# print (f"Darsga kelmagan talabalar: {talaba1} va {talaba2} !")
# print (f'{talaba1} darsga kechikib keldi!')


# def avto_info (kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'korobka': korobka,
#             'yil': yili,
#             'narh': narhi}
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'Oq', 'Avtomat', 2022)
# avto2 = avto_info('GM', 'Gentra', 'Qora', 'Mexanika', 2021, 14000)
# avtolar = [avto1, avto2]
# print ("Online bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto ['narh']:
#         narh = avto ['narh']
#     else:
#         narh = 'Nomalum'
#     print (f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# def oraliq (min, max, qadam = ''):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 2
#     return sonlar
# print (oraliq(0,10,2))
# print (oraliq(10,21))


# def avto_info (kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'korobka': korobka,
#             'yil': yili,
#             'narh': narhi}
#     return avto
# print ("Saytimizdagi avtolar ruyhatini shakillantiramiz:")
# avtolar = []
# while True:
#     print ("\nQuyidagi ma'lumotlarni kiriting", end = '')
#     kompaniya = input ("Ishlab chiqaruvchi: ")
#     model = input ("Modeli: ")
#     rangi = input ("Rangi: ")
#     korobka = input ("Korobka: ")
#     yili = input ("Ishlab chiqarilgan yili: ")
#     narhi = input ("Narhi: ")
#
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input ("Yana avto qushasizmi? (yes/no): ")
#     if javob  == 'no':
#         break
# print ("\nSalonimizdagi avtolar: ")
# for avto in avtolar:
#     if avto ['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print (f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")







# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz
#
# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
#
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")


def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

kattasi(10,20,-5)
print (max)
