# Web Vulnerability Scanner

Un outil open-source pour tester les vulnérabilités web (SQLi, XSS, Command Injection, etc.) dans un environnement contrôlé et légal.

> **Avertissement :**  
> L’utilisation de cet outil doit se faire dans le respect de la loi et de l’éthique. Ne l’utilisez que sur des sites ou applications dont vous possédez les droits, ou à des fins purement éducatives. L’auteur ne saurait être tenu responsable de toute utilisation malveillante.

---

## Table des matières

1. [Présentation](#présentation)  
2. [Fonctionnalités](#fonctionnalités)  
3. [Installation](#installation)  
4. [Utilisation](#utilisation)  
5. [Roadmap et versions](#roadmap-et-versions)  
6. [Contribution](#contribution)  
7. [Licence](#licence)  

---

## Présentation

**Web Vulnerability Scanner** est un scanner de vulnérabilités web simple d’utilisation, conçu pour repérer rapidement les failles courantes dans les applications web. Il prend notamment en charge :

- Les injections SQL (SQLi)  
- Les failles XSS (Cross-Site Scripting)  
- Les injections de commande (Command Injection)

L’objectif est de proposer un outil facile à configurer et à personnaliser grâce à des payloads externes, afin de faciliter le travail de test et d’audit de sécurité.

---

## Fonctionnalités

- **Support des injections SQL, XSS et Command Injection**  
  Détecte automatiquement les champs susceptibles d’être vulnérables et tente des injections malveillantes pour vérifier la présence de failles.

- **Chargement de payloads personnalisés**  
  Permet d’ajouter vos propres chaînes d’attaque via des fichiers `.txt`. Vous pouvez ainsi étendre les tests à des vulnérabilités spécifiques ou à de nouvelles techniques.

- **Threading (exécution parallèle)**  
  Accélère les scans en exécutant plusieurs tests en parallèle.

- **Rapport détaillé** *(optionnel selon l’implémentation)*  
  Génération d’un rapport qui récapitule les vulnérabilités détectées, leur gravité potentielle, et des recommandations pour y remédier.

---

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
