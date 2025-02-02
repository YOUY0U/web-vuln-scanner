import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # Pour la barre de progression
import time

# Chemin vers le dossier contenant SecLists
SECLISTS_PATH = "C:/Users/Youssef/Documents/Transformation-Digitales-2/Projet/Project - WebVuln Scanner/SecLists/Fuzzing/"
INJECTIONS = {
    "SQL": [
        f"{SECLISTS_PATH}SQLi/quick-SQLi.txt",
        f"{SECLISTS_PATH}SQLi/Generic-SQLi.txt",
        f"{SECLISTS_PATH}SQLi/Generic-BlindSQLi.fuzzdb.txt"
    ],
    "XSS": [f"{SECLISTS_PATH}HTML5sec-Injections-Jhaddix.txt"],
    "HTML": [f"{SECLISTS_PATH}template-engines-expression.txt"],
    "XML": [f"{SECLISTS_PATH}XML-FUZZ.txt"],
    "Command": [f"{SECLISTS_PATH}command-injection-commix.txt"]
}

def load_payloads(file_paths, limit=None):
    """Charge les payloads depuis plusieurs fichiers avec une limite optionnelle."""
    payloads = []
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                payloads.extend([line.strip() for line in file if line.strip()])
        except FileNotFoundError:
            print(f"Erreur : Fichier introuvable - {file_path}")
        except Exception as e:
            print(f"Erreur lors du chargement du fichier {file_path}: {e}")
    return payloads[:limit] if limit else payloads

def test_payload(payload, url):
    """Teste un payload sur une URL donnée."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, params={"input": payload}, headers=headers, timeout=2)
        return payload, response.status_code
    except requests.RequestException as e:
        return payload, str(e)

def test_injection_with_progress(url, payloads, injection_type):
    """Teste les payloads avec une barre de progression."""
    print(f"\n[+] Début des tests pour {injection_type} ({len(payloads)} payloads)...")
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Barre de progression avec tqdm
        for payload, status in tqdm(executor.map(lambda p: test_payload(p, url), payloads), total=len(payloads), desc=f"Test {injection_type}"):
            results.append((payload, status))
    print(f"[+] Tests {injection_type} terminés !")
    return results

def analyze_results(results):
    """Analyse les résultats pour générer des statistiques."""
    total = len(results)
    success = sum(1 for _, status in results if str(status).startswith("2"))  # Statuts HTTP 2xx
    errors = sum(1 for _, status in results if isinstance(status, str) and "Exception" in status)
    blocked = total - success - errors  # Tout autre code HTTP
    return {
        "total": total,
        "success": success,
        "errors": errors,
        "blocked": blocked,
        "details": results
    }

def save_detailed_report(injection_type, stats, filename):
    """Sauvegarde les résultats détaillés dans un fichier."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"=== Rapport Détaillé pour {injection_type} ===\n")
        f.write(f"Nombre total de payloads : {stats['total']}\n")
        f.write(f"Payloads réussis (HTTP 2xx) : {stats['success']}\n")
        f.write(f"Erreurs réseau/d'exception : {stats['errors']}\n")
        f.write(f"Payloads bloqués ou autres réponses : {stats['blocked']}\n\n")
        f.write("=== Détails des Tests ===\n")
        for payload, status in stats["details"]:
            f.write(f"Payload: {payload} | Statut: {status}\n")
    print(f"[+] Rapport détaillé sauvegardé dans : {filename}")

def save_summary_report(summary, filename):
    """Sauvegarde un rapport général dans un fichier."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== Rapport Général ===\n")
        for injection_type, stats in summary.items():
            f.write(f"\n{injection_type}:\n")
            f.write(f"  Total Payloads : {stats['total']}\n")
            f.write(f"  Succès (HTTP 2xx) : {stats['success']}\n")
            f.write(f"  Erreurs : {stats['errors']}\n")
            f.write(f"  Bloqués : {stats['blocked']}\n")
    print(f"[+] Rapport général sauvegardé dans : {filename}")

def main():
    target_url = input("Entrez l'URL cible (e.g., https://example.com): ").strip()

    # Choix des types d'injections
    print("Choisissez les types d'injections (séparés par des virgules) :")
    print(", ".join(INJECTIONS.keys()))
    selected = input("Types : ").split(",")

    # Nombre de payloads à tester (facultatif, utile pour limiter les tests longs)
    limit = input("Nombre de payloads max à tester (laisser vide pour tous) : ")
    limit = int(limit) if limit.isdigit() else None

    summary = {}  # Pour le rapport général
    start_time = time.time()  # Chronométrage
    for injection_type in selected:
        injection_type = injection_type.strip()
        if injection_type in INJECTIONS:
            payloads = load_payloads(INJECTIONS[injection_type], limit)
            if payloads:
                results = test_injection_with_progress(target_url, payloads, injection_type)
                stats = analyze_results(results)
                summary[injection_type] = stats
                save_detailed_report(injection_type, stats, f"{injection_type}_detailed_report.txt")
            else:
                print(f"[-] Aucun payload chargé pour {injection_type}.")
        else:
            print(f"[-] Type d'injection non reconnu : {injection_type}")
    save_summary_report(summary, "general_report.txt")
    print(f"Temps total d'exécution : {time.time() - start_time:.2f} secondes.")

if __name__ == "__main__":
    main()
