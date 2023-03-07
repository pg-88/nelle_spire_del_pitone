#Indovina numero
#IMPORT
import random

#INPUT NOME
nome = input ('inserisci il tuo nome : ')
nome
print(f'il nome inserito è : {nome}, è correttò?')

#CHECK NAME INPUT
checknome = input('s/n ? : ')

while (checknome !="n"):
   if (checknome == "s"):
      break
   print ("ops! Non ho capito, insierisci la lettera \"s\" se il nome è giusto o \"n\" se vuoi cambiare nome ")
   
   print(f'il nome inserito è : {nome}, è correttò?')

   checknome = input('s/n ? : ')

   while checknome == "n":
      print ("ops! Riproviamo... inserisci il tuo nome ")
      nome = input ('inserisci il tuo nome : ')
   
      print(f'il nome inserito è : {nome}, è correttò?')

      echecknome = input('s/n ? : ')


#GAME START

print(f"ok {nome}, ti va di fare un gioco, si chiama indovina numero \ns/n?")

check_play= input(" ")

while check_play == "s":

   livello = input ('Scegli il livello di difficoltà da 1 a 10, 1=facile, 10=difficile: ')

   assegnazione_livello = {
   "1": "super facilissimo",
   "2": "facilissimo",
   "3": "Balotta",
   "4": "facilone",
   "5": "Polleg",
   "6": "Umarell",
   "7": "vèz",
   "8": "boia de",
   "9" : "Bazza",
   "10": "Soccia"}

   x= (assegnazione_livello.get(livello))
   print(f"hai scelto il livello : {x}")
   numero_utente = input (f"Benissimo! Prova a indovinare a cosa sto pensando, inserisci un numero da 1 a {livello} : ")
      
   numero_intero_casuale = random.randint(1,5)

   tentativo = 0

   while numero_intero_casuale != int(numero_utente):
      if numero_intero_casuale < int(numero_utente):
         print ('Mi dispiace, hai sbagliato, un piccolo suggerimento, il numero che ho pensato è inferiore, riprova.')
      else:
         print ('Mi dispiace, hai sbagliato, un piccolo suggerimento, il numero che ho pensato è maggiore, riprova.')

      tentativo=tentativo+1
      numero_utente = input ('inserisci un numero : ')
      


   tentativo = tentativo+1

   print (f"Complimenti! Hai indovinato il numero dopo {tentativo} tentativi! Vuoi giocare ancora? \n s/n ?")
   check_play= input(" ")

print('Va bene, alla prossima!')