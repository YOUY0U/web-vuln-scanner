# Web Vulnerability Scanner
<p align="center">
  <img src="./logo.png" alt="Logo du projet" width="200">
  <br>
  <a href="https://github.com/YOUY0U/web-vuln-scanner/actions"><img src="https://img.shields.io/github/actions/workflow/status/YOUY0U/web-vuln-scanner/tests.yml?label=Tests" alt="Statut des tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licence-MIT-blue.svg" alt="Licence MIT"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8%2B-green.svg" alt="Python 3.8+"></a>
</p>

Outil open-source de détection de vulnérabilités web (SQLi, XSS, Command Injection, etc.) conforme aux bonnes pratiques OWASP. Conçu pour les développeurs, pentesters et équipes de sécurité.

> **⚠️ Avertissement légal**  
> Cet outil doit exclusivement être utilisé :
> - Sur des systèmes dont vous possédez l'autorisation explicite
> - À des fins éducatives en environnement contrôlé
> - Dans le cadre de tests de sécurité autorisés
> 
> Les utilisateurs sont seuls responsables de leurs actions. Consultez les [directives légales](LEGAL.md) avant toute utilisation.

---

## Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Exemples](#exemples)
  - [Options](#options)
- [Configuration avancée](#configuration-avancée)
- [Roadmap](#roadmap)
- [Contribution](#contribution)
- [Sécurité](#sécurité)
- [Licence](#licence)
- [Communauté](#communauté)

---

## Présentation

**Web Vulnerability Scanner** est une solution complète d'analyse de sécurité web permettant d'identifier les vulnérabilités courantes dans les applications modernes. Particulièrement adapté pour :

- Les audits de sécurité pré-déploiement
- L'apprentissage des techniques d'injection
- Les tests automatisés en CI/CD
- La recherche proactive de failles

Support technique :
- Compatible avec les frameworks modernes (React, Angular, Vue)
- Analyse des API REST/GraphQL
- Détection des configurations serveur risquées

---

## Fonctionnalités

### 🔍 Détections principales
- **Injections SQL** (Union-based, Blind, Time-based)
- **Cross-Site Scripting (XSS)** (Reflected, Stored, DOM-based)
- **Command/OS Injection**
- **HTML Injection**
- **Fichiers sensibles** (robots.txt, .env, backups)
- **En-têtes de sécurité manquants** (CSP, HSTS, X-Content-Type)

### ⚙️ Fonctionnalités avancées
- **Moteur de payloads dynamiques** avec 1500+ signatures
- **Personnalisation avancée** via fichiers YAML/JSON
- **Multi-threading** contrôlable (jusqu'à 50 threads)
- **Rapports détaillés** (HTML, PDF, JSON)
- **Mode furtif** (random User-Agent, délais variables)
- **Intégration CI/CD** (Jenkins, GitLab CI, GitHub Actions)
- **Proxy support** (Burp Suite, OWASP ZAP)

### 📊 Sortie des résultats
- Classement par criticité (CRITIQUE, HAUTE, MOYENNE, INFO)
- Conseils de correction détaillés
- Références CWE/CVE associées
- Statistiques d'analyse complètes

---

## Prérequis

- Python 3.8+
- Pipenv (recommandé)
- Bibliothèques système : libxml2, libxslt
- Navigateur Chromium (pour les tests XSS avancés)

---

## Installation

### Méthode standard
```bash
git clone https://github.com/YOUY0U/web-vuln-scanner.git
cd web-vuln-scanner
pip install -r requirements.txt
