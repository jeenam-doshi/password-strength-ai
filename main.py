from classifier import PasswordStrengthClassifier

def main():
    print("=== AI PASSWORD STRENGTH ANALYZER ===")
    classifier = PasswordStrengthClassifier()
    
    while True:
        pwd = input("\nEnter a password to test (or type 'exit' to quit): ").strip()
        if pwd.lower() == 'exit':
            break
        if not pwd:
            continue
            
        result = classifier.predict(pwd)
        print(f"\n[Classification]: {result['strength']}")
        print(f"[Shannon Entropy]: {result['entropy_bits']} bits")
        print("[Recommendations]:")
        for tip in result['feedback']:
            print(f" - {tip}")

if __name__ == "__main__":
    main()