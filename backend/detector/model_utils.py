cat > backend/detector/model_utils.py <<'EOF'
import os, joblib, numpy as np, math
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def file_entropy(path):
    b = open(path, "rb").read()
    if not b:
        return 0.0
    from collections import Counter
    freq = Counter(b)
    probs = [v/len(b) for v in freq.values()]
    ent = -sum(p * math.log2(p) for p in probs if p>0)
    return float(ent)

def extract_features(path):
    size_kb = os.path.getsize(path)/1024.0
    ent = file_entropy(path)
    return [ent, size_kb]

def predict_file(path):
    model = load_model()
    features = extract_features(path)
    arr = np.array([features])
    if model is None:
        # fallback: simple rule
        score = 1.0 if features[0] > 6.0 else 0.0
        pred = int(score)
        return {"pred": pred, "score": float(score), "entropy": features[0], "size_kb": features[1]}
    prob = float(model.predict_proba(arr)[0,1])
    pred = int(model.predict(arr)[0])
    return {"pred": pred, "score": prob, "entropy": features[0], "size_kb": features[1]}
EOF
