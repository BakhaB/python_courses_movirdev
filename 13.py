# talaba_0 = {
# 'ism':'alijon',
# 'familiya':'shamsiev',
# 'yosh':22,
# 'fakultet':'matematika',
# 'kurs':4
# }
# print (talaba_0['ism'])
# print (talaba_0['yosh'])

# print (talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print (f"Kalit: {kalit}")
#     print (f"Qiymat: {qiymat}\n")



# telefonlar = {
# 'ali':'I phone x',
# 'vali':'galaxy s9',
# 'orif':'mi 10 pro',
# 'anvar':'pixel 3xl'
# }

# for k,q in telefonlar.items():
#     print (f"{k.title()}ning telefoni {q}")


# mahsulotlar = {
# 'olma':10000,
# 'anor':20000,
# 'uzum':40000,
# 'anjir':25000,
# 'shaftoli': 30000
# }
# print (mahsulotlar.keys())
# print (mahsulotlar.values())

# print ("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print (mahsulot.title())


# bozorlik = ['anor','non', 'uzum', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print (f"{mahsulot.title()}ning narhi {mahsulotlar[mahsulot]} so'm!")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print (f"Iltomos do'koningizga {buyum}ni olib keling!")


# print ("Do'konimizdagi mahsulotlar:\n")
# for mahsulot in sorted(mahsulotlar):
#     print (mahsulot.title())

# print ("Foydalanuvchilar quyidagi telefonlarni shlatadi:\n")
# for tel in telefonlar.values():
#     print (tel.title())

# telefonlar = {
# 'ali':'iphone x',
# 'vali':'galaxy s9',
# 'olim':'mi 10 pro',
# 'orif':'nokia 3310',
# 'hamida':'galaxy s9',
# 'maryam':'huawei p30',
# 'tohir':'iphone x',
# 'umar':'iphone x'
# }
# print ("Foydalanuvchilar quyidagi telefonlarni shlatadi:\n")
# for tel in set(telefonlar.values()):
#     print (tel.title())

# toys = {"ball","car","lamp","ball","bear","car"}
# print (toys)







# python = {'int':'integer',
# 'float':'decimal number',
# 'str':'string',
# 'for':'a type of condition',
# 'if':'another type of condition',
# 'tupel':'a list that can not be changed',
# 'set':'is to eliminate repeated word',
# 'title':'to upper a first letter'
# }
#
# for keys, values in sorted(python.items()):
#     print (f"{keys.title()} - {values}")



# countries = {'France':'Paris',
# 'Germany':'Berlin',
# 'Sweeden':'Stockholm',
# 'Denmark':'Copenagen',
# 'Spain':'Madrid',
# 'Uzbekistan':'Tashkent',
# 'Switzerland':'Bern',
# 'Belgium':'Bruxel'
# }
# print ("Davlatlarning ro'yhati:\n")
# for keys in sorted(countries):
#     print (f"{keys}")
#
# print ("\nDavlatlarning poytahtlari:\n")
# for poytaht in sorted(countries.values()):
#     print (f"{poytaht}")

# land = input ("What country capital you want to know? \n")
# print (f"The capital of  {land} is", countries.get(land,"Bizda bunday ma'lumot yo'q"))


# menu = {'Osh':35000,
# 'Manti':8000,
# 'Sho\'rvo':25000,
# 'Somsa':7000,
# 'Okroshka':20000,
# 'Kavob':30000,
# 'Shashlik':20000,
# 'kuksi':25000,
# 'Salat':16000,
# 'Halisa':40000
# }
# print(f"Please order 3 meals!\n")
# orders = []
# for n in range(3):
#     orders.append(input(f"{n+1} - meal! ").title())
#
# for order in orders:
#     if order in menu:
#         print (f"{order} {menu[order]} so'm")
#     else:
#         print (f"Kechirasiz, bizda {order} yo'q.")



# countries = {'France':'Paris',
# 'Germany':'Berlin',
# 'Sweeden':'Stockholm',
# 'Denmark':'Copenagen',
# 'Spain':'Madrid',
# 'Uzbekistan':'Tashkent',
# 'Switzerland':'Bern',
# 'Belgium':'Bruxel'
# }
# for land in sorted(countries):
#     print (land)
#
# for land in countries.values():
#     print (land)

# land =  (input("Write a country:\n"))
# capital = countries.get(land)
# if capital ==None:
#     print ("Bizda bunday ma'lumot yo'q")
# else:
#     print (f"{land} ning poytahti {capital} shahri")

#
# land = input ("What country capital you want to know? \n")
# print (f"The capital of  {land} is", countries.get(land,"Bizda bunday ma'lumot yo'q"))

menu = {'Osh':35000,
'Manti':8000,
'Sho\'rvo':25000,
'Somsa':7000,
'Okroshka':20000,
'Kavob':30000,
'Shashlik':20000,
'Kuksi':25000,
'Salat':16000,
'Halisa':40000
}

print (f"Please write 3 meals\n")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}").title())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print (f"The price of {buyurtma} is {menu[buyurtma]}")
    else:
        print ( "bizda bunday taom yo'q")
