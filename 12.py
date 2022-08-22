# car_0 = {"model": "ferrari", "rang":"qizil"}
# print (car_0["model"])
# print (car_0["rang"])

# en_uz = {"apple":"alma","apricot":"o'rik","banana":"banan"}
# # print (en_uz)
# print (en_uz["apple"])

# mevalar = {"alma":10000,"tarvuz":8000,"qovun":10000}
# print (f"alma narhi {mevalar['alma']} so'm")
# print (mevalar['qovun'])

# talaba_0 = {"ism":"Bahodir Boliev","yosh":"31","yil":"1991"}
# print (f"{talaba_0['ism']},\
# {talaba_0['yosh']} yoshda,\
# {talaba_0['yil']} yilda tug'ulgan")


# talaba_0 = {"ism":"Bahodir Boliev","yosh":"31","yil":"1991"}
# print (f"{talaba_0['ism']},\
# {talaba_0['yosh']} yoshda,\
# {talaba_0['yil']} yilda tug'ulgan")
# talaba_0 ['kurs'] = 4
# talaba_0 ['fakultet'] = 'IT'
# talaba_0 ['ism'] = "Rafik"
# print (talaba_0)

# talaba_1 = {}
#
# talaba_1 ['ism'] = "Rafik"
# talaba_1 ['kurs'] = 3
# talaba_1 ['yosh'] = 20
#
# talaba_1['kurs'] = 4
# print (talaba_1)
# print (f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kursda o'qiydi!")

# del talaba_0['yosh']
# print (talaba_0)

# telefonlar = {
# 'ali':'I phone x',
# 'vali':'galaxy s9',
# 'orif':'mi 10 pro',
# 'anvar':'pixel 3xl'
# }
# print (telefonlar['orif'])

# phone = telefonlar.get('ali', 'Bunday ism mavjud emas!')
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas!')


# meva = en_uz.get('pine-apple', 'Bunday meva mavjud emas!')
# print (meva)
# phone = telefonlar.get('hasan')
# print (phone)



# Otam = {'ism':'Bahriddin', 'yil':1967, 'shahar':'Navoi','yosh':55}
# print (f"Otamning ismi {Otam['ism']}, {Otam['yil']}-yilda, {Otam['shahar']} viloyatida tug'ilgan.\
# Hozirda yoshlari {Otam ['yosh']} da.")

# I_T = {'Bahodir':'Manti', 'Guli':'Kavob', 'Onam':'Shurpa','Dadam':'Kulchatoy', 'Asal':'qand'}
# print (f"Dadamning sevimli taomi {I_T['Dadam']}, Onamning sevimli taomi {I_T['Onam']}, Gilining sevimli taomi {I_T['Guli']}.")

# taom = {'Dadam': 'Kulchatoy',
# 'Guli':'Kavob',
# 'Onam':'Shurpa',
# 'Asal':'qand',
# 'Bahodir':'Manti'
# }

# print (f"Gulining sevimli ovqati {taom['Guli']}")
# print (f"Onamning sevimli ovqati {taom['Onam']}")
# print (f"Asalning sevimli ovqati {taom['Asal']}")
# print (f"Bahodirning sevimli ovqati {taom['Bahodir']}")
# print (f"Dadamning sevimli ovqati {taom['Dadam']}")

# en_en = {'int':'It is an integer',
# 'float':'It is a decimal number',
# 'str':'It is a word',
# 'if':'It is a condition'
# }
# print (en_en['int'])
# print (en_en['float'])
# print (en_en['str'])
# print (en_en['if'])

# en_en = {'int':'It is an integer',
# 'float':'It is a decimal number',
# 'str':'It is a word',
# 'if':'It is a condition'
# }
# # dict = input("Please, wrtie a word:\n").lower()
# # print (en_en.get(dict,"Bunday so'z mavjud emas"))
#
# dict = input("Please, wrtie a word:\n").lower()
# tr = en_en.get(dict)
# if tr==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print (f"{dict.title()} so'zi tarjimasi {tr}")

python = {'int':'integer',
'float':'decimal number',
'str':'string',
'for':'a type of condition',
'if':'another type of condition',
'tupel':'a list that can not be changed'
}
key = input("Please write a word:\n")

# print(python.get(key,"Bunday so'z mavjud emas"))
tr = python.get(key)

if tr==None:
    print ("Bunday so'z mavjud emas")
else:
    print (f"{key.title()} manosi {tr}")
