### External Imports #############
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

##################################

### Project Imports ##############
#import modules.dataframe as data

##################################

### Main
def main():
    #streamlit ###########################################
    st.header("Regression")
    entries = st.slider("number of elements:", 1, 200)
    d = st.slider("inclination of the line:", 0.0, 100.0)
    d_std = st.slider("Standard deviation:", 0.1 , 10.0)
    k_noise = st.slider("Add some noise!!!", 1, 10)
    #####################################################
    #
    generate_random = np.random.RandomState(6969)
    x = 10 * generate_random.rand(entries)
    
    #noise = np.random.normal(0, d_std, 200)
    noise = np.random.normal(0, d_std, entries)
    #y = x * d + noise
    y = x * d + noise * k_noise # eq retta 


    X = x.reshape(-1, 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    y_p = model.predict(X)
    
    fig = plt.figure()
    plt.scatter(x, y)
    plt.plot(x, y_p, '-r')
    plt.axis([0,10, 0, 200])
    st.pyplot(fig)
    
    
    in_num = st.number_input(f"Insert value for x between 0 and {entries}: ",)
    pre = in_num * model.coef_ + model.intercept_

    st.metric(label="Your Predicted value is:", value=pre)


    st.metric(label=f"Given inclination {d}; Calculate is:", value=f"{model.coef_}")
    st.metric(label=f"Intercept Calculated is:", value=f"{model.intercept_}")


###############################################################################


if __name__ == '__main__':
    main()