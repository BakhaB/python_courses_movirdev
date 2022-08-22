# son = -72
# if son<0:
#     print ("Manfiy son!")
# else:
#     print ("Musbat son!")

# yosh = int(input("Yoshingiz nechida?\n"))
# if yosh<=4:
#     print ("Sizga kirish bepul!")
# elif yosh<=12:
#     print ("Sizga kirish 5000 so\'m!")
# elif yosh<=18:
#     print ("Sizga kirish 8000 so\'m!")
# else:
#     print ("Sizga kirish 10000 so\'m!")


# yosh = int(input("Yoshingiz nechida?\n"))
# if yosh<=4:
#     narh =0
# elif yosh<=12:
#     narh =5000
# elif yosh<=18:
#     narh =8000
# else:
#     narh =10000
# print (f"Sizga kirish {narh} so\'m!")


# kun = input("Bugun kun nima?\n")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print ("Bugun dam olish kuni!")
# else:
#     print ("Bugun ish kuni")

# kun = input("Bugun kun nima?\n")
# harorat = float(input("Havo harorati qanday?\n"))
#
# if kun.lower() == "yakshanba" and harorat>=30:
#     print ("Cho'milgani ketdik!")
# elif kun.lower() == "yakshanba" and harorat<30:
#     print ("Uyda dam olamiz!")
# else:
#     print ("Uzur, bugin ishga!")


# kun = input("Bugun kun nima?\n")
# harorat = float(input("Havo harorati qanday?\n"))
#
# if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
#     print ("Cho'milgani ketdik!")
# elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
#     print ("Uyda dam olamiz!")
# else:
#     print ("Uzur, bugin ishga!")

# narh = 15000
# choy = True
# salat = False
#
# if choy and salat: # BOOLEAN
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
# print (f"Jami {narh} so'm")


# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
#
# if choy:
#     print ("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print ("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print ("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print ("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print ("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print (f"Mijoz {narh} ga narsa oldi!")


# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1
#
# if choy:
#     print ("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print ("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print ("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print ("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print ("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print (f"Mijoz {narh} ga narsa oldi!")

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# print ("manti" in menu) # Menuda manti bormi?
# print ("somsa" in menu)

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yiysiz?\n")
# if ovqat.lower() in menu:
#     print ("Buyurtma qabul qilindi")
# else:
#     print ("Bu ovqat menuda yoq")


# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yiysiz?\n")
# if ovqat.lower() not in menu:
#     print ("Bu ovqat menuda yoq")
# else:
#     print ("Buyurtma qabul qilindi")


# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
# for taom in buyurtmalar:
#     if taom.lower() in menu:
#         print (f"Menuda {taom} bor")
#     else:
#         print (f"Kechirasiz, menuda {taom} yoq")

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# buyurtmalar = []
# if buyurtmalar:
#     print (f"ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print ("Ro'yxat bo'sh!")
# for taom in buyurtmalar:
#     if taom.lower() in menu:
#         print (f"Menuda {taom} bor")
#     else:
#         print (f"Kechirasiz, menuda {taom} yoq")

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
# if buyurtmalar: # Ro'xatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom.lower() in menu:
#             print (f"Menuda {taom} bor")
#         else:
#             print (f"Kechirasiz, menuda {taom} yoq")




# son = int(input("Iltimos juft son kiriting\n"))
# if son%2==0:
#     print ("Rahmat")
# else:
#     print ("Bu son juft emas")


# yosh = int(input("Iltimos yoshingizni kiriting\n"))
# if yosh<4 or yosh>60:
#     print ("Tekin")
# elif yosh<18:
#     print ("10000 so'm")
# elif yosh>18:
#     print ("20000 so'm")

# son1 = int(input("Birinchi sonni kiriting\n"))
# son2 = int(input("Ikkinchi sonni kiriting\n"))
#
# if son1>son2:
#     print ("Son 1 kattaroq")
# elif son1<son2:
#     print ("Son 2 kattaroq ekan")
# else:
#     print ("Ikkiviyam teng ekan")


# mahsulotlar = ["non", "tuz", "shakar", "tort", "pomidor", "un", "sabz", "anor", "alma", "banan"]
# savat = []
# for n in range(5):
#     savat.append(input("5 mahsulot kiriting\n"))
# print (savat)
#
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print (f"{mahsulot} do'konimizda bor")
#     else:
#         print (f"{mahsulot} do'konimizda yo'q")

# mahsulotlar = ["non", "tuz", "shakar", "tort", "pomidor", "un", "sabz", "anor", "alma", "banan"]
# savat = []
#
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} mahsulotlarni kiriting\n"))
# mavjud_emas = []
# bor_mahsulotlar = []
#
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#             bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#         print (f"Quyidagi mahsulotlar do'konimizda yo'q")
#         for mahsulot in mavjud_emas:
#             print (mahsulot)
# else:
#     print ("Siz so'ragan barcha mahsulotlar do'konimizda bor")




# foydalanuvchilar = ["Gblfhfp007", "gblfhfp007", "Gblfhfp008", "gblfhfp008", "Gblfhfp009", "gblfhfp009"]
# yangi = input ("Please input your login:\n")
# if yangi in foydalanuvchilar:
#     print ("Login band, yangi login tanlang!")
# else:
#     print ("Xush kelibsiz, foydalanuvchi!")


# son = int(input ("Please input the number:\n"))
# for n in range(2,11):
#     if not (son%n):
#         print (f"{son} soni {n} ga qoldiqsiz bo'linadi")




# mahsulotlar = ["non", "tuz", "shakar", "tort", "pomidor", "un", "sabz", "anor", "alma", "banan"]
# savat  = []
# for mahsulot in range(5):
#     savat.append(input("5 mahsulotni kiriting:\n"))
# print (savat)
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print (f"{mahsulot} do'konimizda bor")
#     else:
#         print (f"{mahsulot} do'konimizda yo'q")


mahsulotlar = ["non", "tuz", "shakar", "tort", "pomidor", "un", "sabz", "anor", "alma", "banan"]
savat  = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} mahsulotni kiriting:\n"))

bor_mahsulotlar = []
mavjud_emas = []

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print (f"Quyidagi mahsulotlar do'konimizda yo'q: ")
    for mahsulot in mavjud_emas:
        print (mahsulot)
    
else:
    print ("Siz so'ragan barcha mahsulotlar do'konimizda bor" )
