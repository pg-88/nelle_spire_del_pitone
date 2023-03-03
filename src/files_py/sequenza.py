"""Per tradurre blocco per blocco il diagramma,** partiamo dal blocco inizio:
rappresenta semplicemente il fatto di avere il programma e la possibilità di 
poterlo far girare. Cosa scontata adesso però se non ci fosse l'interprete o il
compilatore non si potrebbe proseguire.

Leggi x, Leggi y: Abbiamo bisogno di usare una funzione per questo. Tutti i
linguaggi hanno la possibilità di prendere input in qualche modo, che sia da 
utente, da file o tramite connessioni con DB.

Nel nostro caso assumiamo che l'idea è quella di un input da utente presente
davanti alla tastiera. 

La funzione in python è:

input()
"""

input("Scrivi qualcosa")

"""Eseguendo questo, effettivamente ci chiede un input e si vede la stringa
-Scrivi qualcosa- però poi si ferma e non so dove sia finito quello che ho 
scritto.

Quindi è necessario un assegnamento per memorizzare in una variabile il valore
passato alla funzione input."""

x = int(input("Inserisci il primo numero"))
y = int(input("Inserisci il secondo numero"))

"""Input è una funzione che restituisce stringhe, se ho bisogno di numeri devo
fare una conversine a int che qui ho fatto inglobando la fz input con una fz
int. In sostanza chiedo un input all'utente, prendo quello che ha scritto e lo
trasformo in numero INTERO, poi lo assegno alla variabile.


Ora ho i numeri memorizzati nelle varibili x e y, per essere sicuro faccio
il print (lo step del print non è assolutamente necessario ma serve per capire
se il programma sta procedendo come previsto)"""

print(x)
print(y)

"""Il prossimo step è W = X * Y ovvero un assegnamento. Alla variabile w viene
assegnata un'espressione che, in questo caso è il prodotto del *valore* di due
variabili.


Le regole per l'operazione di assegnamento sono:

- a sinistra del segno `=` ci deve essere un nome valido per una variabile 
(non inizia con numero, non ha spazi, non ha simboli riservati +*-/@#!); 

- a destra un'espressione che può essere un espressione aritmetica come in
questo caso, una chiamata a una funzione (come prima con input),
una costante (numero o stringa scritti nel codice)
"""
w = x * y

"""Ultimo step Leggi(W) che è un semplice comando print"""

print(w)



# Come si poteva fare, ovvere tecniche complesse per cose semplici

#assegnamento di più variabili

a, b = int(input("Scrivi 2 numeri e te li moltiplico")), int(input("Altro"))

v = a * b

print("Il risultato della moltiplicazione è: ", v)