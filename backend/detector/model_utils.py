import os
import math
import numpy as np

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = [0] * 256
    for b in data:
        counts[b] += 1
    probs = [c / len(data) for c in counts if c > 0]
    return -sum(p * math.log2(p) for p in probs)

def extract_features(filepath: str) -> np.ndarray:
    # read beginning of file for quick static features
    with open(filepath, "rb") as f:
        sample = f.read(4096)  # first 4KB
    entropy = calculate_entropy(sample)
    size = os.path.getsize(filepath)
    checksum = sum(sample) % 256 if sample else 0
    return np.array([size, entropy, checksum], dtype=float)
