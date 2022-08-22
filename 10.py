# cars = ["audi", "bmw", "volvo", "kia", "hyndai"]
# for auto in cars:
#     print (auto.title())

# cars = ["audi", "bmw", "volvo", "kia", "hyndai"]
# for auto in cars:
#     if auto == "bmw":
#         print (auto.upper())
#     else:
#         print (auto.title())


# name = input ("What is your name?\n")
# if name.lower() != "ali":
#     print (f"Uzr, {name.title()} biz Alini kutayapmiz.")
# else:
#     print ("Hi Ali")


# javob = float (input ("12*6 nechiga teng\n"))
#
# if javob != 72:
#     print ("Javob xato")


# Yosh = int(input ("How olda are you?\n"))
# if Yosh>=18:
#     print ("Welcome")
# else:
#     print ("Content is 18+")


# login = input ("Yangi login tanlang:\n")
# if len(login)<=5:
#     print ("Login 5 harftan ko'proq bo'lishi shart!")


# yil = int(input("Tug'ulgan yilingizni yozing:\n"))
# if 2022-yil<18:
#     print (f"Yoshingiz {2022-yil} ekan!")
#     print ("Kirish mumkin emas")
# else:
#     print("Welcome!")

# yosh = int(input("Yoshingiz nechida?\n"))
# if yosh>65: print ("Siz COVID-19 risk guruhida ekansiz")


# x,y = 225,50
# print ("x>y") if x>y else print ("y>x")


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for n in cars:
#     if n=="gm":
#         print (n.upper())
#     else:
#         print (n.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for n in cars:
#     if n!="gm":
#         print (n.title())
#     else:
#         print (n.upper())


# name = input ("Ismingiz?\n")
# if name.lower() == "admin":
#     print ("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print (f"Xush kelibsiz {name}")

# number1 = float(input("Biinchi sonni kiriting:\n"))
# number2 = float(input("Ikkinchi sonni kiriting:\n"))
# if number1==number2:
#     print (f"Sonlar teng! {number1}={number2}")

# number = float(input("Istalgan sonni kiriting:\n"))
# if number>0:
#     print ("Bu Musbat son!")
# else:
#     print ("Bu Manfiy son!")

number = int(input("Istalgan sonni kiriting:\n"))
if number>0:
    print (f"Sonning ildizi {number**(1/2)}!")
else:
    print ("Musbat son kiriting!")
