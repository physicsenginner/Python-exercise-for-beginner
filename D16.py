def kayit_olustur(adi="--",soyadi="--",telefon="--",yas="--"):
    print("="*30+"""
       \n Adı: {0}
       \n Soyadı: {1}
       \n Telefonu:{2}
       \n Yaş: {3}
       \n""".format(adi,soyadi,telefon,yas)
     +"="*30)

##    
##adi1 = input("Adınızı Giriniz")
##soyadi1 = input("Soyadınızı Giriniz")
##telefon1 = input("Telefon :")
##yas1 = input("Yaşınızı Giriniz")

kayit_olustur("İbrahim","EDİZ","5052643514","75")
kayit_olustur(soyadi="EDİZ",adi="İbrahim"
              ,yas="75",telefon="5052643514",)
kayit_olustur()
