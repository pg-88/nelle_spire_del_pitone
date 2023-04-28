import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from io import BytesIO


def model(data: pd.DataFrame,  nametrgt: str, perc_test: float):
    model = LogisticRegression()
    y = data[nametrgt]
    X = data.drop(columns=nametrgt)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=perc_test, random_state=42)
    print(X_tr.values)
    model.fit(X_tr.values, y_tr.values)
    return model



def main():
    ##creare il modello
    dataframe = pd.read_csv("streamlitApp/dataframe_iris.csv",index_col=0)
    #st.write(dataframe)
    perc = st.slider(label="test portion of the dataset", min_value=0.1, max_value=0.9)
    log_reg = model(dataframe, "class", perc)
    my_file = st.file_uploader(label="Drag your CSV here:", accept_multiple_files=False)
    
    if (my_file is not None):
        print(my_file.getvalue())
        print(type(my_file))
        features = pd.read_csv(my_file, index_col=0)
        st.markdown("### Imported File CSV")
        st.write(features)

        st.markdown("### Calssificated Data: ")
        arr_feat = features.to_numpy()
        output = log_reg.predict(arr_feat)
        features["Class Predict"] = output
        st.write(features)
        # predispongo l'oggetto binario
        output = BytesIO()

        ## PRESO DA https://stackoverflow.com/a/70120061
        writer = pd.ExcelWriter(output)
        features.to_excel(writer)
        writer.close()
        processed_data = output.getvalue()
        st.download_button(label="Export as excel",data=processed_data, file_name="iris_ml.xlsx")
        #################################################
if __name__ == "__main__":
    main()