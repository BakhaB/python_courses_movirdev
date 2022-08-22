# car0 = {
# 'model':'lacetti',
# 'rang':'oq',
# 'yil':2018,
# 'narhi':13000,
# 'km':50000,
# 'korobka':'avtomat'
# }
#
# car1 = {
# 'model':'nexia 3',
# 'rang':'qora',
# 'yil':2015,
# 'narhi':9000,
# 'km': 89000,
# 'korobka':'mexanika'
# }
#
# car2 = {
# 'model':'gentra',
# 'rang':'qizil',
# 'yil':2019,
# 'narhi':15000,
# 'km':20000,
# 'korobka':'mexanika'
# }

# car = car0
# print (f"{car['model'].title()}, "
# f"{car['rang']} rang, "
# f"{car['yil']} - yil, {car['narhi']} $" )
#
# car = car1
# print (f"{car['model'].title()}, "
# f"{car['rang']} rang, "
# f"{car['yil']} - yil, {car['narhi']} $" )
#
# car = car2
# print (f"{car['model'].title()}, "
# f"{car['rang']} rang, "
# f"{car['yil']} - yil, {car['narhi']} $" )


# cars = [car0, car1, car2]
# print (type(cars))
# for car in cars:
#     print (f"{car['model'].title()}, "
#             f"{car['rang']} rang, "
#             f"{car['yil']} - yil, "
#             f"{car['narhi']}$")


# print (cars[0]['rang'])
# print (cars[1]['rang'])

# print (type(cars))
# for car in cars:
#     print (f"{car['rang'].title()} "
#             f"{car['model']}")


# malibus=[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang': None, # rangi noaniq
#         'yil': 2022,
#         'narh': None,
#         'km': 0,
#         'korobka': 'avto'
#         }
#     malibus.append(new_car)
#
# for malibu in malibus[:3]:
    # malibu['rang'] = 'qizil'
# for malibu in malibus:
#     print (malibu)
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
# for malibu in malibus:
#     print (malibu)
# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq'
#     malibu['korobka'] = 'mexanika'
# for malibu in malibus:
#     print (malibu)

# for malibu in malibus:
#     if malibu ['korobka'] == 'avto':
#         malibu ['narh'] = 40000
#     else:
#         malibu ['narh'] = 35000
# for malibu in malibus:
#     print (malibu)



# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css','js'],
#     'hasan':['php', 'sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
# }
# for ism, tillar in dasturchilar.items():
#     print (f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
#     for til in tillar:
#         print (til.upper())


# for ism, tillar in dasturchilar.items():
#     print (f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
#     for til in tillar:
#         print (f"{til.upper()} ",  end='')


# hamkasblar = {
# 'ali':{'familiya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python','c++']
#         },
# 'vali':{'familiya':'aliyev',
#         'tyil':2001,
#         'malumot':"o'rta-maxsus",
#         'tillar':['html','css','js']
#         },
# 'hasan':{'familiya':'husanov',
#         'tyil':1999,
#         'malumot':'maxsus',
#         'tillar':['python','php']},
# }
#
# for ism, info in hamkasblar.items():
#     print (f"\n{ism.title()}  {info['familiya'].title()}",
#     f"{info['tyil']} - yilda tug'ilgan. "
#     f"Ma'lumoti:{info['malumot']}.\n"
#     "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print (til.upper())



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#
#            }
#
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon","Obid ketmon"]
#            }
#
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }
#
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
#
# olimlar = [buxoriy,qodiriy,vohidov,navoiy]
# for olim in olimlar:
#     ism = olim['ism']
#     tyil = olim['tyil']
#     vyil = olim['vyil']
#     tjoy = olim['tjoy']
#     asarlar = olim ['asarlar']
#
#     print (f"\n{ism} quydagi asarlarni yozgan: ")
#     for asar in asarlar:
#         print (asar)


# films = {'Sonik':['Rock and Roll', 'Fast and furious', 'Me and Me'],
#            'Te':['Zero', 'Il est null', '47 Ronins'],
#            'Monik':['Sony Kage', 'Minimonik', 'Seven Eleven']
#           }
# for name, film in films.items():
#     print (f"\n{name} ning sevimli kinolari: ")
#     for fil in film:
#         print (fil)



# Davlat = {
# "O'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"},
# "USA":{'poytaxt':"washington",
#                    'maydon':448978*4,
#                    'aholi':300_000_000,
#                    'pul birligi':"USD"},
# "France":{'poytaxt':"paris",
#                    'maydon':448978*1.5,
#                    'aholi':80_000_000,
#                    'pul birligi':"Euro"}
# }
# country = input ('Enter a country:\n').upper()
# if country in Davlat:
#     info = Davlat[country]
#     print (f"\n{country.title()}ning poytahti {info['poytaxt'].title()}.",
#     f"{country.title()} ning maydoni va aholisi {info['maydon']} va {info['aholi']}.",
#     f"Shuningdek pul birligi {info['pul birligi']}.")
# else:
#     print ("Bizda bu davlat haqida ma'lumot yo'q" )

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#
#            }
#
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon","Obid ketmon"]
#            }
#
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }
#
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# olimlar = [buxoriy, qodiriy, vohidov, navoiy]
# for olim in olimlar:
#     print (f"\n{olim ['ism']} {olim['tyil']} yilda {olim['tjoy']} shahrida tug'ilgan, va {olim['vyil']} yilda vafot etgan.")

# olimlar = [buxoriy, qodiriy, vohidov, navoiy]
# for olim in olimlar:
#     ism = olim['ism']
#     asarlar = olim['asarlar']
#     print (f"\n{ism} quyidagi asarlarni yozgan:\n")
#     for asar in asarlar:
#         print (asar.upper())

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#             }
# for name, info in kinolar.items():
#     print (f"\n{name.title()}ning sevimli kinolari:")
#     for film in info:
#         print (film)



Davlatlar = {
"o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"},
"usa":{'poytaxt':"washington",
                   'maydon':448978*4,
                   'aholi':300_000_000,
                   'pul birligi':"USD"},
"france":{'poytaxt':"paris",
                   'maydon':448978*1.5,
                   'aholi':80_000_000,
                   'pul birligi':"Euro"}
}
land = input ("Please enter a country:\n").lower()
if land in Davlatlar:
    info = Davlatlar[land]
    print (f"\n{land.capitalize()} ning poytahti {info['poytaxt'].title()}. Va qolgan ma'lumotlar:"
    f"\nMaydoni - {info['maydon']};"
    f"\nAholisi - {info['aholi']};"
    f"\n Pul birligi - {info['pul birligi']}.")
else:
    print ("Bizda bu davlat haqida ma'lumot yo'q" )
