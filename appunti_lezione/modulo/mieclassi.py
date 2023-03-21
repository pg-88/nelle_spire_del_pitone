##Classi:

class Cubo:
    """cotiene lato float e i metodi per il volume e la superficie esterna diagonale principale"""
    def __init__(self, lato:float) -> None:
        self.l = lato
    
    def volume(self):
        """ritorna float"""
        return pow(self.l,3)
        #return self.l**3
    
    def sup_esterna(self):
        return 
    
if __name__ == '__main__':
    p = Cubo(3.7) #p è un cubo di lato 3.7
    vol = p.volume() 
    print(p.volume())