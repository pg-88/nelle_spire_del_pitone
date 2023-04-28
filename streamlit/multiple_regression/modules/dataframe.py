import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale, StandardScaler
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



startup_url = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"
company_url = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Company.csv"

strt = pd.read_csv(startup_url)
cmp = pd.read_csv(company_url)

strt_head = strt.columns
cmp_head = cmp.columns

norm_strt = pd.DataFrame(minmax_scale(strt), columns=strt_head)
norm_cmp = pd.DataFrame(minmax_scale(cmp), columns=cmp_head)

std_strt = pd.DataFrame(StandardScaler().fit_transform(strt), columns=strt_head)
std_cmp = pd.DataFrame(StandardScaler().fit_transform(cmp), columns=cmp_head)

cor_strt = strt.corr()
cor_cmp = cmp.corr()


class AnalData:
    def __init__(self, df: pd.DataFrame) -> None:
        self._df = df

# if __name__ == "__main__":
#     st.radio("select data", ("Startup", "Company"))


    
#     st.write(strt_head)
#     st.write(cmp_head)
    
#     st.write(norm_strt)
#     st.write(norm_cmp)

#     st.write(std_strt.describe())
#     st.write(std_cmp.describe())

#     hm = plt.figure()
#     sns.heatmap(cor_strt, annot=True)
#     st.pyplot(hm)
    