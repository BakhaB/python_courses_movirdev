# ism = input ("What is your name? \n")
# savol = f"Salom {ism.title()}. How old are you?\n"
# yosh = input(savol)
# yosh = int(yosh)
# height = input ("What is your height?\n")
# height = float (height)

# son = 1
# while son<=5:
#     print (son, end= ' ' )
#     son +=1
# print ("Dastur tugadi")

# print ("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol= "Istalgan son kiriting "
# savol += "( dasturni toxtatish uchun 'exit' deb yozing): \n"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print (f"{float(qiymat)} ning kvadrati {float(qiymat)**2} ga teng!")
# print ("Dastur tugadi!")


# print ("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol= "Istalgan son kiriting "
# savol += "( dasturni toxtatish uchun 'exit' deb yozing): \n"
# ishora = True
#
# while ishora:
#     qiymat = input (savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print (int (qiymat) **2)
# print ("Dastur tugadi!")

# print ("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol= "Istalgan son kiriting "
# savol += "( dasturni toxtatish uchun 'exit' deb yozing): \n"
# while True:
#     qiymat = input (savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print (float(qiymat)**2)
# print ("Dastur tugadi!")

# sonlar = list (range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print (f"{son} ning kvadrati {son**2} ga teng")
# sonlar = list (range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print (f"{son} ning kvadrati {son**2} ga teng")


# son = 0
# while son < 10:
#     son+=1
#     if son%2 !=0:
#         continue
#     else:
#         print (son)
# son = 0
# while son < 10:
#     son+=1
#     if son%2 ==0:
#         continue
#     else:
#         print (son)


# savol = "Please write your favourite books:\n"
# savol += "(Write 'stop' after adding all books): "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input (savol)
#     if qiymat == 'stop':
#         break
#
# print ("The end of the program!")

# savol = "What is your age?\n"
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or 'quit':
#         break
#     yosh = int(qiymat)
#
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
#
#     if narh == 0:
#         print ("free of charge")
#     else:
#         print (f"Chipta {narh} so'm")


# savol = 'Your favourite book'
# savol += ' (please enter "stop" if there is no more books!):\n'
# qiymat = ''
# qiymat = input (savol)
# while qiymat != 'stop':
#     qiymat = input(savol)
# else:
#     print ('The project is over!')


# savol = 'Your age'
# savol += ' (please enter "exit" or "quit" after!):\n'
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat =='quit':
#         break
#     age = int(qiymat)
#     if age <7:
#         price = 2000
#     elif 7<age<18:
#         price = 3000
#     elif 18<age<65:
#         price = 10000
#     else:
#         price = 0
#     if price == 0:
#         print ('The entrance for you is free!')
#     else:
#         print (f"The ticket costs {price} so'm")
# print ('The program is over')



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("The program is over")
