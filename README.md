PASSWORD STRENGTH AI

A modular machine learning classifier that evaluates password security by extracting structural features (character distribution, uppercase validation, variety, and Shannon entropy), processing them through a trained Scikit-Learn Random Forest model, and classifying strength into distinct tiers alongside actionable improvement feedback.

**PROJECT STRUCTURE**:-

| Path | Description |
| :--- | :--- |
| `main.py` | CLI interface for interactive evaluation and testing |
| `classifier.py` | Feature extraction, Shannon entropy calculation, and ML model logic |
| `requirements.txt` | Project dependencies |
| `README.md` | Documentation and portfolio instructions |
| `assets/demo.png` | Terminal output screenshot showing password evaluation and feedback |

**QUICK SETUP & USAGE**:-

1. Install dependencies:
   `pip install -r requirements.txt`

2. Run the script:
   `python main.py`

**REQUIREMENTS**:-

* numpy
* scikit-learn
