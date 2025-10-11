import pickle
import os

# This is a placeholder "model" object. In a real project, this would be a
# trained classifier from a library like scikit-learn.
mock_model = {
    "model_type": "placeholder",
    "description": "This is a mock model that does not perform real analysis.",
    "version": 0.1,
}

# Define the path where the model will be saved.
model_directory = "backend/model"
model_path = os.path.join(model_directory, "ransomware_model.pkl")

# Create the directory if it doesn't already exist.
print(f"Ensuring directory exists: {model_directory}")
os.makedirs(model_directory, exist_ok=True)

# Save the mock model object to the file using pickle.
print(f"Creating mock model file at: {model_path}")
with open(model_path, "wb") as f:
    pickle.dump(mock_model, f)

print("✅ Mock model file 'ransomware_model.pkl' created successfully.")