import streamlit as st
import json
from pages import pag1
from pages import pag2
from pages import pag3
from pages import pag4


def auth(name, psw) -> bool:

    auth = False
    with open("./resource/users.json") as file_json:
        users = json.load(file_json)

    for n in users["user_name"] :
        if (n == name and users["password"] == psw):
            auth = True
            break
    return auth
        
def main():
    st.header("Benvenuto")
    
    pag_name = ["pag1","pag2","pag3","pag4"]

    OPTIONS = pag_name
    sim_selection = st.selectbox('Seleziona la pagina', OPTIONS)

    if sim_selection == pag_name[0]:
        pag1()
    elif sim_selection == pag_name[1]:
        pag2()
    elif sim_selection == pag_name[2]:
        pag3()
    else:
        st.markdown("Something went wrong. We are looking into it.")



if __name__ == '__main__':
    main()
