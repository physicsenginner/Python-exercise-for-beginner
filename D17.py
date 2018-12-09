from random import randint
def liste_kontrol(liste2,sayi):
    for item in liste2:
        if item == sayi:
            print(sayi)
            return False
    return True



anahtar = 1
while anahtar == 1:
    if input("""Oynamak için Enter'a bas
            (Çıkış için 'ç')""") == "ç":
        anahtar = 0
    else:
         liste =[]
         while not len(liste) == 6:
            rand = randint(1,50)
            if liste_kontrol(liste,rand):
                liste.append(rand)
    print(liste)

            
    
