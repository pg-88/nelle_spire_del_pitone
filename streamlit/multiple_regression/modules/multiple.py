from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class MultipleRegression:
    def __init__(self, dataframe, NameColTarget) -> None:
        get_feature = lambda Name : dataframe.drop(columns=Name)
        self._feature = get_feature(NameColTarget)
        self._trgt = dataframe[NameColTarget]

    def create_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self._feature, self._trgt)

    
if __name__ == "__main__":
    pass
