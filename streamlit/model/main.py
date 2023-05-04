import seaborn as sns
import streamlit as st
import joblib
from gen_model import MultReg


def main():
    model = joblib.load("model/mutiple_reg.pkl")
    rd = st.number_input("R&D Spend For this year: [$]",step= 1)
    amm = st.number_input("Amministration Costs For this year: [$]",step= 1)
    mrkt = st.number_input("Marketing Spend For this year: [$]",step= 1)

    st.metric("Predicted Profit for this year [$]:", round(model.predict([[rd,amm,mrkt]])[0], 2))

if __name__ == "__main__":
    main()


