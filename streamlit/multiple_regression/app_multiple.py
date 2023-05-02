import streamlit as st
import pandas as pd



from modules.multiple import MultipleRegression as mr



def main():
    path = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"
    st.markdown(
        """## WHERE ARE THE DATAAA??? 
        
        Do you have a .csv or a link?""")
    link = st.text_input(label="") # input del link o del path di sis del file csv
    in_file = st.file_uploader(label="Gimmi da file...", type="csv")
    target = st.text_input(label="Write here the name of the target column")
    if st.button("create the model"):
        if(in_file != None and target != None):
            pass # creare il modello con la classe Multiple regression usando il file csv
        elif(link != None and target != None):
            pass # 

if __name__ == "__main__":
    main()