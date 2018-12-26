class Sınıf():
    __gizli = "iki kişinin bildiği sır değildir"
    
    sinif_niteligi = "sinif_niteliği"
    def ornek_metod(self):
        print("Örnek Metod")
    @classmethod
    def sinif_metodu(cls):
        print("Sınıf Metodu")

    @staticmethod
    def statik_metod():
        print("statik metod")

        
    @classmethod
    def gizliGoster(cls):
        print(cls.__gizli)
    @classmethod
    def gizlidegis(cls,deger):
        cls.__gizli = deger
