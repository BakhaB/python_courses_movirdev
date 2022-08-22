fruit = ["olma", "anjir", "shaftoli", "o'rik"]
prices = [12000, 18000, -25, 36.6]
sonlar = ["bir", "ikki", "uch", 4, 5, 6]
# ismlar = []

# print (fruit)
# print (prices)
# print (sonlar)
# print (ismlar)
# print (fruit[0])
# print (fruit[3])
# print (fruit[-1])
# print (fruit[0].upper())
# print (fruit[0].title())
# print (fruit[0].capitalize())
# print (prices[0] + prices[1])
# fruit[0]="anor"
# print (fruit[0])
# print (fruit)

# fruit.append("tarvuz")
# fruit.append("uzum")
# fruit.insert(0,"banan")
# fruit.insert(3,"ananas")

# cars = []
# cars.append("Lacetti")
# cars.append ("Nexia")
# cars.append("Malibu")
# cars.append("Tracker")

# print (cars)

# del cars [0]
# cars.insert(0, "Tico")
# del cars[1]
#
# cars.remove("Malibu")
#
# print (cars)

# animals = ["it", "mushuk", "sigir", "qo'y", "quyon", "mushuk"]
# animals.remove("mushuk")
# print (animals)

# bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
# mahsulot = bozorlik.pop(1)
# print ("Men" + " " + mahsulot + " " + "sotib oldim")
# print ("Olinmagan mahsulotlar: ", bozorlik)


# bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
# mahsulot2 = bozorlik.pop()
# print (mahsulot2)

# prices.remove(12000)
# prices[0] = prices[0] + 2000
# print (prices)

# ismlar = ["Sonik", "Te", "Shahboz"]
# print (f"{ismlar[1]} va {ismlar[2]} do'st")
# print ("Salom"+" "+ ismlar[0]+","+" "+"bugun choyhona bormi?")


# sonlar = [7 , -5 , 3.3, 286]
# # sonlar[0] = sonlar[0] + 5
# sonlar.append(-96)
# sonlar.insert(2,87)
# print (sonlar)


# t_s = ["Tamerlan", "Manguberdi"]
# z_s = ["Rooney", "Depp"]
# t_s = t_s.pop(0)
# z_s = z_s.pop(0)
# print ("Men tarixiy shahslardan", t_s, "bilan, zamonaviy shahslardan esa", z_s, "bilan suhbat qilishni istar edim")

friends = []
friends.append("Sonik")
friends.append("Te")
friends.append("Shahboz")
friends.append("Mura")
friends.remove("Mura")
friends.insert(0, "Uktam")
friends.insert(2,"Lenin")
friends.insert(5, "G'ani")
# print (friends)

guests = []
guests.append(friends.pop(3))
guests.append(friends.pop(0))
guests.append(friends.pop(-1))
print ("\nKelgan mehmonlar: ", guests)
