import streamlit as st 
import pandas as pd

def select_source():
    st.selectbox("Type of resource: ", )


def main():
    st.header("Let's create a Dataframe!")

    st.file_uploader()
if __name__ == '__main__':
    main()