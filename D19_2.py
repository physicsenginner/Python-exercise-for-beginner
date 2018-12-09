metin = """Yaşamak Bir Ağaç Gibi Tek ve Hür
ve Bir Orman Gibi Kardeşçesine"""
def azalt(ifade):
    if len(ifade)<1:
        return ifade
    else:
        print(ifade)
        return azalt(ifade[:-1])
print(azalt("Mutlu Döner"))
