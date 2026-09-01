# PROJET FINAL PANDAS — ANALYSE DES DONNÉES UNIVERSITAIRES

## Objectif

Réaliser une analyse complète de données universitaires en utilisant **Pandas uniquement** pour toutes les opérations de traitement et d'analyse.

Vous disposez de 5 fichiers CSV :

- `students.csv` : informations sur les étudiants
- `courses.csv` : informations sur les matières
- `grades.csv` : notes obtenues
- `attendance.csv` : assiduité par semestre
- `exams.csv` : informations sur les examens

## Règle principale

Le projet doit être réalisé avec **Pandas uniquement** pour la manipulation, le nettoyage, la transformation, l'agrégation et l'analyse des données.

Ne pas utiliser NumPy, Seaborn, Matplotlib ou une autre bibliothèque pour effectuer les analyses.

Vous pouvez utiliser Python et Pandas, mais le cœur du projet doit être Pandas.

## Partie 1 — Découverte des données

Pour chaque fichier :

1. Importer le CSV.
2. Afficher les premières et dernières lignes.
3. Afficher le nombre de lignes et de colonnes.
4. Afficher les noms des colonnes.
5. Examiner les types de données.
6. Produire un résumé statistique.
7. Identifier les valeurs manquantes.
8. Identifier les doublons.

## Partie 2 — Nettoyage

Nettoyer les données et expliquer les décisions prises.

Vous devez notamment :

- traiter les valeurs manquantes ;
- vérifier les doublons ;
- corriger les types de données si nécessaire ;
- vérifier les valeurs incohérentes ;
- uniformiser les données textuelles ;
- convertir les dates correctement.

## Partie 3 — Analyse des étudiants

Répondre avec Pandas aux questions suivantes :

1. Combien d'étudiants sont enregistrés ?
2. Combien y a-t-il d'étudiants dans chaque filière ?
3. Quelle est la répartition hommes/femmes ?
4. Quelle est la moyenne d'âge ?
5. Quel est l'âge minimum et maximum ?
6. Combien d'étudiants sont en L1, L2 et L3 ?
7. Quelle filière contient le plus d'étudiants ?

## Partie 4 — Analyse des notes

À partir de `grades.csv` et `courses.csv` :

1. Calculer la moyenne de chaque matière.
2. Trouver la matière ayant la meilleure moyenne.
3. Trouver la matière ayant la plus faible moyenne.
4. Calculer le nombre de notes disponibles par matière.
5. Calculer la moyenne des notes par semestre.
6. Identifier les étudiants ayant les meilleures notes.
7. Identifier les étudiants ayant les plus faibles résultats.
8. Calculer la moyenne générale de chaque étudiant.
9. Classer les étudiants selon leur moyenne générale.
10. Déterminer le nombre d'étudiants ayant une moyenne générale >= 10.
11. Déterminer le nombre d'étudiants ayant une moyenne générale < 10.

## Partie 5 — Jointures

Utiliser les opérations de jointure Pandas pour construire un DataFrame d'analyse complet.

Vous devez notamment utiliser :

- `merge()`
- `concat()` lorsque cela est pertinent

Construire un DataFrame permettant de relier :

étudiant → filière → matière → note → semestre.

## Partie 6 — Analyse par filière

Répondre aux questions :

1. Quelle est la moyenne générale par filière ?
2. Quelle filière possède le meilleur résultat ?
3. Quelle filière possède le plus faible résultat ?
4. Quelle filière possède le plus de notes supérieures ou égales à 10 ?
5. Quel est le taux de réussite par filière ?
6. 
# Partie 7 — Analyse de l'assiduité

À partir de `attendance.csv` :

1. Calculer le taux moyen de présence par filière.
2. Calculer le nombre moyen d'absences.
3. Identifier les étudiants ayant une faible présence.
4. Comparer présence et résultats.
5. Déterminer si les étudiants ayant beaucoup d'absences ont généralement de moins bons résultats.

## Partie 8 — Analyse avancée

#
Créer un indicateur de performance pour chaque étudiant.

Exemple de catégories :

- Très faible
- Faible
- Moyen
- Bon
- Excellent

Créer également un indicateur de risque :

- Risque élevé
- Risque moyen
- Risque faible

Les règles doivent être définies et justifiées.

## Partie 9 — GroupBy et agrégations

Le projet doit obligatoirement utiliser plusieurs analyses avec :

- `groupby()`
- `agg()`
- `count()`
- `mean()`
- `median()`
- `min()`
- `max()`
- `sum()`

Créer des tableaux récapitulatifs propres.

## Partie 10 — Pivot tables

Créer au minimum 3 tableaux croisés avec `pd.pivot_table()`.

Exemples :

- moyenne par filière et semestre ;
- moyenne par matière et semestre ;
- nombre d'étudiants par filière et niveau.

## Partie 11 — Classements

Produire :

- Top 10 général ;
- Top 5 de chaque filière ;
- 10 étudiants ayant les plus faibles moyennes ;
- matières classées de la meilleure à la moins bonne moyenne.

## Partie 12 — Questions finales

Répondre clairement aux questions suivantes :

1. Quelle est la filière la plus performante ?
2. Quelle est la matière la plus difficile ?
3. Quel est le taux de réussite global ?
4. Quelle filière a le meilleur taux de réussite ?
5. Les absences semblent-elles liées aux performances ?
6. Quel semestre présente les meilleurs résultats ?
7. Combien d'étudiants peuvent être considérés comme étant à risque ?
8. Quels sont les 10 meilleurs étudiants ?
9. Quels sont les 10 étudiants les plus en difficulté ?
10. Quelles conclusions générales peut-on tirer des données ?

## Fonctions Pandas à maîtriser

Le projet doit te permettre de pratiquer notamment :

`read_csv()`, `head()`, `tail()`, `info()`, `describe()`, `shape`, `columns`, `dtypes`, `isna()`, `fillna()`, `dropna()`, `drop_duplicates()`, `astype()`, `loc[]`, `iloc[]`, `query()`, `sort_values()`, `value_counts()`, `groupby()`, `agg()`, `merge()`, `concat()`, `pivot_table()`, `melt()`, `apply()`, `map()`, `replace()`, `rename()`, `drop()`, `assign()`, `rank()`, `cut()`, `qcut()`, `to_datetime()`.

## Rendu attendu

Créer un notebook :

`Projet_Final_Pandas.ipynb`

Organisation recommandée :

1. Importation
2. Chargement des données
3. Exploration
4. Nettoyage
5. Transformation
6. Jointures
7. Analyse descriptive
8. Analyse par matière
9. Analyse par filière
10. Analyse de l'assiduité
11. Classements
12. Pivot tables
13. Réponses aux questions finales
14. Conclusion

## Difficulté

Le projet est volontairement assez gros. Il ne faut pas chercher à tout terminer en une seule cellule.

Chaque résultat doit être accompagné d'une courte explication en Markdown dans le notebook.

**Objectif final : être capable de recevoir plusieurs fichiers CSV bruts et de mener une analyse complète uniquement avec Pandas.**

