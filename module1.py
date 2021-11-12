def arithmetic(a:float,b:float,c:str):
    """Lihtne kalkulaator
    +- liitmine
    --lahutamine
    *-korrutamine
    /-jagamine
    :param float a:Esimene arv
    :param float b:Teine arv
    :param str c:Aritmeetiline tehing
    :rtype var: Märamata tüüb
    """

    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            r="Div/0"
    else:
        r="Tundmatu sym"
    return r

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
    #:param int number : True or False
    #:rtype str: Funktsiooni vastus 1 or 2
    #Tagastab True kui on algarve ja False kui on midagi muu
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  
            return False
    else:
        return True  



def square(s:float):
    #P, S, d leidmine
    #:Param float number: P, S, d
    #:rtype str: int int int

     if j!=0:
        p=j*4
        s=j*j
        d=sqrt(j*j*j*j)
        a=(("P="),p)
        b=(("S="),s)
        c=(("D="),d)
     return a,b,c

def season(num):
    #määrame aastaaega kuude kaupa 
    #:param int seson: kuu järjekordne number
    #:rtype str: aastaaja nimetus
    #Tagastab season talv või kevad või suvi või sügis 
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


def xor_cipher(string: str , key: str)->str:
    """Tavaline sõna kodeeritakse
    ord - десятичное число,которое кодирует букву
    """

    result = ""
    temp = int()
    for i in range(len(string)):
        temp = ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp ^=ord(key[j])
        result +=chr(temp)
    return result

def xor_uncipher(string:str , key: str) -> str:
    result =""
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i]= chr(ord(key[j]) ^ ord(temp[i]))
        result +=temp[i]
    return result



def bank(a:float, years:int):
    #otsime, milline on panus
    #:param float raha, int aasta: raha
    #:rtype bool: Funktisooni vastus raha
    if a>=0:
        k=years*1.1
        b=a*k
    return b 


def date(day: int, month: int, year: int):
    if year%4 == 0:
        if month == 2 and 0 < day <= 29:
            vastus=True
        elif 0 < day <= 31:
            vastus=True
        elif 0 < day <= 30:
            vastus=True
        else:
            vastus=False
    elif year%4 != 0:
        if month == 2 and 0 < day < 28:
            vastus=True
        elif 0 < day <= 31:
            vastus=True
        elif 0 < day <= 30:
            vastus=True
        else:
            vastus=False
    else:
        vastus=False

    return vastus
   