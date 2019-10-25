#Exercice1: un échiquier.

#liste=["a","z","a","z","a","z","a","z"]
    #for i in range(len(liste)):
       # print ([i])
       # for j in range(liste[i]):
            #print (liste[i][j])




#exercice2: Matrix dans le terminal
list=[0, 0, 0, 0]
tiret="------"
for i in range(0, 4):
    list[i]=1
    print ("{}\n{}\n{}\n{}\n".format(list[0],list[1],list[2],list[3]))
    list[i]=0

    
#=====================================================
#exercice 3: nombre pair ?

user=float(input("amount"))


def even(mynumber):
    
    round(mynumber)
        
    if mynumber% 2 ==0 :
       print("even")
    if not mynumber% 2 == 0:
        print("not even")


even(user)


#======================================================
#exercice4: factorielle

number=(input("enter number"))

def factorielle(num):
        num=int(num)
        i=1
    
        while num >= i:
              print(num*i)
              i+=1
        


factorielle(number) 



#=======================================================
#exercice5: les tirets ça compte!

def facturation(tiret):
        tiret=tiret.replace('-','\_')
        print(tiret)
    
        
facture=("--------")
print(facture)
facturation(facture)

#======================================================
#exercice6: entrainez vous avec les tableaux.

list=["aubergine","patate","banane","melon","PQ","yahourt"]

print("acheter",list[0],"aussi du",list[4],"puis",list[-1],".")


#======================================================
#exercice7: le tableau d'un HUMAIN:

def humain(liste):
        for i in range (len(liste)):
                print(liste[i])

liste=["thomas","Win", "33ans","séduisant"]        
humain(liste)


#======================================================
#exercice8: le max d'un tableau:

liste=[1,2,3,4,5]

def maximus(liste):
        print(max(liste))

maximus(liste) 

#plus loin:


#======================================================
#exercice9: to do liste:

def todolist(liste):
        user=""

        while user!="fin":
                user=input("to do: ")
                
                if user=="fin":
                   break
                
                liste.append(user)
                
        print(liste)

liste=[]
todolist(liste)





