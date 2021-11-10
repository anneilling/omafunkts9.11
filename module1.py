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
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  
            return False
    return True  

