"""Ho fatto un file .py perchè il notebook jupiter non va bene con print"""

#Funzione print
"""Si invoca con il nome print, come argomenti prende un po di tutto però
nel caso si tratti di un oggetto non rappresentabile ci mostra il suo indirizzo
di memoria."""

v = 66
print(v)

s = "lorem ipsum"
print(s)

quota = 2.33333
print(quota)

l = [2, 3, "Hi", "hello"] #lista. posso stampare una lista intera
print(l) #output [2, 3, "Hi", "hello"]
#la lista ha un'indice [0, 1,    2,     3  ]
#                      [2, 3, "Hi", "hello"]
#oppure posso stampare un elemento di una lista
print(l[0]) #stampa solo il primo elemento

print(__name__)#stampa variabli interne a python

print(type)#ritorna la categoria a cui appartiene type non ha senso ma si può

#Concatenazione nel print:

print("v è una variabile il cui valore è: ", v, '\n', "mentre la variabile quota è un numero con la virgola: ", '\t', quota)
#             ^stringa costante                   ^singolo carattere(carattere speciale)

##### Per sperimentare si potrebbe creare una lista di nomi e una lista di età e provare a selezionarli e comporli per fare una stringa
