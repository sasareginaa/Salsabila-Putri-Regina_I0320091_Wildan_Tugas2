print("********Menghitung Luas Persegi Panjang********")
panjang=float(input("Masukkan nilai panjang"))
lebar=float(input("Masukan nilai lebar"))
luas=panjang*lebar
print("Luasnya persegi panjang adalah", luas, "satuan")

print("********Menghitung Luas Lingkaran********")
phi=3.14
r=float(input("Masukan nilai r"))
luas=phi*(r**2)
print("Luasnya lingkaran adalah", luas, "satuan")

print("********Menghitung Luas Permukaan Kubus********")
sisi=float(input("Masukan nilai sisi"))
luas_permukaan=6*(sisi**2)
print("Luas permukaannya adalah", luas_permukaan, "Satuan")

print("********Mengkonversi Suhu Celcius ke Farenheit********")
celcius=float(input("Masukan suhu dalam celcius"))
fahrenheit=((9/5)*celcius)+32
print("Suhu dalam farenheit adalah", fahrenheit, "Fahrenheit")

print("********Mengkonversi Suhu Reamur ke Kelvin********")
reamur=float(input("Masukan suhu dalam reamur"))
kelvin=((5/4)*reamur)+273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")
