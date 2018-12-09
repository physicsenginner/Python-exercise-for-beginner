#### tek satırlık fonksiyon
##fonk = lambda x : x*x
##print(fonk(5))
##fonk2 = lambda x,y : print("{} ile {} sayısı girildi".format(x,y))
##fonk2(1,5)
##harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
##çevrim = {i: harfler.index(i) for i in harfler}
##isimler = ["ahmet", "ışık", "ismail", "çiğdem",
##"can", "şule", "iskender"]
##print(sorted(isimler))
##print(sorted(isimler, key=lambda x: çevrim.get(x[0])))

def siralama(*args):
    harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    çevrim = {i: harfler.index(i) for i in harfler}
    isimler = list(args)
    print(sorted(isimler, key=lambda x: çevrim.get(x[0])))
    
siralama("ahmet", "ışık", "ismail", "çiğdem",
"can", "şule", "iskender")
