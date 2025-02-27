import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

clustering_data_scaled = np.load('data/clustering_data_scaled.npy')

k = 4  


kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(clustering_data_scaled)

students_data = pd.read_csv('data/Students_Grading_Dataset.csv')

students_with_clusters = students_data.copy()

students_with_clusters['Cluster'] = clusters

students_with_clusters.to_csv('data/students_with_clusters.csv', index=False)

print(f'Modelo treinado com {k} clusters! Dados salvos em "data/students_with_clusters.csv".')
