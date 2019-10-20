# ex1 le nombre le plus grand
a=4
b=2
c=3
d=1
if a>b and a>c and a>d:
    print (a)

# ex2 condition d'âge
import math
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
#if ValueError:
    #print ("empty")


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
longueur=float(input("longueur"))      
largeur=float(input("largeur"))
profondeur=float(input("profondeur"))
debit=float(input("debit par minute"))
volume=longueur*largeur*profondeur
print("temps de remplissage",volume/debit,"mn")

#ex7 calcul de cercle
import math
rayon=int(input("entrez rayon du cercle"))
raycalc=rayon**2
aire=math.pi*raycalc
print(round(aire,2))

#ex8 pyramide
#bon mais "pas ça"
print("*")
print("**")
print("***")
print("****")
print("*****")

n="*"
for x in range (0,6): #abcisse ?
    print(x*n) #on peut multiplier un carac string


           
    


