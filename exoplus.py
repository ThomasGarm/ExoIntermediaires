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
if math.sqrt(age).is_integer():#==False:
    print ("not a square")

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
    


