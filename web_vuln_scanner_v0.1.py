from scanner import load_payloads, test_injection_with_progress, analyze_results, save_detailed_report
from config import INJECTIONS

def main():
    target_url = input("Entrez l'URL cible : ").strip()
    selected = input(f"Types d'injections ({', '.join(INJECTIONS.keys())}) : ").split(",")

    for injection_type in selected:
        injection_type = injection_type.strip()
        if injection_type in INJECTIONS:
            payloads = load_payloads(INJECTIONS[injection_type])
            if payloads:
                results = test_injection_with_progress(target_url, payloads, injection_type)
                stats = analyze_results(results)
                save_detailed_report(injection_type, stats)
            else:
                print(f"Aucun payload pour {injection_type}.")
        else:
            print(f"Type inconnu : {injection_type}")

if __name__ == "__main__":
    main()
