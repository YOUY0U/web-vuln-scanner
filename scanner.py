import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from config import INJECTIONS, TIMEOUT, MAX_THREADS, REPORTS_DIR
import os

def test_payload(payload, url):
    """Teste un payload en GET et en POST et renvoie les détails."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        target_url = url

        # Test GET
        response_get = requests.get(target_url, params={"search": payload}, headers=headers, timeout=TIMEOUT)
        response_post = requests.post(target_url, data={"search": payload}, headers=headers, timeout=TIMEOUT)

        return {
            "url": target_url,
            "payload": payload,
            "status": response_get.status_code if response_get.status_code == 200 else response_post.status_code,
            "response": response_get.text[:500] if response_get.status_code == 200 else response_post.text[:500]  # 🔥 Stocker la vraie réponse
        }

    except requests.RequestException as e:
        return {"url": url, "payload": payload, "status": "ERROR", "response": str(e)}

def test_injection_with_progress(urls, payloads, injection_type):
    """Teste tous les payloads sur chaque URL et retourne les résultats."""
    print(f"\n[+] Test en cours pour {injection_type} sur {len(urls)} pages...")
    results = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for result in tqdm(executor.map(lambda args: test_payload(*args), [(p, u) for u in urls for p in payloads]),
                           total=len(urls) * len(payloads), desc=f"Test {injection_type}"):
            results.append(result)
    return results

def analyze_results(results):
    """Analyse les résultats et extrait les vulnérabilités réelles."""
    total = len(results)
    success = 0
    errors = 0
    blocked = 0
    details = []

    for result in results:
        url, payload, status, response = result["url"], result["payload"], result["status"], result["response"]

        if status == "ERROR" or "error" in response.lower() or "syntax error" in response.lower():
            errors += 1
            details.append({
                "url": url,
                "payload": payload,
                "response": response[:500]  # 🔥 Vraie réponse affichée
            })
        elif str(status).startswith("2"):
            success += 1
        else:
            blocked += 1

    return {
        "total": total,
        "success": success,
        "errors": errors,
        "blocked": blocked,
        "details": details
    }

def save_detailed_report(injection_type, stats):
    """Sauvegarde un rapport détaillé avec les vrais résultats."""
    filename = os.path.join(REPORTS_DIR, f"{injection_type}_detailed_report.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"=== Rapport {injection_type} ===\n")
        f.write(f"Pages testées : {stats['total']}\n")
        f.write(f"✔️ Succès : {stats['success']}\n")
        f.write(f"❌ Erreurs détectées : {stats['errors']}\n")
        f.write(f"🚫 Bloqués : {stats['blocked']}\n\n")

        if stats["errors"] > 0:
            f.write("=== Détails des Vulnérabilités ===\n")
            for vuln in stats["details"]:
                f.write(f"\n🔗 URL: {vuln['url']}\n")
                f.write(f"💉 Payload: {vuln['payload']}\n")
                f.write(f"⚠️ Réponse: {vuln['response']}\n")
                f.write("=" * 40 + "\n")

    print(f"[+] Rapport détaillé sauvegardé dans {filename}")


def load_payloads(file_paths):
    """Charge les payloads depuis plusieurs fichiers de SecLists"""
    payloads = []

    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    payloads.extend([line.strip() for line in file if line.strip()])
            except Exception as e:
                print(f"❌ Erreur de lecture {file_path}: {e}")
        else:
            print(f"⚠️ Fichier introuvable : {file_path}")

    return payloads if payloads else ["' OR '1'='1' --"]  # 🔥 Ajoute un payload par défaut si aucun n'est trouvé
