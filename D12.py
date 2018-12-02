liste = ["Pzt","S","Ç","P","C","Ct","Pz"]
islem = input("ay için 1 gün için 2")
if islem == "1":
    ranj = range(1,12)
    liste = liste2
else :
    ranj = range(1,8)
    liste = liste1
gun = input("Sıra Girişi:")
if gun:
    gun = int(gun)
    for i in ranj:
        if i == gun:
            
            print("Bugün Günlerden {}".format(liste[i-1]))
else:
    print("Gün girişi yapınız")
    
