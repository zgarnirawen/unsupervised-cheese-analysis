import pandas as pd
import skfuzzy as fuzz
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# Chargement CORRECT
data = pd.read_csv("fromages.txt", sep="\s+", engine="python", index_col=0)

# Vérification
print(data.head())
print("Colonnes :", data.columns)
print("Dimensions :", data.shape)

# Infos détaillées
print(data.info())

# Statistiques
print(data.describe())



kmeans = KMeans(n_clusters=4, random_state=42)
labels_kmeans = kmeans.fit_predict(data)

# Ajouter les clusters aux données
data_kmeans = data.copy()
data_kmeans['Cluster_KMeans'] = labels_kmeans

print(data_kmeans)

# Distances aux centres
distances = kmeans.transform(data)
data_kmeans['Distance_to_center'] = np.min(distances, axis=1)
print(data_kmeans)




# Standardisation
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# ACP 2D
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Plot clusters
plt.figure(figsize=(10,7))
colors = ['red', 'blue', 'green', 'orange']
for i in range(4):
    plt.scatter(data_pca[labels_kmeans == i, 0],
                data_pca[labels_kmeans == i, 1],
                c=colors[i], label=f"Cluster {i}")

# Ajouter noms des fromages
for i, txt in enumerate(data.index):
    plt.text(data_pca[i, 0], data_pca[i, 1], txt, fontsize=8)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("ACP + K-means")
plt.legend()
plt.show()




# Transposer (format requis)
data_T = data_scaled.T

# FCM
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data_T, c=4, m=2, error=0.005, maxiter=1000, init=None
)

# Matrice d'appartenance
print("Matrice d'appartenance:\n", u)

# Classe dominante
labels_fcm = u.argmax(axis=0)
data_fcm = data.copy()
data_fcm['Cluster_FCM'] = labels_fcm
print(data_fcm)

# Infos FCM
print("Nombre d'itérations :", p)
print("Critère objectif (J) :", jm[-1])
print("FPC (qualité du clustering) :", fpc)

comparison = pd.DataFrame({
    'KMeans': labels_kmeans,
    'FCM': labels_fcm
}, index=data.index)
print(comparison)

inertia = []
K_range = range(1, 10)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(data_scaled)
    inertia.append(km.inertia_)

# Plot courbe du coude
plt.figure(figsize=(8,5))
plt.plot(K_range, inertia, marker='o')
plt.xlabel("Nombre de clusters K")
plt.ylabel("Inertie intra-classe")
plt.title("Méthode du coude - K-means")
plt.show()

# Points avec appartenance < 0.6 → ambigus
ambiguous = [i for i in range(len(u.T)) if max(u[:, i]) < 0.6]
print("Fromages ambigus :", data.index[ambiguous])