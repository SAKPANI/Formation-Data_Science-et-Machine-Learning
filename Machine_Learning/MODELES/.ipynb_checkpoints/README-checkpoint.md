# Machine Learning appliqué — Arbres de décision, Random Forest, XGBoost, Séries temporelles

Support complet pour apprendre les modèles de ML les plus utilisés en pratique, avec deux
jeux de données e-commerce générés pour ce cours.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `cours.pdf` | Le cours complet (théorie, code, paramètres à régler, mini-projets) |
| `cours.tex` | Source LaTeX du cours (modifiable) |
| `dataset_exercices.csv` | Jeu de données **clients e-commerce** (2000 lignes) pour les mini-projets après chaque modèle |
| `dataset_projet_final.csv` | Jeu de données **transactions e-commerce sur 3 ans** (~17 000 lignes) pour le projet final |
| `README.md` | Ce fichier — guide question par question |

## Comment utiliser ce cours

1. Lisez `cours.pdf` chapitre par chapitre, dans l'ordre.
2. À la fin de chaque chapitre (Arbre, Random Forest, XGBoost, Séries temporelles), faites
   le **mini-projet** correspondant sur `dataset_exercices.csv`. Les questions ci-dessous
   reprennent celles du PDF, avec un peu plus d'indications pour démarrer.
3. Une fois les 4 modèles maîtrisés, attaquez le **projet final** sur
   `dataset_projet_final.csv` (section dédiée plus bas).

---

## Dataset 1 — `dataset_exercices.csv`

Une ligne = un client. Colonnes :
`date_inscription, age, genre, region, type_abonnement, depense_mensuelle,
nb_commandes_mois_dernier, nb_retours, jours_depuis_derniere_commande,
score_satisfaction, churn`

`churn = 1` signifie que le client a résilié / est parti.

### Mini-projet 1 — Arbre de décision
1. Chargez le dataset, encodez les variables catégorielles, séparez train/test.
2. Entraînez un `DecisionTreeClassifier` pour prédire `churn`, avec `max_depth=2` puis
   sans limite (`max_depth=None`). Comparez le score en train et en test dans les deux cas.
   - *Question* : dans quel cas le modèle "récite" les données d'entraînement plutôt que
     d'apprendre une règle générale ?
3. Affichez l'arbre (`plot_tree`). Quelle est la première variable utilisée ? Retrouvez-vous
   cette variable dans vos graphiques d'exploration (EDA) du chapitre 2 ?
4. Cherchez le meilleur `max_depth` avec `GridSearchCV` et tracez le score en fonction de
   `max_depth`.
5. **Bonus régression** : refaites l'exercice en prédisant `depense_mensuelle` avec un
   `DecisionTreeRegressor`. Quelle métrique utilisez-vous à la place de l'accuracy ?

### Mini-projet 2 — Random Forest
1. Entraînez un `RandomForestClassifier` avec les mêmes réglages de profondeur que
   l'arbre seul. Le score s'améliore-t-il ?
2. Tracez le score en test en fonction de `n_estimators` (10, 50, 100, 200, 400).
3. Affichez l'importance des variables (`feature_importances_`). Classez les 3 variables
   les plus importantes pour prédire le churn.
4. Ajoutez `class_weight="balanced"`. Le F1-score de la classe `churn=1` change-t-il ?
   Pourquoi (regardez la proportion de churn dans le dataset) ?

### Mini-projet 3 — XGBoost
1. Entraînez un `XGBClassifier` par défaut et comparez son F1-score à celui du Random
   Forest.
2. Tracez la courbe d'apprentissage (logloss train vs test) avec `n_estimators=1000` et
   sans early stopping. Voyez-vous une divergence entre les deux courbes (signe
   d'overfitting) ?
3. Ajoutez `early_stopping_rounds=20`. Combien d'arbres sont réellement utilisés
   (`xgb.best_iteration`) ?
4. Testez plusieurs `learning_rate` (0.01, 0.05, 0.1, 0.3) et tracez le F1-score obtenu
   pour chacun.

### Mini-projet 4 — LightGBM
1. Entraînez un `LGBMClassifier` par défaut et comparez son F1-score à XGBoost et Random
   Forest.
2. Testez `num_leaves` ∈ {7, 15, 31, 63, 127} et tracez le F1-score en test en fonction de
   `num_leaves`. À partir de quand voyez-vous l'overfitting apparaître ?
3. Repassez les colonnes catégorielles en type `"category"` et utilisez
   `categorical_feature` au lieu de `get_dummies`. Le score ou le temps d'entraînement
   changent-ils ?
4. Chronométrez l'entraînement de LightGBM, XGBoost et Random Forest sur ce dataset et
   comparez.

### Mini-projet 5 — CatBoost
1. Entraînez un `CatBoostClassifier` en donnant les colonnes catégorielles brutes via
   `cat_features` (sans `get_dummies`). Comparez le F1-score à LightGBM et XGBoost.
2. Testez `depth` ∈ {2, 4, 6, 8, 10} et tracez le F1-score en test en fonction de la
   profondeur.
3. Retirez `cat_features` (ou encodez vous-même les colonnes catégorielles). Le score
   change-t-il ? Qu'est-ce que ça vous apprend ?
4. Construisez un tableau récapitulatif (accuracy, F1, temps d'entraînement) comparant
   XGBoost, LightGBM et CatBoost, et concluez lequel choisir sur ce dataset.

### Mini-projet 6 — Séries temporelles
1. Comptez le nombre d'inscriptions par jour (`groupby("date_inscription").size()`) et
   tracez la courbe.
2. Décomposez cette série avec `seasonal_decompose` (tendance / saisonnalité / résidu).
3. Créez des variables de retard (`lag_1`, `lag_7`) et une moyenne mobile sur 7 jours, puis
   entraînez un `RandomForestRegressor` pour prédire les inscriptions du lendemain.
4. Comparez le MAE de votre modèle à un modèle "naïf" (prédire que demain = aujourd'hui).
   Votre modèle bat-il ce modèle naïf ?

---

## Dataset 2 — `dataset_projet_final.csv` (Projet final)

Une ligne = une transaction. Colonnes :
`date, categorie, prix_unitaire, quantite, remise, canal_acquisition, mode_paiement,
depense_pub, revenu_transaction, produit_retourne`

### Question 1 — Exploration
- Quelles catégories de produits génèrent le plus de revenu ?
- Le revenu journalier a-t-il une tendance et/ou une saisonnalité visible ? (tracez-le)
- Y a-t-il un lien visuel entre `remise` et `produit_retourne` ?

### Question 2 — Classification : prédire `produit_retourne`
- Entraînez un arbre de décision, un Random Forest, XGBoost, LightGBM et CatBoost.
- Le dataset est déséquilibré (peu de retours) : utilisez `class_weight`/`scale_pos_weight`
  et regardez F1-score / recall de la classe minoritaire, pas seulement l'accuracy.
- Avec LightGBM et CatBoost, essayez de passer directement les colonnes catégorielles
  brutes (`categorie`, `canal_acquisition`, `mode_paiement`) sans `get_dummies`.
- Quel modèle donne le meilleur F1-score sur la classe "retourné" ?

### Question 3 — Régression : prédire `revenu_transaction`
- Entraînez les 5 mêmes familles de modèles en régression.
- Comparez MAE, RMSE et $R^2$. Quelles variables comptent le plus (feature importance) ?

### Question 4 — Série temporelle : prévoir les ventes
- Agrégez `revenu_transaction` par jour.
- Prévoyez les 30 prochains jours avec (a) un modèle SARIMA et (b) un modèle ML
  (Random Forest ou XGBoost) avec features de lag/moyenne mobile.
- Comparez les deux approches sur les 30 derniers jours réels disponibles (MAE, RMSE).

### Question 5 — Optimisation
- Choisissez un modèle (celui qui vous semble le plus prometteur) et lancez une recherche
  d'hyperparamètres (`GridSearchCV` ou `RandomizedSearchCV`).
- Quel gain de score obtenez-vous par rapport aux paramètres par défaut ?

### Question 6 — Conclusion (à rédiger)
Rédigez une courte synthèse (une page) qui répond à :
- Quel modèle recommandez-vous pour chaque tâche (retour produit, revenu, prévision de
  ventes) et pourquoi (score, rapidité, interprétabilité) ?
- Quelles limites voyez-vous à votre analyse (qualité des données, hypothèses faites) ?

---

## Conseils généraux
- Faites toujours un `train_test_split` (ou un découpage chronologique pour les séries
  temporelles) **avant** de juger un modèle : ne jamais évaluer sur les données
  d'entraînement.
- Sauvegardez vos graphiques (`plt.savefig(...)`) au fur et à mesure : ils serviront pour
  votre rapport final.
- N'hésitez pas à relire les encadrés "Paramètres importants" du `cours.pdf` avant chaque
  mini-projet : ils listent les leviers à essayer pour améliorer un score qui stagne.
