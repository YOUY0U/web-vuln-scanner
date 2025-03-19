import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os
import scanner
from config import INJECTIONS, REPORTS_DIR
from crawler import crawl_site
from scanner import load_payloads, test_injection_with_progress, analyze_results, save_detailed_report
from ai_analysis import generate_ai_report  # ✅ Ajout de l'IA pour l'analyse automatique

# 🎨 Couleurs et styles pour une meilleure apparence
BG_COLOR = "#1E1E2E"
TEXT_COLOR = "#EAEAEA"
BUTTON_COLOR = "#4A90E2"
AI_BUTTON_COLOR = "#8E44AD"
TITLE_FONT = ("Arial", 18, "bold")
LABEL_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 12, "bold")


def show_report(stats, report_type):
    """Affiche le rapport généré dans une fenêtre"""
    report_window = tk.Toplevel(root)
    report_window.title(f"📄 Rapport {report_type}")
    report_window.geometry("700x600")
    report_window.configure(bg=BG_COLOR)

    tk.Label(report_window, text=f"📌 Rapport : {report_type}", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    text_area = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 12), bg="#2C2C3E", fg=TEXT_COLOR)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # 📊 Affichage du rapport
    text_area.insert(tk.END, f"=== Rapport {report_type} ===\n")
    text_area.insert(tk.END, f"📄 Pages testées : {stats['total']}\n")
    text_area.insert(tk.END, f"✔️ Succès : {stats['success']}\n")
    text_area.insert(tk.END, f"❌ Erreurs détectées : {stats['errors']}\n")
    text_area.insert(tk.END, f"🚫 Bloqués : {stats['blocked']}\n\n")

    if stats["errors"] > 0:
        text_area.insert(tk.END, "=== Détails des Vulnérabilités ===\n")
        for vuln in stats["details"]:
            text_area.insert(tk.END, f"\n🔗 URL: {vuln['url']}\n")
            text_area.insert(tk.END, f"💉 Payload: {vuln['payload']}\n")
            text_area.insert(tk.END, f"⚠️ Réponse: {vuln['response'][:300]}...\n")
            text_area.insert(tk.END, "=" * 40 + "\n")

    text_area.config(state=tk.DISABLED)  # Empêcher la modification

    tk.Button(report_window, text="📁 Enregistrer", font=BUTTON_FONT,
              bg=BUTTON_COLOR, fg=TEXT_COLOR,
              command=lambda: save_report_to_file(stats, report_type)).pack(pady=5)

    tk.Button(report_window, text="🤖 Analyser avec IA", font=BUTTON_FONT,
              bg=AI_BUTTON_COLOR, fg=TEXT_COLOR,
              command=lambda: show_ai_report(report_type)).pack(pady=5)

    tk.Button(report_window, text="❌ Fermer", font=BUTTON_FONT,
              bg="red", fg=TEXT_COLOR, command=report_window.destroy).pack(pady=5)


def save_report_to_file(stats, report_type):
    """Sauvegarde le rapport dans un fichier"""
    filename = os.path.join(REPORTS_DIR, f"{report_type}_report.txt")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"=== Rapport {report_type} ===\n")
        file.write(f"📄 Pages testées : {stats['total']}\n")
        file.write(f"✔️ Succès : {stats['success']}\n")
        file.write(f"❌ Erreurs détectées : {stats['errors']}\n")
        file.write(f"🚫 Bloqués : {stats['blocked']}\n\n")

    messagebox.showinfo("✅ Enregistré", f"Le rapport {report_type} a été sauvegardé dans {filename}")


def show_ai_report(report_type):
    """Affiche le rapport d'analyse IA"""
    ai_report_content = generate_ai_report(report_type)

    ai_window = tk.Toplevel(root)
    ai_window.title(f"🤖 Rapport IA - {report_type}")
    ai_window.geometry("700x500")
    ai_window.configure(bg=BG_COLOR)

    tk.Label(ai_window, text=f"🤖 Rapport IA : {report_type}", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    text_area = tk.Text(ai_window, wrap=tk.WORD, font=("Arial", 12), bg="#2C2C3E", fg=TEXT_COLOR)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, ai_report_content)
    text_area.config(state=tk.DISABLED)

    tk.Button(ai_window, text="❌ Fermer", font=BUTTON_FONT,
              bg="red", fg=TEXT_COLOR, command=ai_window.destroy).pack(pady=5)


def start_scan():
    """Lance le scan en arrière-plan"""
    url = url_entry.get().strip()
    selected = listbox.curselection()
    types = [listbox.get(i) for i in selected]

    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL cible.")
        return
    if not types:
        messagebox.showerror("Erreur", "Veuillez sélectionner au moins un type d'injection.")
        return

    scan_button.config(state=tk.DISABLED)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"🔍 Scan en cours pour {url}...\n")

    threading.Thread(target=run_scan, args=(url, types), daemon=True).start()


def run_scan(url, types):
    """Scanne le site et détecte les vulnérabilités"""
    urls = crawl_site(url, max_pages=10)

    reports = {}
    for injection_type in types:
        payloads = scanner.load_payloads(INJECTIONS.get(injection_type, []))
        if payloads:
            results = scanner.test_injection_with_progress(urls, payloads, injection_type)
            stats = scanner.analyze_results(results)
            scanner.save_detailed_report(injection_type, stats)
            reports[injection_type] = stats
        else:
            print(f"❌ Aucun payload trouvé pour {injection_type}")

    scan_button.config(state=tk.NORMAL)

    for injection_type, content in reports.items():
        show_report(content, injection_type)


# 🌟 Interface graphique améliorée
root = tk.Tk()
root.title("🛡 WebVuln Scanner")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

tk.Label(root, text="🔍 Web Vulnerability Scanner", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

url_entry = tk.Entry(root, width=50, font=("Arial", 14))
url_entry.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 14), width=40, height=6, bg="#2C2C3E", fg=TEXT_COLOR)
for inj in INJECTIONS.keys():
    listbox.insert(tk.END, inj)
listbox.pack()

scan_button = tk.Button(root, text="🚀 Démarrer Scan", font=BUTTON_FONT,
                        bg=BUTTON_COLOR, fg=TEXT_COLOR, command=start_scan)
scan_button.pack(pady=10)

result_text = tk.Text(root, height=10, font=("Arial", 12), bg="#2C2C3E", fg=TEXT_COLOR)
result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
