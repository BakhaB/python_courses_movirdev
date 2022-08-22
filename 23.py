### Klass va Obyekt

# matn = "Assalomu aleykum!"
# print (matn.lower())
# print (matn.upper())
# print (type(matn))

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu

    def info(self):
        inf = f"{self.model}, RAM:{self.ram}, SSD:{self.hdd}, CPU:{self.cpu}"
        return inf

macbook = Kompyuter("Apple Macbook","8Gb", "512Gb","M1", "M1")

print (macbook.info())
