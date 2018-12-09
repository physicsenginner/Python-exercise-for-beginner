def calistir(ifade):
    print(eval(ifade))

##calistir(input("Çalıştırılacak ifadeyi giriniz"))
x=10
def ilkFonk(var1,var2):
    global x
    x=var1 + var2
    print(x)
    x = 135

ilkFonk(2,5)
print(x)
