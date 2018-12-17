import os
url = r"D:\İbrahim EDİZ\24112018\defter.txt"
if os.path.exists(url):
    pass
else:
    open(url,"w")


anahtar = 1
adim = ""
def d_okuma(url):
    global adim
    liste = []
    try:
        adim = "F:d_okuma-1F"
        with open(url,"r") as dosya:
            liste = dosya.readlines()
        adim = "F:d_okuma-2F"
    except:
        print("bir hata oluştu Hata Kodu:",adim)
    return liste

def d_yazma(url):
    global adim
    liste = []
    try:
        adim = "F:d_yazma-1F"
        dosya = open(url,"r+")
        liste = dosya.readlines()
        adim = "F:d_yazma-2F"
        dosya.seek(0)
        liste2 = liste.copy()
        adim = "F:d_yazma-3F"
        sira = str(len(liste)+1)
        baslik = input("Başlığı giriniz")
        detay = input("Detayı giriniz")
        adim = "F:d_yazma-4F"
        liste2.append(sira+";"+baslik+";"+detay+"\n")
        adim = "F:d_yazma-5F"
        liste = liste2
    except:
        print("bir hata oluştu Hata Kodu:",adim)
    finally:
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()
def bilgi_yazdir(liste):
    for item in liste:
        print(item)

def d_guncelle(url):
    global adim
    liste = []
    try:
        adim = "F:d_guncelle-1F"
        dosya = open(url,"r+")
        adim = "F:d_guncelle-2F"
        bilgi_yazdir(d_okuma(url))
        liste2 = liste.copy()
        giris = input("İşlem yapmak istediğiniz dosyayı seçiniz")
        for i in range(0,len(liste2)):
            if giris == liste2[i].split(";")[0]:
                baslik = input("Başlığı giriniz")
                detay = input("Detayı giriniz")
                liste2[i] = giris+";"+baslik+";"+detay+"\n"
        liste = liste2
    except:
        print("bir hata oluştu Hata Kodu:",adim)
    finally:
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()
                
def d_sil(url):
    global adim
    liste = []
    try:
        adim = "F:d_guncelle-1F"
        dosya = open(url,"r+")
        adim = "F:d_guncelle-2F"
        bilgi_yazdir(d_okuma(url))
        liste2 = liste.copy()
        giris = input("İşlem yapmak istediğiniz dosyayı seçiniz")
        for i in range(0,len(liste2)):
            if giris == liste2[i].split(";")[0]:
               liste2.pop(i)
        liste = liste2
    except:
        print("bir hata oluştu Hata Kodu:",adim)
    finally:
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()        

        
        
            
            

while anahtar == 1:
    try:
        giris = int(input("""Yapmak istediğiniz işlemi seçiniz:
          (1) S
          (2) İ
          (3) D
          (4) U
          (5) E\n"""))
        adim = "1A"
        if giris == 5:
            anahtar = 0
            adim = "2A girilen :"+str(giris)
        elif giris == 1:
            adim = "3A girilen :"+str(giris)
            pass
        elif giris == 2:
            adim = "4A girilen :"+str(giris)
            d_yazma(url)
        elif giris == 3:
            adim = "5A girilen :"+str(giris)
            d_sil(url)
        elif giris == 4:
            adim = "6A girilen :"+str(giris)
            d_guncelle(url)
        else:
            raise Exception("Hata Oluştu Else Giriş")
    except:
        print("Hata Kodu:",adim)
        





            
