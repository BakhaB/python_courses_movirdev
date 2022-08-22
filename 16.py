# ismlar = []
# n = 1
# while True:
#     savol = f'{n} - dostingizni ismini kiriting!\n'
#     ism = input (savol)
#     ismlar.append(ism)
#     repeat = input ('Yana ism kiritasizmi? (ha/yoq)\n')
#     n+=1
#     if repeat != 'ha':
#         break
# print ('Here the list of your friends:\n')
# for ism in ismlar:
#     print (ism.title())

# friends = {}
# ishora = True
# while ishora:
#     ism = input ("Do'stingizni ismini kiriting:\n")
#     yosh = input (f"{ism}ning yoshini kiriting:\n")
#     friends [ism] = int(yosh)
#
#     repeat = input ("Yanado'stingiz borma? (ha/yoq)")
#     if repeat == 'yoq':
#         ishora = False
#
# for ism, yosh in friends.items():
#     print (f"{ism.title()} {yosh} yoshida")


# cars = ['BMW', 'Mrecedes', 'BMW', 'lecetti', 'TOYOTA', 'BMW', 'Audi']
# cars.remove('BMW')
# print (cars)
# cars = ['BMW', 'Mrecedes', 'BMW', 'lecetti', 'TOYOTA', 'BMW', 'Audi']
# while 'BMW' in cars:
#     cars.remove('BMW')
# print (cars)
#
# cars = ['BMW', 'Mrecedes', 'BMW', 'lecetti', 'TOYOTA', 'BMW', 'Audi']
# car = 'BMW'
# while car in cars:
#     cars.remove('BMW')
# print (cars)

# students = ['hasan', 'husan', 'olim', 'zolim']
# ranked_students = {}
# while students:
#     student = students.pop()
#     mark = input (f"Please put a mark of {student.title()}: \n")
#     print (f"{student.title()} got a mark!")
#     ranked_students[student] = int(mark)

# orders = []
# n = 1
# while True:
#     question ='Please write the name of the meal: \n'
#     meal = input (question)
#     orders.append(meal)
#     repeat = input ('More meals? (yes/no)')
#     n=+1
#     if repeat != 'yes':
#         break
# print("Here the list of your meals:\n")
# for meal in orders:
#     print (meal.title())
#
# ebozor = {}
# ishora = True
# while ishora:
#     mahsulotlar = input ("Write the food: \n")
#     narh = input ("Write the price: \n")
#     ebozor[mahsulotlar] = float(narh)
#     repeat = input('Any other food? (yes/no)')
#     if repeat == 'no':
#         ishora = False
# print ("Here the list of your food with the prices: \n")
# for mahsulotlar, narh in ebozor.items():
#     print (f"The price of {mahsulotlar.title()} is {narh} USD!")


ebozor = {'alma': 25, 'nok': 10, 'non': 5, 'asal': 55}
orders = ['alma', 'asal', 'osh', 'posh']

while orders:
    order = orders.pop()
    if order in ebozor.keys():
        narh = ebozor[order]
        print(f"The price of {order.title()} is {narh} USD")
    else:
        print (f"We do not have {order.title()}!")
