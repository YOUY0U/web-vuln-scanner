# Web Vulnerability Scanner
<p align="center">
  <img src="./logo.png" alt="Logo du projet" width="200">
  <br>
  <a href="https://github.com/YOUY0U/web-vuln-scanner/actions"><img src="https://img.shields.io/github/actions/workflow/status/YOUY0U/web-vuln-scanner/tests.yml?label=Tests" alt="Statut des tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licence-MIT-blue.svg" alt="Licence MIT"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8%2B-green.svg" alt="Python 3.8+"></a>
</p>

Outil avancé de détection de vulnérabilités web (SQLi, XSS, Command Injection, etc.) conforme aux bonnes pratiques OWASP. Conçu pour les développeurs, pentesters et équipes de sécurité.

> **⚠️ Avertissement légal**  
> Cet outil doit exclusivement être utilisé :
> - Sur des systèmes dont vous possédez l'autorisation explicite.
> - À des fins éducatives en environnement contrôlé.
> - Dans le cadre de tests de sécurité autorisés.
>
> Les utilisateurs sont entièrement responsables de leurs actions. Consultez les [directives légales](LEGAL.md) avant toute utilisation.

---

## Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Roadmap](#roadmap)
- [Licence](#licence)

---

## Présentation

**Web Vulnerability Scanner** est un outil puissant et automatisé d'analyse de sécurité web permettant d'identifier et d'exploiter les vulnérabilités courantes. Il est optimisé pour :

- Audits de sécurité pré-déploiement.
- Apprentissage et formation à la cybersécurité.
- Tests automatisés intégrés aux pipelines CI/CD.
- Recherche proactive de failles et renforcement des applications.

Support technique :
- Compatible avec les frameworks modernes (React, Angular, Vue).
- Analyse des API REST/GraphQL.
- Détection des configurations serveur risquées et mauvaises pratiques.

---

## Fonctionnalités

### 🔍 Détection des vulnérabilités
- **Injections SQL** (Union-based, Blind, Time-based).
- **Cross-Site Scripting (XSS)** (Reflected, Stored, DOM-based).
- **Command/OS Injection**.
- **HTML Injection**.

### ⚙️ Fonctionnalités avancées
- **Moteur de payloads dynamiques** avec 1500+ signatures.
- **Personnalisation avancée** via fichiers YAML/JSON.
- **Multi-threading** contrôlable (jusqu'à 250 threads).
- **Rapports détaillés** (HTML, PDF, JSON).
- **Mode furtif** (random User-Agent, délais variables).

### 📊 Sortie des résultats
- Classement des vulnérabilités par criticité (CRITIQUE, HAUTE, MOYENNE, INFO).
- Conseils de correction détaillés.
- Références CWE/CVE associées.
- Statistiques d'analyse complètes.

---

## Prérequis

- Python 3.8+.
- Pipenv (recommandé).
- Bibliothèques système : libxml2, libxslt.
- Navigateur Chromium (pour les tests XSS avancés).

---

## Installation

### Installation standard
```bash
git clone https://github.com/YOUY0U/web-vuln-scanner.git
cd web-vuln-scanner
pip install -r requirements.txt
```

---

## Roadmap

- [ ] **v0.1** - Création d’un scanner basique supportant les injections SQL, XSS et Command Injection avec un seul payload par type.
- [ ] **v0.2** - Extension aux injections HTML avec un payload spécifique.
- [ ] **v0.3** - Intégration de la base de données SecLists (1.7 Go de payloads) pour une couverture étendue.
- [ ] **v0.4** - Ajout d'une validation des entrées utilisateur (vérification des URL, gestion des erreurs).
- [ ] **v0.5** - Possibilité de créer des payloads personnalisés.
- [ ] **v0.6** - Optimisation des performances grâce au multi-threading (ThreadPoolExecutor).
- [ ] **v0.7** - Support des requêtes HTTP GET et POST pour une détection plus complète.
- [ ] **v0.8** - Amélioration de l'affichage des résultats avec Plotly et Termcolor.
- [ ] **v0.9** - Développement d'une interface graphique interactive.
- [ ] **v1.0** - Intégration d'une IA (ChatGPT API) pour suggérer des solutions et calculer les scores CVSS.

---

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
