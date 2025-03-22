import joblib
import pandas as pd

# Load trained model
model = joblib.load('habit_model.pkl')

# Predict app usage
def predict_usage(day_of_week, launch_count):
    data = pd.DataFrame({'day_of_week': [day_of_week], 'launch_count': [launch_count]})
    prediction = model.predict(data)[0]
    return round(prediction, 2)
