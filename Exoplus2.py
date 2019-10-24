#Exercice1: un échiquier.

liste=["a","z","a","z","a","z","a","z"]
    for i in range(len(liste)):
        print ([i])
        for j in range(liste[i]):
            print (liste[i][j])




#exercice2: Matrix dans le terminal
list=[0, 0, 0, 0]
for i in range(0, 4):
    list[i]=1
    print (list,"------")
    list[i]=0




#exercice 3: nombre pair ?
user=float(input("amount"))


def even(mynumber):
        round(mynumber,0)
        if mynumber% 2 ==0 :
           print("even")
        if not mynumber% 2 == 0:
           print("not even")


even(user)
    
    

