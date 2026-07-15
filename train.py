import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("dataset/air quality.csv")

# Remove missing values
df = df.dropna()

# Select features and target
features = ["PM2.5", "PM10", "NO", "NO2", "NOx", "CO", "SO2", "O3"]

target = "AQI"

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/air_quality_model.pkl")

print("✅ Model trained successfully!")
print("✅ Model saved to model/air_quality_model.pkl")