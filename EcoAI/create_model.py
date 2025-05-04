# create_model.py

import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Generate synthetic data: [transport_km, energy_kWh, meat_kg]
X = np.random.rand(100, 3) * [100, 50, 10]  # realistic max ranges
# Coefficients representing approximate carbon impact factors
y = X @ [0.12, 0.25, 0.4]  # weighted sum: transport, energy, meat

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save model to file
with open('carbon_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to carbon_model.pkl")
