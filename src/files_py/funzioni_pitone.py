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
names = ["Pluto","Balto","Lassie","Pongo"]
age =  [121,15,34,12]
print ("Il cane", names[0], "ha",str(age[0]), "anni",'\n' "Il cane", names[1], "ha",str(age[1]), "anni,""\n"
       "Il cane", names[2], "ha",str(age[2]), "anni, Il cane", names[3], "ha",str(age[3]),"anni.")

#provo a stampare tutti i cani con relativi anni innescando un ciclo
#devo prima contare il numero di elementi della lista, poi posso innescare un ciclo con numero di cicli pari al numero degli elementi e stampare 
# gli elementi delle due liste con posizione della lista pari al numero del ciclo. Nota : cosa succede se le liste non hanno lo stesso numero di elementi?


for i in range(len(names)):
   print(f'{names[i]} ha {age[i]}') 

# posso usare anche la funzione zip (unisce due liste)

for n, y in zip(names, age):
	print(f'{n} ha {y}')
        
#cosa succede quando le due liste non sono lunghe uguali?

nome = input ('inserisci il tuo nome : ')
nome
print(f'il nome inserito è : {nome}, è correttò?')

checknome = input('s/n ? : ')
checknome

while checknome == "n":
   print ("ops! Riproviamo... inserisci il tuo nome ")
   nome = input ('inserisci il tuo nome : ')
   nome
   print(f'il nome inserito è : {nome}, è correttò?')

   checknome = input('s/n ? : ')
   checknome


print(f"ok {nome}, ti va di fare un gioco, si chiama indovina numero \ns/n?")

check_play= input(" ")

while check_play == "s":

   numero_utente = input ('Benissimo! Prova a indovinare a cosa sto pensando, inserisci un numero da 1 a 5 : ')
   numero_utente

   import random
   numero_intero_casuale = random.randint(1,5)
   print(numero_intero_casuale)

   tentativo = 0

   while numero_intero_casuale != int(numero_utente):
      if numero_intero_casuale < int(numero_utente):
         print ('Mi dispiace, hai sbagliato, un piccolo suggerimento, il numero che ho pensato è inferiore, riprova.')
      else:
         print ('Mi dispiace, hai sbagliato, un piccolo suggerimento, il numero che ho pensato è maggiore, riprova.')

      tentativo=tentativo+1
      numero_utente = input ('inserisci un numero : ')
      numero_utente


   tentativo = tentativo+1

   print (f"Complimenti! Hai indovinato il numero dopo {tentativo} tentativi! Vuoi giocare ancora? \n s/n ?")
   check_play= input(" ")

print('Va bene, alla prossima!')