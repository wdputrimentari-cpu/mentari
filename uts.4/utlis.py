# utils.py
import math

def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def luas_trapesium(a, b, tinggi):
    return 0.5 * (a + b) * tinggi

def luas_lingkaran(r):
    return math.pi * r * r
