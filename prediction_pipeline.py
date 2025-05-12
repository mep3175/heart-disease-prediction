import pandas as pd
import joblib

class CustomData:
    def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg,
                 thalach, exang, oldpeak, slope, ca, thal):
        self.data = {
            "age": [float(age)],
            "sex": [int(sex)],
            "cp": [float(cp)],
            "trestbps": [float(trestbps)],
            "chol": [float(chol)],
            "fbs": [int(fbs)],
            "restecg": [float(restecg)],
            "thalach": [float(thalach)],
            "exang": [int(exang)],
            "oldpeak": [float(oldpeak)],
            "slope": [float(slope)],
            "ca": [float(ca)],
            "thal": [float(thal)]
        }

    def get_data_as_dataframe(self):
        return pd.DataFrame(self.data)

class PredictPipeline:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, data):
        return self.model.predict(data)
