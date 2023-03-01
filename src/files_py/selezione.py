"""prendiamo in input come nel file sequenza.py
però stavolta proviamo a prendere un float"""

x = float(input("Inserisci primo numero\n"))
y = float(input("Inserisci secondo numero\n"))


"""Biforcazione, la condizione sarà un espressione booleana che compone con un
and, 2 espressioni booleane sulle 2 variabili"""

if(x != 0 and y != 0):
    w = x * y
else:
    w = 0

"""L'espressione booleana è 

(x != 0 and y != 0)

Leggendola un elemento alla volta:

x non uguale a 0 e y non uguale a zero

Quindi risulterà vera solo se entrambe i valori sono diversi da zero

L'altrimenti e il blocco di codice dell'else"""