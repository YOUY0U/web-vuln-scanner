import openai
import os
from config import REPORTS_DIR

# 🔑 Remplace par ta propre clé API OpenAI
OPENAI_API_KEY = "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"  # Mets ta clé API ici
openai.api_key = OPENAI_API_KEY


def analyze_vulnerabilities(report_content):
    """Utilise ChatGPT pour analyser et proposer des solutions aux vulnérabilités."""
    prompt = f"""
    Voici un rapport de vulnérabilités détectées sur un site web :

    {report_content}

    🔍 **Analyse demandée :**
    1️⃣ Identifie les **injections les plus critiques**.
    2️⃣ Évalue les **risques potentiels** pour le site web.
    3️⃣ Propose des **solutions détaillées** pour corriger ces failles.

    Donne-moi une analyse **précise et complète**. 
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # ✅ Utilisation correcte du modèle GPT-4o
            messages=[
                {"role": "system", "content": "Tu es un expert en cybersécurité."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]

    except openai.error.OpenAIError as e:
        return f"❌ Erreur avec l'IA : {str(e)}"


def generate_ai_report(report_type):
    """Génère un rapport intelligent basé sur le scan."""
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

    return ai_report  # ✅ Retourne le rapport pour affichage
