import os

# 🔥 Récupère le chemin absolu de SecLists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECLISTS_PATH = os.path.join(BASE_DIR, "SecLists", "Fuzzing")

# ✅ Dossier où seront stockés les rapports
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# ✅ Vérifie si les dossiers existent, sinon les crée
os.makedirs(SECLISTS_PATH, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# 🔥 Définition des injections avec les bons fichiers de SecLists
INJECTIONS = {
    "SQL": [
        os.path.join(SECLISTS_PATH, "SQLi", "quick-SQLi.txt"),
        os.path.join(SECLISTS_PATH, "SQLi", "Generic-SQLi.txt"),
        os.path.join(SECLISTS_PATH, "SQLi", "Generic-BlindSQLi.fuzzdb.txt")
    ],
    "XSS": [
        os.path.join(SECLISTS_PATH, "Polyglots", "XSS-Polyglots.txt"),
        os.path.join(SECLISTS_PATH, "XSS", "XSS-Polyglots-Dmiessler.txt"),
        os.path.join(SECLISTS_PATH, "FuzzingStrings-SkullSecurity.org.txt")
    ],
    "HTML": [
        os.path.join(SECLISTS_PATH, "HTML5sec-Injections-Jhaddix.txt")
    ],
    "XML": [
        os.path.join(SECLISTS_PATH, "XML-FUZZ.txt"),
        os.path.join(SECLISTS_PATH, "XXE-Fuzzing.txt")
    ],
    "Command": [
        os.path.join(SECLISTS_PATH, "command-injection-commix.txt")
    ]
}

# Configuration du scanner
MAX_THREADS = 200  # 🔥 Augmente le nombre de requêtes simultanées
TIMEOUT = 1  # Réduit le timeout pour accélérer le scan

print(f"✅ Payloads trouvés dans : {SECLISTS_PATH}")
print(f"✅ Configuration chargée : {BASE_DIR}")
