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
   
   print(f'il nome inserito è : {nome}, è corretto?')

   checknome = input('s/n ? : ')

   while checknome == "n":
      print ("ops! Riproviamo... inserisci il tuo nome ")
      nome = input ('inserisci il tuo nome : ')   
      print(f'il nome inserito è : {nome}, è corretto?')
      checknome = input('s/n ? : ')
      if (checknome == "s"):
         break


#GAME START

checknome = input('s/n ? : ')


while (checknome !="n" and checknome != "s"):
   print ("ops! Non ho capito, insierisci la lettera s se il nome è giusto o n se vuoi cambiare nome ")
   
   print(f'il nome inserito è : {nome}, è correttò?')

   checknome = input('s/n ? : ')

while checknome == "n":
   print ("ops! Riproviamo... inserisci il tuo nome ")
   nome = input ('inserisci il tuo nome : ')
   
   print(f'il nome inserito è : {nome}, è correttò?')

   checknome = input('s/n ? : ')
   


print(f"ok {nome}, ti va di fare un gioco, si chiama indovina numero \ns/n?")

check_play= input(" ")

level = 0
new_level = 0

#ciao

while check_play == "s":
     
   if level == 0:
      level = input ("Scegli il livello di difficoltà da 1 a 10, 1=facile, 10=difficile: ")

   else:
      level=level
      
   assegnazione_livello = {
      "1": "super facilissimo",
      "2": "facilissimo",
      "3": "Balotta",
      "4": "Facilone",
      "5": "Polleg",
      "6": "Umarell",
      "7": "Vèz",
      "8": "Boia de",
      "9" : "Rusco",
      "10": "Soccia"}

   print(f"hai scelto il livello : {assegnazione_livello.get(level)}")
   numero_utente = input (f"Benissimo! Prova a indovinare a cosa sto pensando, inserisci un numero da 1 a {level} : ")
               
   numero_intero_casuale = random.randint(1,int(level))

while check_play == "s":

   numero_utente = input ('Benissimo! Prova a indovinare a cosa sto pensando, inserisci un numero da 1 a 5 : ')
   

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
      
   check_play= input("")

   if check_play=="s":
      print("Di quanti livelli vuoi aumentare o diminuire la difficoltà?")
      new_level=input("")
      level=(int(level)+int(new_level))
      print (level)
   else:
      check_play == 0

      


   tentativo = tentativo+1

   print (f"Complimenti! Hai indovinato il numero dopo {tentativo} tentativi! Vuoi giocare ancora? \n s/n ?")
   check_play= input(" ")


print('Va bene, alla prossima!')