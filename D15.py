from random import randint
rand = randint(1,100)
while not input("Devam Etmek İster misin?"):
    for i in range(0,5):
        tahmin  = int(input("Tuttuğum sayısı tahmin et"))
        if tahmin < rand:
            print("yukarı")
        elif tahmin > rand:
            print("aşağı")
        elif tahmin == rand:
            print("tebrikler")
            break
    print("Tahmin Ettiğim Sayı",rand)

