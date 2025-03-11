import openai
import os
from config import REPORTS_DIR

# 🔑 Mets ta propre clé API OpenAI ici
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def analyze_vulnerabilities(report_content):
    """Utilise ChatGPT pour analyser et résumer les vulnérabilités trouvées."""
    prompt = f"""
    Voici un rapport de vulnérabilités détectées :

    {report_content}

    📌 Analyse ce rapport et identifie :
    1️⃣ Les vulnérabilités les plus critiques
    2️⃣ Les risques potentiels
    3️⃣ Des recommandations pour corriger ces failles

    Donne-moi une analyse détaillée et structurée.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Tu es un expert en cybersécurité."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Erreur avec l'IA : {str(e)}"

def generate_ai_report(report_type):
    """Génère un rapport IA basé sur le scan."""
    report_path = os.path.join(REPORTS_DIR, f"{report_type}_report.txt")

    if not os.path.exists(report_path):
        return f"❌ Aucun rapport trouvé pour {report_type}."

    with open(report_path, "r", encoding="utf-8") as file:
        report_content = file.read()

    # 🔥 Analyse IA
    ai_report = analyze_vulnerabilities(report_content)

    # 📁 Sauvegarde du rapport IA
    ai_report_path = os.path.join(REPORTS_DIR, f"{report_type}_ai_report.txt")
    with open(ai_report_path, "w", encoding="utf-8") as file:
        file.write(ai_report)

    return f"✅ Rapport IA généré : {ai_report_path}"
