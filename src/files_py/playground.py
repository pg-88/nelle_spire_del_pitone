#Indovina numero

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