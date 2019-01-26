"ecrire le programme qui va retourner 1 liste3 les elements commune entre les deux"
liste1=[12,23,53,14,7,9,19,34,23,19,12]
liste2=[4,51,18,24,52,19,34]

"""set = ensemble{} généréer sur la base de la liste =, on va pas avoir les mémes elements sans doubleurs
A.intsersection(B)
avec aAet B sont des set """
x=set(liste1)
y=set(liste2)
liste3=x.intersection(y)
list(liste3)
if liste3==[]:
    print(" pas d'intersction")
else :
    print(list(liste3))
    


