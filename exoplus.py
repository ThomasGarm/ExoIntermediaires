
# ex1 le nombre le plus grand
a=4
b=2
c=3
d=1
if a>b and a>c and a>d:
    print (a)

# ex2 condition d'âge
import math
try:
    age = int(input("entrez votre âge"))
    if age<0:
        print ("pas possib'")
    if age>=21:
        print ("authorized access")
    if age % 2 == 0:
        print ("even age")
    if math.sqrt(age).is_integer():
        print ("square")
    if math.sqrt(age).is_integer()==False:
        print ("not a square")
except ValueError:
    print("no entry")



# ex3 le nombre caché
print("Cherchez le nombre caché!")
sn=177
inpnum=int(input("entrez un nombre"))
while sn!=inpnum:
    if inpnum<sn:
       print("plus grand")
       inpnum=int(input("recommence"))
    if inpnum>sn:
       print("plus petit")
       inpnum=int(input("recommence"))  
if inpnum==sn:
    print("Bravo")  

#ex4 nombre en boucle
for i in range(0,100):
    print(i+1)

#ex5 nombre en boucle pair
for i in range(0,100):
    if i%2==0:
        print (i+2)

#ex6 remplir la piscine
def piscine(a, b, c, d):
    volume=a*b*c/d
    print (volume)
piscine(9, 9, 9, 9)
    


#ex7 calcul de cercle
import math
rayon=int(input("entrez rayon du cercle"))
raycalc=rayon**2
aire=math.pi*raycalc
print(round(aire,2))

#ex8 pyramide


n="*"
for i in range (0,6): 
    print(i*n) #on peut multiplier un carac string

#ex7
for i in range(0,100):
    print(i+1)
    if i%3==0 and not i%5==0:
       print("FIZZ")
    if i%5==0 and not i%3==0:
       print("BUZZ")
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
   


           
    


