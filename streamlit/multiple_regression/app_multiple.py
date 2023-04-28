import streamlit as st
import pandas as pd



from modules.multiple import MultipleRegression as mr


def main():
    path = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"
    df = pd.read_csv(path)
    st.write(df)
    reg = mr(df, "Profit")


if __name__ == "__main__":
    main()