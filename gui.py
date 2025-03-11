import tkinter as tk
from tkinter import messagebox
import threading
import scanner
from config import INJECTIONS
from crawler import crawl_site
from ai_analysis import generate_ai_report

# Couleurs et styles
BG_COLOR = "#2C3E50"
TEXT_COLOR = "#ECF0F1"
BUTTON_COLOR = "#3498DB"
AI_BUTTON_COLOR = "#8E44AD"

def show_report(stats, report_type):
    """Affiche automatiquement le rapport généré dans une nouvelle fenêtre."""
    report_window = tk.Toplevel(root)
    report_window.title(f"📄 Rapport {report_type}")
    report_window.geometry("900x700")
    report_window.configure(bg=BG_COLOR)

    tk.Label(report_window, text=f"📌 Rapport : {report_type}", font=("Arial", 14, "bold"),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    text_area = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 10), bg="#1C2833", fg=TEXT_COLOR)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # 🔥 Affichage amélioré
    text_area.insert(tk.END, f"=== Rapport {report_type} ===\n")
    text_area.insert(tk.END, f"Total Pages Testées : {stats['total']}\n")
    text_area.insert(tk.END, f"✔️ Succès : {stats['success']}\n")
    text_area.insert(tk.END, f"❌ Erreurs détectées : {stats['errors']}\n")
    text_area.insert(tk.END, f"🚫 Bloqués : {stats['blocked']}\n\n")

    text_area.config(state=tk.DISABLED)

    tk.Button(report_window, text="🤖 Analyse IA", font=("Arial", 12),
              bg=AI_BUTTON_COLOR, fg=TEXT_COLOR,
              command=lambda: show_ai_report(report_type)).pack(pady=5)
    tk.Button(report_window, text="❌ Fermer", font=("Arial", 12),
              bg="red", fg=TEXT_COLOR, command=report_window.destroy).pack(pady=5)

def show_ai_report(report_type):
    """Affiche le rapport généré par l'IA."""
    ai_report_content = generate_ai_report(report_type)

    ai_window = tk.Toplevel(root)
    ai_window.title(f"🤖 Rapport IA - {report_type}")
    ai_window.geometry("900x700")
    ai_window.configure(bg=BG_COLOR)

    tk.Label(ai_window, text=f"🤖 Rapport IA : {report_type}", font=("Arial", 14, "bold"),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    text_area = tk.Text(ai_window, wrap=tk.WORD, font=("Arial", 10), bg="#1C2833", fg=TEXT_COLOR)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, ai_report_content)
    text_area.config(state=tk.DISABLED)

    tk.Button(ai_window, text="❌ Fermer", font=("Arial", 12),
              bg="red", fg=TEXT_COLOR, command=ai_window.destroy).pack(pady=5)

def start_scan():
    """Lance le scan en arrière-plan."""
    url = url_entry.get().strip()
    selected = listbox.curselection()
    types = [listbox.get(i) for i in selected]

    if not url or not types:
        messagebox.showerror("Erreur", "Veuillez entrer une URL et sélectionner un type d'injection.")
        return

    scan_button.config(state=tk.DISABLED)
    threading.Thread(target=run_scan, args=(url, types), daemon=True).start()

def run_scan(url, types):
    """Scanne tout le site et détecte les vulnérabilités."""
    urls = crawl_site(url, max_pages=10)

    for injection_type in types:
        payloads = scanner.load_payloads(INJECTIONS.get(injection_type, []))
        results = scanner.test_injection_with_progress(urls, payloads, injection_type)
        stats = scanner.analyze_results(results)
        scanner.save_detailed_report(injection_type, stats)
        show_report(stats, injection_type)

    scan_button.config(state=tk.NORMAL)

# Interface
root = tk.Tk()
root.title("🛡 WebVuln Scanner")
root.geometry("900x700")
root.configure(bg=BG_COLOR)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5, bg="#34495E", fg=TEXT_COLOR)
for inj in INJECTIONS.keys():
    listbox.insert(tk.END, inj)
listbox.pack()
scan_button = tk.Button(root, text="🚀 Démarrer Scan", bg=BUTTON_COLOR, fg=TEXT_COLOR, command=start_scan)
scan_button.pack(pady=10)

root.mainloop()
