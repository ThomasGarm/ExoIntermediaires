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



