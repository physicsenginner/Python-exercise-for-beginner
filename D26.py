class Asker():
    komutanlik = "Kara"
    rutbe = ""
    __askersayisi=[]
    __deger1 = 0
    def __init__(self,adi=""):
        self.daire = ["İstihkâm"]
        self.hitap = adi
        self.selamdur()
        self.degerarti()
        self.askerarttir()
    @staticmethod
    def pi():
        return 22/7
    @classmethod
    def degerarti(cls):
        cls.__deger1 += 1
    @classmethod
    def askerlistele(cls):
        for asker in cls.__askersayisi:
            print(asker)
    @classmethod
    def deger(cls):
        print(cls.__deger1)
    def sayigoster(self):
        print(self.askersayisi)
    def askerarttir(self):
        self.__askersayisi.append(self.hitap)
    def selamdur(self):
        print(self.hitap, "Selam Durdu!!!")
    def emirver(self):
        print("Rahat-Hazır Ol")
        self.selamdur()
    def nobet():
        print("üç beş nöbeti")
        

class Sivil():
    uyruk = ""
