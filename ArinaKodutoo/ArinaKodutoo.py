from funktionid import *
#7
import datetime
d=int(input("paev: "))
m=int(input("Kuu: "))
y=int(input("aasta: "))
try:
    data=datetime.date(y,m,d)
    print(data)
    print("True")
except:
    print("False")


#6
print(is_prime(int(input("arv: "))))

#5
a = int(input("kui palju euro: "))
years = int(input("Mitu aastat?"))
bank(a, years)


#4
num=season(input("kuu number: "))
print(num)


#3
P,S,d=square(input("ruudu külg"))
print(f"Läbimõõt: {P}")
print(f"Pindala: {S}")
print(f"Diagonaal: {d}")


#2
true_false,p=is_year_leap(input("Sisesta aasta: "))
print(true_false,"----",p)



#1
answer=arithmetic(2.5,"+",1.8,)
print(answer)
answer=arithmetic(input(),input(),input())
print(answer)

