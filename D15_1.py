giris = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Karesini Hesaplama
(6) Kare Kökünü Hesaplama"""
print(giris)
anahtar = 1
while anahtar == 1:
    soru=input("""Yapmak istediğiniz işlemi seçiniz
               (Çıkmak için ç):""")
    if soru == "ç":
        print("Çıkılıyor")
        anahtar = 0
    else:
        if soru == "5" :
            sayi1 = int(input("Sayıyı Giriniz"))
            print("İşlemin sonucu :{}".format(sayi1**2))
        elif soru == "6":
            sayi1 = int(input("Sayıyı Giriniz"))
            print("İşlemin sonucu :{}".format(sayi1**0.5))
        else:
            sayi1=int(input("Birinci Sayıyı Giriniz"))
            sayi2=int(input("İkinci Sayıyı Giriniz"))
            if soru == "1":
                print("İşlemin sonucu :{}".format(sayi1+sayi2))
            elif soru == "2":
                print("İşlemin sonucu :{}".format(sayi1-sayi2))
            elif soru == "3":
                print("İşlemin sonucu :{}".format(sayi1*sayi2))
            elif soru == "4" and sayi1 > 0:
                print("İşlemin sonucu :{}".format(sayi1/sayi2))
        
                
    
