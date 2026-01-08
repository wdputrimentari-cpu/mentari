# main.py

from utils import *

print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Jajar Genjang")
print("5. Layang-Layang")
print("6. Belah Ketupat")
print("7. Trapesium")
print("8. Lingkaran")
print("9. Keluar")

pilih = int(input("Pilih bangun datar: "))

if pilih == 1:
    sisi = float(input("Masukkan sisi: "))
    print("Luas Persegi =", luas_persegi(sisi))

elif pilih == 2:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    print("Luas Persegi Panjang =", luas_persegi_panjang(panjang, lebar))

elif pilih == 3:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    print("Luas Segitiga =", luas_segitiga(alas, tinggi))

elif pilih == 4:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    print("Luas Jajar Genjang =", luas_jajar_genjang(alas, tinggi))

elif pilih == 5:
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    print("Luas Layang-Layang =", luas_layang_layang(d1, d2))

elif pilih == 6:
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    print("Luas Belah Ketupat =", luas_belah_ketupat(d1, d2))

elif pilih == 7:
    a = float(input("Masukkan sisi sejajar a: "))
    b = float(input("Masukkan sisi sejajar b: "))
    tinggi = float(input("Masukkan tinggi: "))
    print("Luas Trapesium =", luas_trapesium(a, b, tinggi))

elif pilih == 8:
    r = float(input("Masukkan jari-jari: "))
    print("Luas Lingkaran =", luas_lingkaran(r))

elif pilih == 9:
    print("Program selesai")

else:
    print("Pilihan tidak valid")
