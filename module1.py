def arithmetic(a:float,b:float,c:str):
    """Lihtne kalkulaator
    +- liitmine
    --lahutamine
    *-korrutamine
    /-jagamine
    :param float a:Esimene arv
    :param float b:Teine arv
    :param str c:Aritmeetiline tehing
    :rtype float:
    """

    if c=="+":
        n=a+b
    elif c=="-":
        n=a-b
    elif c=="*":
        n=a*b
    elif c=="/":
        if b!=0:
            n=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("Viga!")
    return n

def is_year_leap(aasta: int):

    #Liigaasta leidmine
    #Tagastab True kui on liigaasta ja False kui ei ole
    #:param int aasta:Asta number
    #:rtype bool:Funktsioni vastus logilises formatis
   
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

from math import sqrt
def is_prime(number):
    #algarve leidmine
    #Tagastab True kui on algarve ja False kui on midagi muu
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  
            return False
    return True  



def square(s:float):
    if s!=0:
        tulemus=""
        p=s*4
        s=s*s
        d=sqrt(s*s*s*s)
        print("P=",p)
        print("S=", s)
        print("d=" , d)
    return tulemus


def season(num):
   if num==12 or 1 <= num <= 2:
       s="Talv"
   elif  3 <= num <= 5:
       s="Kevad"
   elif 6 <= num <= 8:
       s="Suvi"
   elif 9 <= num <= 11:
       s="Sügis"
   else:
       s="Viga!"
   return s


def date(date, month, year):

