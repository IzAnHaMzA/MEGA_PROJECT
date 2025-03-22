import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the data
data = pd.read_csv('data/app_usage.csv')

# Preprocess data
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['day_of_week'] = data['timestamp'].dt.dayofweek

# Prepare features and target
X = data[['day_of_week', 'launch_count']]
y = data['usage_time']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'habit_model.pkl')

print("✅ Model trained and saved as habit_model.pkl")
