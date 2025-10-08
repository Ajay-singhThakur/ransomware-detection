import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

BASE = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE, "model.joblib")

# NOTE: Demo training data (very small toy dataset).
# Replace with a real labeled dataset for actual detection.
X = np.array([
    [1000, 3.5, 50],
    [2048, 7.5, 30],
    [512, 1.2, 70],
    [4096, 8.1, 90],
    [8192, 7.8, 120],
    [256, 0.9, 20]
], dtype=float)

y = ["Safe", "Ransomware", "Safe", "Ransomware", "Ransomware", "Safe"]

clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X, y)

joblib.dump(clf, MODEL_PATH)
print(f"Trained demo model written to {MODEL_PATH}")
