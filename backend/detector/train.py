cat > backend/detector/train.py <<'EOF'
import os, joblib, numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def train_dummy():
    rng = np.random.RandomState(42)
    # features: [entropy, size_kb]
    # Safe files (low entropy, small size typical text)
    X_safe = rng.normal(loc=[2.0, 20], scale=[0.5, 10], size=(400,2))
    # Malicious-ish (higher entropy, larger)
    X_bad  = rng.normal(loc=[7.0, 200], scale=[0.8, 80], size=(200,2))
    X = np.vstack([X_safe, X_bad])
    y = np.array([0]*400 + [1]*200)  # 0 safe, 1 malicious
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    print("Train score:", clf.score(X_test, y_test))
    joblib.dump(clf, MODEL_PATH)
    print("Saved model to", MODEL_PATH)

if __name__ == "__main__":
    train_dummy()
EOF
