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







