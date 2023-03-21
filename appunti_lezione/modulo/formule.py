from math import pi

def lib_area_rect(base:float, altezza:float) -> float:
    """ritorna float che è l'area calcolata con base e altezza"""
    return base * altezza

def lib_perim_rect(base:float, altezza:float) -> float:
    """ritorna float che è il perimetro calcolato con base e altezza"""
    return 2*base + 2*altezza

def lib_area_cerchio(raggio:float) -> float:
    """ritorna float area del cerchio"""
    return pi * raggio**2

def lib_perim_cerchio(raggio:float) -> float:
    """ritorna float perimetro del cerchio"""
    return 2*pi*raggio

def lib_rettangolo(base:float, altezza:float) -> tuple:
    """primo float è perimetro del rettangolo, secondo float rappresenta l'area"""
    return lib_perim_rect(base, altezza), lib_area_rect(base, altezza)