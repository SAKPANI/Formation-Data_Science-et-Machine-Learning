# 📊 PROJET FINAL — VISUALISATION DES DONNÉES UNIVERSITAIRES

## CONTEXTE

Ce projet est la suite directe du projet d'analyse réalisé avec **Pandas**.

⚠️ Les analyses de base ont déjà été réalisées dans le projet Pandas : nettoyage, valeurs manquantes, jointures, calculs, moyennes, taux de réussite, analyses par filière/matière, présence, absences, retards, corrélations et classements.

**Ne refais donc pas tout le projet Pandas.**

Récupère le DataFrame final propre et utilise-le comme point de départ. L'objectif est maintenant de maîtriser **Matplotlib et Seaborn** pour transformer les résultats en représentations graphiques claires et les interpréter.

---

# PARTIE 0 — RÉCUPÉRATION DU DATAFRAME FINAL

### Travail
- Importer Pandas, Matplotlib et Seaborn.
- Charger le DataFrame final du projet Pandas.
- Afficher quelques lignes.
- Vérifier dimensions, colonnes et types.
- Vérifier les variables nécessaires aux graphiques.

### Questions
1. Combien de lignes possède le DataFrame ?
2. Combien de colonnes ?
3. Quelles variables seront utilisées ?
4. Quelles variables sont numériques ?
5. Quelles sont catégorielles ?
6. Existe-t-il encore des valeurs manquantes pouvant influencer les graphiques ?
7. Les données sont-elles prêtes pour la visualisation ?

---

# PARTIE 1 — RÉPARTITION PAR FILIÈRE

### Graphiques
- Barplot des effectifs.
- Représentation des proportions.

### Questions
1. Quelle filière possède le plus d'étudiants ?
2. Quelle possède le moins d'étudiants ?
3. Les effectifs sont-ils équilibrés ?
4. Quelle proportion représente chaque filière ?
5. Le graphique confirme-t-il l'analyse Pandas ?
6. Quelle représentation est la plus lisible ?
7. Pourquoi ?

---

# PARTIE 2 — RÉPARTITION PAR SEXE

### Graphiques
- Barplot.
- Représentation proportionnelle.
- Sexe par filière.

### Questions
1. Quelle catégorie est majoritaire ?
2. Quelle proportion représente-t-elle ?
3. La répartition est-elle équilibrée ?
4. La répartition varie-t-elle selon les filières ?
5. Quelle filière présente la plus grande différence ?
6. Quel graphique permet le mieux de comparer les filières ?
7. Que peux-tu conclure ?

---

# PARTIE 3 — DISTRIBUTION DES ÂGES

### Graphiques
- Histogramme.
- Histogramme + KDE.
- Boxplot.

### Questions
1. Quelle tranche d'âge est la plus représentée ?
2. La distribution est-elle concentrée ou dispersée ?
3. Est-elle symétrique ?
4. Existe-t-il des valeurs atypiques ?
5. Que montre le boxplot ?
6. Quel graphique représente le mieux la distribution ?
7. Quel graphique permet de détecter les valeurs atypiques ?
8. Quelle conclusion ?

---

# PARTIE 4 — DISTRIBUTION DES NOTES

### Graphiques
- Histogramme.
- Histogramme + KDE.
- Boxplot.

### Questions
1. Où se concentrent les notes ?
2. Quelle tranche est la plus fréquente ?
3. Les notes sont-elles plutôt faibles ou élevées ?
4. Combien de notes sont visuellement sous 10 ?
5. Existe-t-il beaucoup de notes élevées ?
6. Existe-t-il des valeurs atypiques ?
7. La distribution semble-t-elle normale ?
8. Quel graphique est le plus informatif ?
9. Le résultat confirme-t-il Pandas ?
10. Quelle conclusion sur le niveau général ?

---

# PARTIE 5 — RÉUSSITE ET ÉCHEC

Règle déjà utilisée dans Pandas : **note >= 10 = réussite ; note < 10 = échec**.

### Graphiques
- Barplot réussite/échec.
- Représentation proportionnelle.

### Questions
1. Quelle catégorie domine ?
2. Quel est le taux de réussite ?
3. Quel est le taux d'échec ?
4. L'écart est-il important ?
5. Le niveau paraît-il satisfaisant ?
6. Quel graphique est le plus efficace ?
7. Quelle conclusion ?

---

# PARTIE 6 — MOYENNE PAR FILIÈRE

### Graphiques
- Barplot.
- Classement graphique.

### Questions
1. Quelle filière possède la meilleure moyenne ?
2. Quelle possède la plus faible ?
3. Quelle est la différence entre les deux ?
4. Les écarts sont-ils importants ?
5. Combien de filières ont une moyenne >= 10 ?
6. Le graphique confirme-t-il Pandas ?
7. Quelle filière semble la plus performante ?
8. Laquelle nécessite davantage d'attention ?

---

# PARTIE 7 — TAUX DE RÉUSSITE PAR FILIÈRE

### Graphique
Comparer toutes les filières.

### Questions
1. Quelle filière possède le meilleur taux ?
2. Quelle possède le plus faible ?
3. Quelle est la différence ?
4. Les différences sont-elles importantes ?
5. Une bonne moyenne implique-t-elle forcément un bon taux de réussite ?
6. Compare avec la Partie 6.
7. Quelle filière semble globalement la plus performante ?

---

# PARTIE 8 — ANALYSE DES MATIÈRES

### Graphiques
- Moyenne par matière.
- Classement.
- Taux de réussite.
- Boxplot par matière.

### Questions
1. Quelle matière a la meilleure moyenne ?
2. Quelle a la plus faible ?
3. Quelles sont les 5 meilleures ?
4. Quelles sont les 5 plus faibles ?
5. Quelle a le meilleur taux de réussite ?
6. Quelle a le plus faible ?
7. Quelle matière possède la plus grande dispersion ?
8. Quelle semble la plus difficile ?
9. Quelle semble la mieux maîtrisée ?
10. Une bonne moyenne implique-t-elle forcément un bon taux ?
11. Que montre le boxplot que le barplot ne montre pas ?
12. Quelle représentation est la plus utile pour la dispersion ?

---

# PARTIE 9 — ABSENCES

### Graphiques
- Histogramme.
- Boxplot.
- Absences moyennes par filière.

### Questions
1. Où se concentrent les absences ?
2. Existe-t-il beaucoup d'absences ?
3. Existe-t-il des étudiants très absents ?
4. Existe-t-il des valeurs atypiques ?
5. Quelle filière a le plus d'absences en moyenne ?
6. Quelle en a le moins ?
7. Les différences sont-elles importantes ?
8. Que montre le boxplot ?
9. Quelle conclusion ?

---

# PARTIE 10 — TAUX DE PRÉSENCE

### Graphiques
- Histogramme.
- Boxplot.
- Présence moyenne par filière.

### Questions
1. Où se concentrent les taux de présence ?
2. Les étudiants sont-ils globalement assidus ?
3. Combien ont >= 90 % ?
4. Combien ont < 75 % ?
5. Quelle filière a le meilleur taux ?
6. Quelle a le plus faible ?
7. Existe-t-il des valeurs atypiques ?
8. Quelle relation visuelle peut-on faire avec les résultats ?

---

# PARTIE 11 — RETARDS

### Graphiques
- Histogramme.
- Boxplot.
- Retards moyens par filière.

### Questions
1. Où se concentrent les retards ?
2. Existe-t-il des étudiants avec beaucoup de retards ?
3. Existe-t-il des valeurs atypiques ?
4. Quelle filière en a le plus ?
5. Quelle en a le moins ?
6. Les différences sont-elles importantes ?
7. Quelle conclusion ?

---

# PARTIE 12 — ABSENCES ET MOYENNE

### Graphiques
- Scatterplot.
- Regression plot.
- Éventuellement distinction par filière.

### Questions
1. Quelle tendance générale observes-tu ?
2. Que devient la moyenne lorsque les absences augmentent ?
3. Les points sont-ils dispersés ?
4. Existe-t-il des étudiants très absents mais performants ?
5. Existe-t-il des étudiants peu absents mais faibles ?
6. La tendance est-elle positive ou négative ?
7. Le graphique confirme-t-il la corrélation Pandas ?
8. La relation semble-t-elle forte ou faible ?
9. Peut-on parler de causalité ?
10. Quelles sont les limites ?

---

# PARTIE 13 — PRÉSENCE ET MOYENNE

### Graphiques
- Scatterplot.
- Regression plot.
- Éventuellement distinction par filière.

### Questions
1. Quelle tendance générale ?
2. Les plus présents semblent-ils avoir de meilleures moyennes ?
3. Existe-t-il des exceptions ?
4. La relation est-elle positive ou négative ?
5. Le graphique confirme-t-il Pandas ?
6. La relation semble-t-elle forte ou faible ?
7. Peut-on parler de causalité ?
8. Quelles sont les limites ?

---

# PARTIE 14 — RETARDS ET MOYENNE

### Graphiques
- Scatterplot.
- Regression plot.

### Questions
1. Quelle tendance observes-tu ?
2. Que devient la moyenne quand les retards augmentent ?
3. Existe-t-il des exceptions ?
4. La tendance est-elle positive ou négative ?
5. Le graphique confirme-t-il Pandas ?
6. La relation est-elle forte ou faible ?
7. Peut-on parler de causalité ?
8. Quelle conclusion ?

---

# PARTIE 15 — HEATMAP DES CORRÉLATIONS

Variables possibles : âge, note, moyenne, absences, retards, taux de présence.

### Questions
1. Quelle variable est la plus positivement corrélée à la moyenne ?
2. Quelle est la plus négativement corrélée ?
3. Quelle relation est la plus forte ?
4. Quelle est la plus faible ?
5. Que montre absences/présence ?
6. Que montre présence/moyenne ?
7. Que montre absences/moyenne ?
8. Que montre retards/moyenne ?
9. Le graphique confirme-t-il les analyses précédentes ?
10. Quelle relation mérite le plus d'attention ?
11. Pourquoi corrélation ne signifie-t-elle pas causalité ?

---

# PARTIE 16 — TOP 10 DES MEILLEURS ÉTUDIANTS

Les classements ont déjà été réalisés avec Pandas.

### Graphiques
- Barplot horizontal du Top 10.
- Moyennes.
- Éventuellement distinction par filière.

### Questions
1. Qui est le premier ?
2. Quelle est sa moyenne ?
3. Quel est l'écart premier/dixième ?
4. Quelle filière est la plus représentée ?
5. Le classement est-il serré ?
6. Existe-t-il une grande différence entre les premiers ?
7. Quelle représentation permet le mieux de lire les noms ?
8. Quel profil général possède le Top 10 ?

---

# PARTIE 17 — ÉTUDIANTS EN DIFFICULTÉ

⚠️ Un NaN n'est pas une note de 0.

### Graphiques
- Barplot horizontal.
- Comparaison des moyennes.
- Éventuellement distinction par filière.

### Questions
1. Quels sont les étudiants concernés ?
2. Quelle est la moyenne du plus faible ?
3. Quelle est celle du dixième ?
4. Quelles filières sont représentées ?
5. Quelle filière est la plus représentée ?
6. Le groupe présente-t-il un grand écart ?
7. Peut-on identifier un profil commun ?
8. Que montre la visualisation ?

---

# PARTIE 18 — PERSONNALISATION DES GRAPHIQUES

Pour plusieurs graphiques travailler sur :
- titre ;
- labels des axes ;
- rotation des labels ;
- légende ;
- taille ;
- annotations ;
- ticks ;
- grille lorsque pertinente ;
- ordre des catégories ;
- lisibilité ;
- `tight_layout()`.

### Questions
1. Le titre est-il clair ?
2. Les axes sont-ils correctement nommés ?
3. Les unités sont-elles indiquées ?
4. Les noms sont-ils lisibles ?
5. Les valeurs importantes sont-elles visibles ?
6. La légende est-elle nécessaire ?
7. Y a-t-il des éléments inutiles ?
8. Comment améliorer la lisibilité ?
9. Quelle différence entre graphique brut et graphique personnalisé ?

---

# PARTIE 19 — CHOIX DU BON GRAPHIQUE

### Questions
1. Quand utiliser un barplot ?
2. Quand utiliser un histogramme ?
3. Quand utiliser un boxplot ?
4. Quand utiliser un scatterplot ?
5. Quand utiliser une heatmap ?
6. Quand utiliser une représentation proportionnelle ?
7. Quel graphique choisir pour comparer des catégories ?
8. Quel graphique choisir pour étudier une distribution ?
9. Quel graphique choisir pour deux variables numériques ?
10. Quel graphique choisir pour plusieurs corrélations ?
11. Pourquoi un graphique peut-il être plus adapté qu'un autre ?

---

# PARTIE 20 — SYNTHÈSE VISUELLE

Construire une page/notebook de synthèse avec les graphiques les plus importants :

- effectif par filière ;
- répartition par sexe ;
- moyenne générale ;
- réussite/échec ;
- moyenne par filière ;
- moyenne par matière ;
- taux de présence ;
- absences ;
- présence/moyenne ;
- absences/moyenne.

### Questions
1. Quels sont les 5 graphiques les plus importants ?
2. Pourquoi les as-tu sélectionnés ?
3. Quel graphique apporte l'information la plus importante ?
4. Quel graphique compare le mieux les filières ?
5. Quel graphique évalue le mieux le niveau général ?
6. Quel graphique montre le mieux l'assiduité ?
7. Quel graphique montre les relations entre variables ?
8. La synthèse permet-elle de comprendre rapidement la situation ?

---

# PARTIE 21 — INTERPRÉTATION

Pour chaque graphique important :

**Observation → comparaison → interprétation possible → limite → conclusion.**

### Questions
1. Qu'observes-tu ?
2. Quelle catégorie domine ?
3. Quelle est la plus faible ?
4. Quelle différence importante observes-tu ?
5. Y a-t-il une tendance ?
6. Y a-t-il des valeurs atypiques ?
7. Le graphique confirme-t-il Pandas ?
8. Quelle interprétation proposes-tu ?
9. Quelles limites faut-il considérer ?
10. Quelle conclusion peux-tu tirer ?

---

# PARTIE 22 — SYNTHÈSE FINALE

### Questions finales

1. Quelle est la situation générale des étudiants ?
2. Le niveau académique semble-t-il satisfaisant ?
3. Le taux de réussite est-il élevé ?
4. Le taux d'échec est-il préoccupant ?
5. Les étudiants sont-ils globalement assidus ?
6. Les absences semblent-elles associées aux performances ?
7. Les retards semblent-ils associés aux performances ?
8. Quelle filière possède les meilleurs résultats ?
9. Quelle filière possède les résultats les plus faibles ?
10. Quelle matière semble la plus difficile ?
11. Quelle matière semble la mieux maîtrisée ?
12. Quels sont les principaux constats ?
13. Quels problèmes nécessitent une attention particulière ?
14. Quelles recommandations peux-tu proposer ?
15. Quelles limites possède l'étude ?
16. Quelles visualisations supplémentaires pourrais-tu proposer ?

---

# ✅ RÈGLE FINALE

**Ne refais PAS le projet Pandas.**

Le projet Pandas a servi à préparer et analyser les données.

Ici :

**ANALYSE PANDAS → VISUALISATION → INTERPRÉTATION**

Pour chaque visualisation :

1. Identifier la question.
2. Préparer les données nécessaires avec Pandas si besoin.
3. Choisir le graphique adapté.
4. Créer le graphique avec Matplotlib ou Seaborn.
5. Le personnaliser.
6. L'interpréter.
7. Comparer avec le résultat du projet Pandas.
8. Conclure.

🎯 Objectif : être capable de choisir une représentation adaptée à une question et de produire un graphique propre, lisible, pertinent et interprétable.
