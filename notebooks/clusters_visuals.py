import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

students_with_clusters = pd.read_csv('data/students_with_clusters.csv')

cluster_summary = students_with_clusters.groupby('Cluster').agg({
    'Attendance (%)': ['mean', 'median', 'std'],
    'Total_Score': ['mean', 'median', 'std'],
    'Study_Hours_per_Week': ['mean', 'median', 'std'],
    'Stress_Level (1-10)': ['mean', 'median', 'std'],
    'Sleep_Hours_per_Night': ['mean', 'median', 'std']
})

cluster_summary.columns = ['_'.join(col) for col in cluster_summary.columns]
cluster_summary.reset_index(inplace=True)

cluster_summary

if not os.path.exists('visuals'):
    os.makedirs('visuals')

sns.set_theme(style='whitegrid')

variables = [
    'Total_Score', 'Attendance (%)', 'Study_Hours_per_Week',
    'Stress_Level (1-10)', 'Sleep_Hours_per_Night'
]

for var in variables:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Cluster', y=var, data=students_with_clusters, palette='viridis')
    plt.title(f'Distribuição de {var} por Cluster')
    plt.savefig(f'visuals/{var}_by_cluster.png')
    plt.close()

print('Gráficos salvos na pasta "visuals"!')