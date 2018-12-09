try:
    dosya = open(r"D:\İbrahim EDİZ\24112018\defter.txt","r+")
    dosya.read()
    giris = input("Adı Giriniz") + input("Telefonu Giriniz")
    if len(giris) <= 9:
        raise Exception("Hiç mi isim girilmedi")
    else:
        pass
    dosya.write("\n"+giris)
except IOError as hata:
    print("Hata Oluştu",hata)
finally:
    dosya.close()


with open(r"D:\İbrahim EDİZ\24112018\defter.txt","r+") as d:
    d.read()
    d.write("\nİbrahim EDİZ:5052643514")
    
