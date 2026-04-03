# Classification Non Supervisée – K-means et Fuzzy C-Means (FCM)

## 1. Objectif du TP
L'objectif de ce TP est d'appliquer des méthodes de **classification non supervisée** sur un jeu de données de fromages, afin de :  
- Identifier des groupes de fromages ayant des caractéristiques similaires.  
- Comparer les résultats obtenus avec deux approches différentes : **K-means** et **Fuzzy C-Means (FCM)**.  
- Visualiser les partitions grâce à l'**Analyse en Composantes Principales (ACP)**.  
- Évaluer la qualité du clustering et interpréter les résultats.  

---

## 2. Bibliographie / Références
- **Pandas** pour la manipulation des données : [https://pandas.pydata.org/](https://pandas.pydata.org/)  
- **Scikit-learn** pour K-means et ACP : [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)  
- **Scikit-fuzzy** pour Fuzzy C-Means : [https://pythonhosted.org/scikit-fuzzy/](https://pythonhosted.org/scikit-fuzzy/)  
- Livre : Tan, Steinbach, Kumar – *Introduction to Data Mining* (chapitre sur le clustering)  
- Documentation officielle ACP : [https://scikit-learn.org/stable/modules/decomposition.html](https://scikit-learn.org/stable/modules/decomposition.html)

---

## 3. Méthodes utilisées
1. **Exploration des données**  
   - Chargement du fichier `fromages.txt`  
   - Affichage des premières lignes, dimensions et statistiques descriptives.  

2. **Classification K-means**  
   - Application de K-means avec 4 clusters.  
   - Calcul de la distance de chaque fromage au centre de son cluster.  

3. **Classification Fuzzy C-Means (FCM)**  
   - Application de FCM avec 4 clusters.  
   - Analyse de la matrice des degrés d'appartenance.  
   - Détermination de la classe dominante pour chaque observation.  

4. **Visualisation via ACP**  
   - Standardisation des données.  
   - Projection des fromages sur un plan 2D.  
   - Visualisation des clusters K-means et FCM avec des couleurs différentes pour chaque classe.  

5. **Détermination du nombre optimal de clusters (méthode du coude)**  
   - Variation du nombre de clusters de 1 à 9.  
   - Tracé de l’inertie intra-classe pour identifier le “coude”.

---

## 4. Interprétations des résultats

- **K-means (clusters durs)** :  
  - Chaque fromage appartient à un seul cluster.  
  - On observe des groupes homogènes basés sur les caractéristiques nutritionnelles.  
  - Exemple : K-means a regroupé les fromages très riches en calcium dans un cluster.  

- **Fuzzy C-Means (clusters flous)** :  
  - Certains fromages ont des degrés d’appartenance élevés à plusieurs clusters (ex : `CarredelEst`, `Bleu`, `Cheddar`).  
  - Permet de détecter les fromages “ambigus” qui ne sont pas typiques d’un seul cluster.  

- **ACP (projection 2D)** :  
  - Permet de visualiser la séparation des clusters.  
  - Les clusters sont généralement bien séparés, mais certains fromages se trouvent entre deux groupes, confirmant les résultats FCM.  

- **Analyse de la qualité du clustering** :  
  - K-means : distance moyenne au centre du cluster montre la compacité.  
  - FCM : FPC (~0.56) indique une séparation modérée entre clusters et permet d’identifier les fromages ambigus.  

- **Nombre optimal de clusters** :  
  - Courbe de l’inertie intra-classe : le coude se situe autour de 4 clusters.  
  - Confirme que le choix de K = 4 pour K-means et FCM est approprié.

---

## 5. Réponses aux questions théoriques

1. **Différence fondamentale entre K-means et FCM** :  
   - **K-means** : partition “dure”, chaque observation appartient à un seul cluster.  
   - **FCM** : partition “floue”, chaque observation a un degré d’appartenance à tous les clusters.  

2. **Cas où FCM est plus adapté que K-means** :  
   - Lorsque certaines observations ne sont pas clairement assignables à un cluster unique.  
   - Pour les données présentant des chevauchements ou des ambigüités.  

3. **Inertie intra-classe** :  
   - Mesure la compacité des clusters.  
   - Somme des distances au carré entre chaque point et le centre de son cluster.  
   - Plus l’inertie est faible, plus les clusters sont homogènes.  

4. **ACP conserve-t-elle toute l’information ?**  
   - Non, elle réduit la dimensionnalité.  
   - Elle conserve la majorité de la variance, mais une partie de l’information est perdue lors de la projection sur 2 dimensions.

---

## 6. Remarques supplémentaires

- Les fromages ambigus identifiés par FCM :  
  `CarredelEst`, `Bleu`, `Cheddar`, `Coulomniers`, `Fr.chevrepatemolle`, `Fr.fondu.45`, `Maroilles`, `Parmesan`, `Rocquefort`, `Vacherin`.  
- Les graphes peuvent être résumés comme :  
  - **K-means** : cluster dur  
  - **FCM** : cluster flou  

---

