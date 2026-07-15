import joblib
import numpy as np

# Load trained model
model = joblib.load("model/air_quality_model.pkl")

def predict_aqi(pm25, pm10, no, no2, nox, co, so2, o3):

    data = np.array([[pm25, pm10, no, no2, nox, co, so2, o3]])

    prediction = model.predict(data)

    return round(prediction[0], 2)