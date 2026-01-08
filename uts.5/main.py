from utils import *

while True:
    print("\n===== MENU BANGUN RUANG =====")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")
    print("6. Prisma")
    print("7. Limas")
    print("8. Keluar")

    pilih = int(input("Pilih bangun ruang : "))

    if pilih == 1:
        s = float(input("Masukkan sisi : "))
        print("Volume Kubus =", volume_kubus(s))

    elif pilih == 2:
        p = float(input("Masukkan panjang : "))
        l = float(input("Masukkan lebar : "))
        t = float(input("Masukkan tinggi : "))
        print("Volume Balok =", volume_balok(p, l, t))

    elif pilih == 3:
        r = float(input("Masukkan jari-jari : "))
        t = float(input("Masukkan tinggi : "))
        print("Volume Tabung =", volume_tabung(r, t))

    elif pilih == 4:
        r = float(input("Masukkan jari-jari : "))
        t = float(input("Masukkan tinggi : "))
        print("Volume Kerucut =", volume_kerucut(r, t))

    elif pilih == 5:
        r = float(input("Masukkan jari-jari : "))
        print("Volume Bola =", volume_bola(r))

    elif pilih == 6:
        alas = float(input("Masukkan luas alas : "))
        t_prisma = float(input("Masukkan tinggi prisma : "))
        print("Volume Prisma =", volume_prisma(alas, t_prisma))

    elif pilih == 7:
        alas = float(input("Masukkan luas alas : "))
        t_limas = float(input("Masukkan tinggi limas : "))
        print("Volume Limas =", volume_limas(alas, t_limas))

    elif pilih == 8:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")