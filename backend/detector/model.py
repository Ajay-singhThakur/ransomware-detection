import numpy as np

# Load model will be saved in train.py
model = None

def extract_features(file_path):
    """
    Simple feature extraction: length of first 1024 bytes + sum modulo 256
    """
    with open(file_path, "rb") as f:
        data = f.read(1024)
    return np.array([len(data), sum(data) % 256])
