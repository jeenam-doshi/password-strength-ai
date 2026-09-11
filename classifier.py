import math
import string
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class PasswordStrengthClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self._train_synthetic()

    def _extract_features(self, password: str) -> list:
        length = len(password)
        lower = sum(1 for c in password if c in string.ascii_lowercase)
        upper = sum(1 for c in password if c in string.ascii_uppercase)
        digits = sum(1 for c in password if c in string.digits)
        symbols = sum(1 for c in password if c in string.punctuation)
        
        # Shannon Entropy Estimation
        char_space = 0
        if lower > 0: char_space += 26
        if upper > 0: char_space += 26
        if digits > 0: char_space += 10
        if symbols > 0: char_space += len(string.punctuation)
        
        entropy = length * math.log2(char_space) if char_space > 0 and length > 0 else 0
        has_sequence = 1 if any(seq in password.lower() for seq in ['123', 'abc', 'password', 'qwerty']) else 0
        
        return [length, lower, upper, digits, symbols, entropy, has_sequence]

    def _train_synthetic(self):
        np.random.seed(42)
        X, y = [], []
        
        # Weak samples (simulating missing cases like zero uppercase)
        for _ in range(300):
            length = np.random.randint(4, 8)
            feats = [length, length*0.6, 0, length*0.2, 0, length * 2.5, 1]
            X.append(feats)
            y.append(0)
            
        # Moderate samples
        for _ in range(300):
            length = np.random.randint(8, 12)
            feats = [length, length*0.4, length*0.3, length*0.2, length*0.1, length * 4.0, 0]
            X.append(feats)
            y.append(1)
            
        # Strong samples
        for _ in range(300):
            length = np.random.randint(12, 20)
            feats = [length, length*0.3, length*0.3, length*0.2, length*0.2, length * 5.5, 0]
            X.append(feats)
            y.append(2)
            
        self.model.fit(X, y)

    def predict(self, password: str) -> dict:
        features = self._extract_features(password)
        pred = self.model.predict([features])[0]
        
        labels = {0: "Weak ❌", 1: "Moderate ⚠️", 2: "Strong 🛡️"}
        
        feedback = []
        if len(password) < 10:
            feedback.append("Increase length to at least 10-12 characters.")
        if features[2] == 0:  # Upper count check
            feedback.append("Add at least one uppercase letter (A-Z).")
        if features[3] == 0:  # Digit count check
            feedback.append("Add numeric digits (0-9).")
        if features[4] == 0:  # Symbol count check
            feedback.append("Include special symbols (!@#$%).")
            
        return {
            "strength": labels[pred],
            "entropy_bits": round(features[5], 2),
            "feedback": feedback if feedback else ["Looks solid! No major weaknesses found."]
        }