import pickle
import numpy as np

with open('carbon_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_carbon(data):
    arr = np.array(data).reshape(1, -1)
    return round(model.predict(arr)[0], 2)
