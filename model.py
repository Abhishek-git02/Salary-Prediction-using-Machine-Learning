import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv('house_price_dataset.csv')

# Clean data
data = data.dropna()

# Features & target
X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model (VERY IMPORTANT)
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")