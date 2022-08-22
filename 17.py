# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print('Assalomu aleykum!')
# salom_ber()


# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f'Assalomu aleykum hurmatli {ism.title()}!')
# salom_ber('BAHODIR')
# salom_ber('nargiza')
# print (salom_ber.__doc__)


# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ism va familiyasini jamlab
#     chiqaruvchi funksiya"""
#     print(f'Foydalanuvchi ismi: {ism.title()}\n'
#     f'Foydalanuvchi familiyasi: {familiya.title()}')
# toliq_ism('BAHODIR', 'boliev')


# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f'{ism.title()} ning yoshi {2022 - tugilgan_yil}da!')
# yosh_hisobla('BAHODIR', 1991)


# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f'{ism.title()} ning yoshi {2022 - tugilgan_yil}da!')
# yosh_hisobla(tugilgan_yil = 1991,ism = 'BAHODIR')


# def yosh_hisobla(tugilgan_yil, joriy_yil = 2022):
#     """Foydalanuvchi tug'ilgan yilidan uni yoshini hisoblaydi"""
#     print(f'Siz {joriy_yil - tugilgan_yil} yoshdasiz!')
# yosh_hisobla(1991, 2022)
# yosh_hisobla(1994)




# def tug_yil(ism,yosh):
#     """Foydalanuvchi tug'ilgan yilini hisoblaydigan dastur"""
#     print(f'{ism.title()} {2022 - yosh} yilda tugilgan!')
# tug_yil('bahodir',31)


# def kvadrat_kub(x):
#     """Sonning kvadrati va kubini hisoblaydigan dastur"""
#     print(f'{x} ning kvadrati {x**2} ga teng!\n'
#     f'{x} ning kubi esa {x**3} ga teng!')
# kvadrat_kub(7)


# def son(x):
#     """Son yo tog' yo jupligini aniqlaydigan dastur"""
#     if x%2==0:
#         print (f"{x}, bu jup son!")
#     else:
#         print (f"{x}, bu tog' son!")
# son(8)


# def sonlar(x,y):
#     """Sonlarning qaysi katta yo qaysi kichikligini aniqlaydigan dastur"""
#     if x>y:
#         print (f"{x} {y} dan katta!")
#     elif x<y:
#         print (f"{x} {y} dan kichik!")
#     else:
#         print ("Ushbu sonlar teng!")
# sonlar(8,7)
# sonlar(3,9)
# sonlar(27,27)


# def sonlar(x,y=2):
#     """x*y darajasini aniqlaydigan dastur"""
#     print (f"{x} ning {y} darajasi - {x**y} ga teng!")
# sonlar(8,7)
# sonlar(9,3)
# sonlar(6)


def son(x):
    """Sonning qoldiqsiz bo'linishini hisoblaydigan dastur"""
    for n in range (2,11):
        if not x%n:
            print (f"{x} {n} ga qoldiqsiz bo'linadi!")
son(7)
son(1)
son(2)
son(3)
son(20)
