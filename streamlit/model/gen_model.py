import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import joblib as jl



class MultReg:
    
    def __init__(self, csv_url, target_name) -> None:
        '''Args:
            url: il percorso della risorsa di tipo csv
            taget_name: il nome della colonna (Series) che contiene il target'''
        self._df = pd.read_csv(csv_url)
        self._feature = self._df.drop[target_name]
        self._target = self._df[target_name]

        self._feature_train = self._getTrainTest()[0]
        self._feature_tst = self._getTrainTest()[1]
        self._target_train = self._getTrainTest()[2]
        self._target_tst = self._getTrainTest()[3]

    def _getTrainTest(self):
        '''Suddivide feature e target in train set e test set'''
        X_train, X_test, y_train, y_test = train_test_split(
            self._feature, self._target, random_state=42, test_size=0.33)
        
        return (X_train, X_test, y_train, y_test)

    def _createModel(self):
        '''genera il modello
        
        necessita di un dataset per la feature con più di una colonna'''
        model = LinearRegression()
        model.fit(self._feature_train, self._target_train)
        return model

    def exportBin(self, name):
        '''crea il file binario e il metatag con joblib'''
        my_model = self._createModel()
        print(my_model)
        name = name + '.pkl'
        print(name)
        jl.dump(my_model, name)

    # def exportMlem(self, path_name):
    #     path_tag = path_name + '_'
    #     my_model = self._createModel()
    #     mlem.api.save(my_model, path_name, path_tag)



if __name__ == "__main__":
    startup = MultReg("https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv")
    startup.exportBin("./streamlit/model/mutiple_reg")