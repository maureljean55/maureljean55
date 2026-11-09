<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1b2a,50:1b3a5c,100:1f6feb&height=210&section=header&text=N%27cho%20Jean%20Maurel%20Monne&fontSize=40&fontColor=ffffff&fontAlignY=36&desc=%C3%89tudiant%20en%20intelligence%20artificielle%20%C2%B7%20ECE%20Paris&descSize=17&descAlignY=56&animation=fadeIn" width="100%" alt="N'cho Jean Maurel Monne" />

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=20&duration=3200&pause=900&color=1F6FEB&center=true&vCenter=true&width=620&lines=Futur+Data+Scientist;Machine+Learning+%C2%B7+SQL+%C2%B7+Python;Applications+web+et+mobiles+de+bout+en+bout;En+recherche+de+stage+ou+d%27alternance" alt="Futur Data Scientist · Machine Learning · Applications web et mobiles" />

<br>

![Recherche](https://img.shields.io/badge/Recherche-Stage%20ou%20alternance-1f6feb?style=for-the-badge)
![Poste visé](https://img.shields.io/badge/Poste%20vis%C3%A9-Data%20Scientist-0e8a5f?style=for-the-badge)
![Mobilité](https://img.shields.io/badge/Mobilit%C3%A9-%C3%8Ele--de--France%20%C2%B7%20France-6f42c1?style=for-the-badge)

</div>

<br>

## 👋 À propos

Actuellement en formation en intelligence artificielle à l'**ECE Paris**, j'oriente mon parcours vers le métier de **Data Scientist**. Je suis convaincu que la valeur d'un modèle tient autant à la rigueur de la collecte des données qu'à la pertinence de leur analyse.

Je m'attache donc à maîtriser toute la chaîne : **modélisation des bases de données → collecte et préparation → apprentissage automatique → mise en production** au service de décisions concrètes. En parallèle, je conçois et déploie des applications web et mobiles complètes, ce qui me permet de comprendre aussi bien les besoins des utilisateurs que les contraintes d'un produit réel.

> [!TIP]
> **Je recherche un stage ou une alternance en tant que Data Scientist**, en Île-de-France ou partout en France.

<br>

## 📊 Projets data & machine learning

<table>
<tr>
<td width="50%" valign="top">

### 🔮 [Prédiction du churn clients](https://github.com/maureljean55/prediction-churn-clients)

Prédire quels clients d'un opérateur télécom vont résilier, pour agir avant leur départ.

- Jeu *Telco Customer Churn* (IBM) · 7 043 clients
- Pipeline scikit-learn : standardisation, one-hot, gestion du déséquilibre
- Régression logistique vs Random Forest

**AUC 0,835** · **8 départs sur 10 détectés**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

</td>
<td width="50%" valign="top">

### 🛍️ [Analyse des ventes d'un magasin](https://github.com/maureljean55/analyse-ventes-magasin)

Comprendre ce qui fait le chiffre d'affaires de 3 boutiques de prêt-à-porter et proposer des actions concrètes.

- ≈ 100 000 transactions nettoyées (doublons, valeurs manquantes)
- Requêtes d'agrégation SQL sur SQLite
- Saisonnalité, jours de la semaine, effet des promotions

**Décembre = 13,5 % du CA** · **Samedi = 24 % du CA hebdo**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)

</td>
</tr>
</table>

<br>

## 🚀 Réalisations

### 🔎 Objely · plateforme de restitution d'objets perdus

Objely met en relation les personnes ayant perdu un objet et celles qui l'ont retrouvé, puis accompagne la restitution jusqu'à son terme.

- **Rapprochement automatique** des déclarations grâce à un score de correspondance calculé directement en SQL (catégorie, couleurs, marque, lieu, date)
- **Base de données robuste** : 80 migrations PostgreSQL, sécurité par ligne (RLS) et index dédiés
- Messagerie en temps réel, vérification de la propriété, planification des restitutions, notifications push
- Assistant de support fondé sur **Gemini**, avec limitation des requêtes pour maîtriser les coûts

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)

[![Code](https://img.shields.io/badge/Code%20source-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/maureljean55/objely)
[![Démo](https://img.shields.io/badge/D%C3%A9mo%20en%20ligne-1f6feb?style=for-the-badge&logo=vercel&logoColor=white)](https://objely.vercel.app)

<details>
<summary><b>L'écosystème Objely : 3 applications complémentaires</b></summary>
<br>

| Application | Rôle | Liens |
|:--|:--|:--|
| **Objely Admin** | Portail de modération : indicateurs en temps réel, gestion des utilisateurs, rapprochements, signalements | [Code](https://github.com/maureljean55/objely-admin) · [Démo](https://objely-admi.vercel.app) |
| **Objely École** | Borne tactile pour lycées et universités, couplée par un code à usage unique | [Code](https://github.com/maureljean55/objely-ecole) · [Démo](https://objely-ecole.vercel.app) |
| **Objely École Admin** | Gestion des objets trouvés pour la vie scolaire | [Code](https://github.com/maureljean55/objely-admin-ecole) |

</details>

---

<table>
<tr>
<td width="50%" valign="top">

### 🧾 [Devis Maker](https://github.com/maureljean55/devis-maker)

Devis et prospection commerciale assistée par IA, conçu pour une **menuiserie à Abidjan** (client réel).

- Chaîne de données : recherche Google → SQLite → messages personnalisés par **Llama 3.3** → export CSV et liens WhatsApp
- Tableau de bord, suivi des prospects, envoi d'e-mails

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square)

[Démo en ligne →](https://devis-maker-njm9.vercel.app)

</td>
<td width="50%" valign="top">

### 🛡️ [DecisionGuard AI](https://github.com/maureljean55/DecisionGuard-AI) <sub>`en cours`</sub>

Plateforme SaaS d'aide à la décision : une **IA multi-agents** analyse une décision d'entreprise, évalue les risques avec un moteur de calcul déterministe, simule des scénarios et produit un rapport (FR/EN).

- API **FastAPI** (Python 3.13) + front Next.js
- Authentification, organisations, isolation des données
- Tests pytest et vitest, environnement Docker complet

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
</table>

<br>

## 🧰 Compétences techniques

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sklearn,postgres,sqlite,mongodb,ts,js,react,nextjs,tailwind,nodejs,fastapi,supabase,redis,docker,vercel,git,github&perline=9" alt="Technologies maîtrisées" />
</p>

| Domaine | Compétences |
|:--|:--|
| **Langages** | Python, SQL, TypeScript, JavaScript, HTML, CSS |
| **Data science** | pandas, NumPy, Matplotlib, scikit-learn, Jupyter · nettoyage et exploration de données · classification, évaluation (AUC, rappel, matrice de confusion) |
| **Données** | PostgreSQL, SQLite, MongoDB · modélisation de bases · requêtes, fonctions et index SQL · collecte (scraping, export CSV) · pipelines de données |
| **IA générative** | Intégration de LLM (Gemini, Llama 3.3 via Groq) · ingénierie de prompts · assistants conversationnels · systèmes multi-agents |
| **Web & mobile** | React, Next.js, Tailwind CSS, React Native, Expo · PWA · temps réel · notifications push · internationalisation |
| **Back-end** | Node.js, FastAPI · API REST · authentification (OAuth, JWT, bcrypt) · sécurité par ligne (RLS) · limitation de requêtes |
| **Cloud & outils** | Supabase, Vercel, Docker, Git, GitHub |
| **En cours d'approfondissement** | Statistiques, Power BI, deep learning |

<br>

## 💡 Ce que j'apporte

<table>
<tr>
<td align="center" width="33%">
<h3>🧭</h3>
<b>Vision d'ensemble</b><br>
<sub>Je conduis un projet de bout en bout, de la conception de la base de données jusqu'à la mise en production.</sub>
</td>
<td align="center" width="33%">
<h3>🤝</h3>
<b>Expérience client</b><br>
<sub>J'ai livré un outil opérationnel répondant aux besoins concrets d'une entreprise.</sub>
</td>
<td align="center" width="33%">
<h3>✅</h3>
<b>Exigence de qualité</b><br>
<sub>Sécurité des données, maîtrise des coûts et documentation soignée font partie de ma démarche.</sub>
</td>
</tr>
</table>

<br>

<div align="center">

*Merci de votre visite ! Je reste à votre disposition pour échanger sur une opportunité de stage ou d'alternance en Data Science.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,50:1b3a5c,100:0d1b2a&height=110&section=footer" width="100%" alt="" />

</div>
