import math

def volume_kubus(s):
    return s ** 3

def volume_balok(p, l, t):
    return p * l * t

def volume_tabung(r, t):
    return math.pi * r * r * t

def volume_kerucut(r, t):
    return (1/3) * math.pi * r * r * t

def volume_bola(r):
    return (4/3) * math.pi * r ** 3

def volume_prisma(alas, t_prisma):
    return alas * t_prisma

def volume_limas(alas, t_limas):
    return (1/3) * alas * t_limas