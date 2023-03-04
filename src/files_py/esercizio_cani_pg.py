### Definizione delle funzioni
def dif_list(lunga: list, corta: list) -> int:
    """Prese due liste, ritorna un intero che rappresenta la differenza di
    numero di elementi delle liste. Se ritorna un num negativo la corta
    ha più elementi della lunga"""
    return len(lunga) - len(corta)

def ask_eta(diff: int):
    """anzichè chiamare la funzione dif_list passo come parametro un numero che
    rappresenta il numero di iterazioni da fare.
    Questo rende la funzione riutilizzabile anche in altro contesto ovvero
    quando le liste hanno altro nome o sono dichiarate in un altro file."""

    """In caso la lista_1 fosse più lunga della lista_2, va a incrementare ad 
    ogni ciclo la lista_2 con l'imput dato dall'utente. """

    while diff > 0:
        eta = int(input(f"Quanti anni ha {nomi_cani[-diff]}?"))
        #indice negativo per partire dalla fine della lista.
        #altrimenti avrei dovuto usare come indice (len(nomi_cani) - diff)
        eta_cani.append(eta)
        diff -= 1 #Equivale a diff = diff -1 
    
def ask_name(diff: int):
    """anzichè chiamare la funzione dif_list passo come parametro un numero che
    rappresenta il numero di iterazioni da fare.
    Questo rende la funzione riutilizzabile anche in altro contesto ovvero
    quando le liste hanno altro nome o sono dichiarate in un altro file."""

    """In caso la lista_2 fosse più lunga della lista_1, va a incrementare
    ad ogni ciclo la lista_1 con l'imput dato dall'utente. """

    while diff < 0:
        name= input(f"Come si chiama il cane di {eta_cani[-diff]} anni?")
        #indice negativo per partire dalla fine della lista.
        #altrimenti avrei dovuto usare come indice (len(eta_cani) - diff)
        nomi_cani.append(name)
        diff -= 1 #Equivale a diff = diff -1

def completa_dati(nomi: list, eta: list) -> None:
    """Prende due liste, controlla se una è più lunga dell'altra e nel caso
    invoca la funzione appropriata per completare i dati."""
    
    d = dif_list(nomi, eta)
    if d == 0:
        print("Le liste sono complete")
    if d > 0:
        ask_eta(d)
    else:
       ask_name(d)

def stampa_dati(nomi: list, eta:list) -> None:
    
    """Prende come parametri le liste di nomi e età rispettivamente.
    Ritorna None,
    Stampa i dati contenuti formattati."""
    
    for i in range(len(nomi)):
        print(f"Il cane {nomi[i]} ha {eta[i]} anni\n")


###Fine definizione delle funzioni

"""
La parte di definizione di classi e funzioni spesso viene fatta in un file
separato da cui si importa con la direttiva import quello che serve.
I files che contengono classi e funzioni utili al programma sono detti librerie
"""

###Test/Esecuzione

#Dati in ingresso al programma
nomi_cani = ["Whisky", "Pluto", "Balto", "Lassie","Pongo"]
eta_cani = [3, 6, 1]

#Chiamate di funzioni
if dif_list(nomi_cani, eta_cani) != 0:
    completa_dati(nomi_cani, eta_cani)

stampa_dati(nomi_cani, eta_cani)
"""
Con questo if controllo le liste, se hanno numero diverso di elementi lancio 
completa_dati. Se sono omogenee (if diventa False) il blocco if viene ignorato
e si va direttamente a stampa_dati.
Anche questa piccola serie di istruzioni finali può diventare una funzione.

N.B. in questo esempio la modifica dei dati avviene dinamicamente in memoria 
quindi terminata l'esecuzione i dati 'nuovi' spariscono. Per poterli salvare e 
riutilizzare dobbiamo far tornare delle nuove liste alle funzioni che
aggiornano i dati.

Possibili Espansioni:
1. Come fare se i dati mancanti fossero in mezzo alla lista?
Esempio
Nomi = ["Pluto", "", "Balto", "Lassie","Pongo"]
eta = ["N/A", 5, "N/A", 3, 6]
Servirebbe un ciclo che controlla cosa c'è in ogni elemento della lista.

2. -Più avanzato- rifare tutto usando le classi, ad esempio creare una classe
Cane che ha le proprietà nome ed età (volendo anche sesso, razza...) e delle 
funzioni (metodi) per inserire o aggiornare i dati. Inoltre si può fare
un'altra classe (Anagrafica) che controlla la completezza dei dati e li
restituisce formattati o sotto forma di file.
"""