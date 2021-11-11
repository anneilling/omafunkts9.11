from module1 import *
from math import *

while True:
    print("Funktsioonid" .center(50,"+"))
    v=input("arithmetic - A\nis_year_leap-Y\nis_prime-N\nsquare-S\nseason-K\ndate-D")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe: ")
        tulemus=arithmetic(arv1,arv2,sym)
        print(tulemus)
    elif v.upper()=="Y":
        tulemus=is_year_leap(int(input("Sisesta aasta ")))
        print(tulemus)
    elif v.upper()=="N":
        tulemus=is_prime(int(input("Sisesta number ")))
        print(tulemus)
    elif v.upper()=="S":
        tulemus=square(int(input("Sisesta ruudu külk: ")))
        print(tulemus)
    elif v.upper()=="K":
        tulemus=season(int(input("Sisetage kuu number (1-12): ")))
        print(tulemus)
    elif v.upper()=="D":
