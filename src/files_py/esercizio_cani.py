

def dif_list(lunga: list, corta: list) -> int:

    x=len(lunga) - len(corta)
    return x

nomi_cani = ["Whisky", "Pluto", "Balto", "Lassie","Pongo"]
eta_cani = [3, 6, 1]
y=dif_list(nomi_cani, eta_cani)    
#print(y)
def ask_eta():
    y=dif_list(nomi_cani, eta_cani)
    while y>0:
     eta= input(f"Quanti hanni ha {nomi_cani[-y]}?") 
     eta_cani.append(eta)
     y=y-1                                                      
    else:
     print("Le due liste sono lunghe uguali")
    return eta_cani


def ask_name():
    y=dif_list(nomi_cani, eta_cani)
    while y<0:
     name= input(f"Come si chiama il cane di {eta_cani[y]} anni?") 
     nomi_cani.append(name)
     y=y+1                                                      
    else:
     print("Le due liste sono lunghe uguali")
    return nomi_cani


if y>0:
  ask_eta()
  print ("Il cane", nomi_cani[0], "ha",str(eta_cani[0]), "anni",'\n' "Il cane", nomi_cani[1], "ha",str(eta_cani[1]), "anni,""\n"
        "Il cane", nomi_cani[2], "ha",str(eta_cani[2]), "anni","\n" "Il cane", nomi_cani[3], "ha",str(eta_cani[3]),"anni.",
        "\n" "Il cane", nomi_cani[4], "ha",str(eta_cani[4]),"anni.")
else:
  ask_name() 
  print ("Il cane", nomi_cani[0], "ha",str(eta_cani[0]), "anni",'\n' "Il cane", nomi_cani[1], "ha",str(eta_cani[1]), "anni,""\n"
        "Il cane", nomi_cani[2], "ha",str(eta_cani[2]), "anni","\n" "Il cane", nomi_cani[3], "ha",str(eta_cani[3]),"anni.",
        "\n" "Il cane", nomi_cani[4], "ha",str(eta_cani[4]),"anni.")  