# Analyse d'une boutique de sport en ligne — Projet capstone

> Projet de synthèse : nettoyage de données, fusion de sources multiples, statistiques descriptives et exploration graphique, sur un jeu de données e-commerce simulé mais réaliste (formats incohérents, valeurs manquantes, doublons, clés orphelines).

## Contexte

Tu rejoins l'équipe data d'une boutique en ligne togolaise d'articles de sport. On te confie **5 fichiers** extraits de systèmes différents (site web, CRM, ERP fournisseurs), jamais nettoyés, jamais croisés. Ta mission : les rendre exploitables, puis en tirer des réponses concrètes pour trois services de l'entreprise (direction, marketing, qualité).

Ce projet couvre tout ce que tu as appris jusqu'ici : **pandas (nettoyage, fusion), statistiques descriptives codées, visualisation avec matplotlib/seaborn**. Il s'arrête volontairement **avant le machine learning** — ce sera la suite logique une fois ce projet terminé.

## Les données

Tous les fichiers sont dans `data/`. Ils sont **volontairement sales** — c'est le point du projet, pas un bug.

| Fichier | Contenu | Clé |
|---|---|---|
| `clients.csv` | Informations clients | `client_id` |
| `produits.csv` | Catalogue produits | `product_id` |
| `fournisseurs.csv` | Fournisseurs des produits | `supplier_id` |
| `commandes.csv` | Commandes passées en 2025 | `order_id`, référence `client_id` et `product_id` |
| `avis.csv` | Avis clients laissés après livraison | `review_id`, référence `order_id` |

### Dictionnaire des variables

**`clients.csv`**
- `client_id` : identifiant unique
- `nom` : nom complet
- `age` : âge du client
- `sexe` : F / M
- `ville` : ville de résidence
- `date_inscription` : date de création du compte
- `segment` : Nouveau / Régulier / VIP

**`produits.csv`**
- `product_id` : identifiant unique
- `category` : Running / Fitness / Football / Basketball / Yoga / Cyclisme
- `brand` : marque
- `cost_price` : prix d'achat (coût, en k FCFA)
- `list_price` : prix de vente affiché (en k FCFA)
- `stock_quantity` : stock disponible
- `supplier_id` : référence vers `fournisseurs.csv`

**`fournisseurs.csv`**
- `supplier_id` : identifiant unique
- `supplier_name` : nom du fournisseur
- `country` : pays d'origine
- `lead_time_days` : délai d'approvisionnement moyen (jours)
- `reliability_score` : score de fiabilité (0 à 5)

**`commandes.csv`**
- `order_id` : identifiant unique
- `date` : date de la commande
- `client_id` : référence vers `clients.csv`
- `product_id` : référence vers `produits.csv`
- `quantity` : nombre d'articles commandés
- `discount_pct` : pourcentage de réduction appliqué
- `payment_method` : mode de paiement
- `region` : région de livraison
- `delivery_time_days` : délai de livraison réel (jours) — vide si commande encore en cours
- `status` : Livrée / En cours / Annulée / Retournée

**`avis.csv`**
- `review_id` : identifiant unique
- `order_id` : référence vers `commandes.csv`
- `rating` : note laissée (1 à 5)
- `comment_length` : longueur du commentaire laissé (nombre de caractères)

## Ce qu'on te demande

Le projet est structuré en 4 phases. **Fais-les dans l'ordre** — chaque phase dépend de la précédente, et sauter une étape de nettoyage se paiera cash dans les statistiques et les graphes plus loin.

Aucun graphe ni aucune méthode n'est indiqué dans les questions ci-dessous : c'est à toi de décider quoi utiliser et pourquoi, comme dans le mini-projet précédent.

---

### Phase 1 — Audit et nettoyage (par fichier)

Pour **chacun des 5 fichiers**, avant de les toucher, fais un audit systématique :
- Combien de valeurs manquantes, dans quelles colonnes ?
- Y a-t-il des doublons (lignes strictement identiques, ou identifiants dupliqués avec des infos différentes) ?
- Les formats sont-ils cohérents dans chaque colonne (dates, texte, casse, espaces) ?
- Y a-t-il des valeurs impossibles ou aberrantes (âge de 180 ans, quantité négative, prix négatif) ?

Ensuite, nettoie chaque fichier :
- Uniformise les formats de date.
- Uniformise les catégories textuelles qui désignent la même chose écrite différemment (ex. villes, modes de paiement, catégories de produits).
- Décide, pour chaque valeur manquante, si tu la supprimes, l'imputes (et avec quoi — moyenne, médiane, mode ? justifie ton choix), ou la laisses telle quelle (et pourquoi).
- Traite les valeurs aberrantes : les corriger si l'erreur est évidente, les exclure si elles sont injustifiables, ou les garder si elles sont plausibles — dans tous les cas, **documente ta décision**.
- Supprime les doublons après les avoir identifiés et compris.

### Phase 2 — Fusion des données

Avant de fusionner, réfléchis :
- Certaines commandes référencent des `client_id` ou `product_id` qui n'existent pas dans les autres fichiers. Que fais-tu de ces lignes ? (les supprimer silencieusement peut fausser tes totaux — décide consciemment et documente)
- Certains avis référencent des commandes inexistantes — même question.
- Toutes les commandes n'ont pas d'avis : quel type de jointure utilises-tu selon la question posée (voir Phase 4) ?

Construit une table consolidée exploitable, en conservant la possibilité de revenir aux tables sources si besoin.

### Phase 3 — Statistiques descriptives

Calcule et documente, pour les variables numériques clés (prix, délai de livraison, note, âge, quantité) :
- Tendance centrale (moyenne, médiane) et dispersion (écart-type, IQR).
- Compare moyenne et médiane sur chaque variable : sont-elles proches ? Si non, qu'est-ce que ça t'indique sur la distribution ?

### Phase 4 — Exploration graphique et interprétation

Réponds, graphe(s) à l'appui, aux questions suivantes posées par l'entreprise. **Formule d'abord la question en tes propres mots, choisis ensuite le ou les graphes adaptés, puis interprète** — ne te contente jamais d'un graphe sans un paragraphe qui dit ce qu'il montre.

1. **Direction générale** — Le chiffre d'affaires (à calculer à partir de `quantity`, `list_price`, `discount_pct`) évolue-t-il de façon particulière sur l'année ? Y a-t-il des tendances exploitables pour anticiper les stocks ?
2. **Direction générale** — Quelles catégories de produits génèrent le plus de marge (`list_price - cost_price`) ? Est-ce cohérent avec ce qui se vend le plus (`quantity`) ?
3. **Qualité** — Le délai de livraison influence-t-il la note laissée par les clients ? Cette relation est-elle la même dans toutes les régions ?
4. **Qualité** — Les fournisseurs avec un `lead_time_days` élevé ont-ils un impact visible sur le stock ou sur les délais de livraison des produits qu'ils fournissent ?
5. **Marketing** — Le profil des clients VIP (âge, ville, ancienneté) diffère-t-il de celui des clients Nouveaux ? Le mode de paiement varie-t-il selon la région ?
6. **Marketing** — Certains produits ont-ils un stock très déséquilibré par rapport à leurs ventes (sur-stock ou rupture imminente) ?
7. **Direction générale** — Existe-t-il des variables numériques du jeu de données fusionné fortement corrélées entre elles ? Toutes les variables numériques disponibles ont-elles un sens à être incluses dans cette analyse ?

Pour chaque question, sois attentif à ce que ton graphe **ne cache pas** une partie de la réponse (moyenne sans dispersion, proportions avec trop de catégories, variables sans rapport incluses dans une corrélation, etc.).

---

## Livrable attendu

Un notebook Jupyter (`.ipynb`) unique, structuré selon les 4 phases ci-dessus, avec :
- du code commenté,
- les graphes produits,
- **un paragraphe d'interprétation en Markdown après chaque graphe** (le code seul ne suffit pas — un recruteur ou un manager veut lire ta conclusion, pas deviner à partir d'un graphe brut),
- une conclusion générale de quelques lignes en fin de notebook.

## Auto-évaluation

Avant de pousser sur GitHub, vérifie que tu peux répondre "oui" à chaque point :

- [ ] J'ai documenté chaque décision de nettoyage (pas seulement exécuté du code)
- [ ] J'ai géré les valeurs manquantes en justifiant le choix pour chaque colonne concernée
- [ ] J'ai géré les clés orphelines dans les jointures consciemment, pas par accident
- [ ] Chaque graphe répond à une question formulée clairement avant le graphe
- [ ] Chaque graphe est suivi d'une interprétation écrite, pas seulement affiché
- [ ] J'ai vérifié qu'aucun de mes graphes ne cache une partie de la réponse (dispersion, catégories trop nombreuses, variable sans sens incluse)
- [ ] Mon notebook s'exécute de haut en bas sans erreur sur une exécution propre (`Kernel → Restart & Run All`)

## Structure du dépôt suggérée

```
.
├── README.md
├── data/
│   ├── clients.csv
│   ├── produits.csv
│   ├── fournisseurs.csv
│   ├── commandes.csv
│   └── avis.csv
├── consigne_projet.pdf
└── notebook_analyse.ipynb   <- ton livrable
```

---

*Ce projet clôture la partie analyse de données de la formation. La suite : machine learning avec scikit-learn.*
