import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'ransomware_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Warning: Model file not found at {MODEL_PATH}. Using mock prediction.")
    model = None

def predict_ransomware(file_path):
    if not model:
        return "Safe (mock)"

    _, file_extension = os.path.splitext(file_path)
    dangerous_extensions = ['.exe', '.dll', '.bat', '.scr']

    if file_extension.lower() in dangerous_extensions:
        return "Malicious (mock)"
    else:
        return "Safe (mock)"