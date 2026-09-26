x = int(input("Masukkan sebuah bilangan bulat: "))

if x < 0:
    print ("Bilangan negatif")
elif x  == 0:
    print ("Nol")
elif x % 2 == 0:
    print ("Bilangan positif genap")
else:
    print ("Bilangan positif ganjil")