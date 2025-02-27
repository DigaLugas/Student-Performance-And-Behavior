import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

students_with_clusters = pd.read_csv('data/students_with_clusters.csv')

students_with_clusters['Cluster'].value_counts()
sns.set_theme(style='whitegrid')

plt.figure(figsize=(8, 6))
sns.boxplot(x='Cluster', y='Total_Score', data=students_with_clusters)
plt.title('Distribuição das Notas por Cluster')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Cluster', y='Stress_Level (1-10)', data=students_with_clusters)
plt.title('Nível de Estresse por Cluster')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Cluster', y='Study_Hours_per_Week', data=students_with_clusters)
plt.title('Horas de Estudo por Semana por Cluster')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Study_Hours_per_Week', y='Total_Score', hue='Cluster', data=students_with_clusters, palette='viridis')
plt.title('Clusters: Horas de Estudo vs. Nota Total')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Attendance (%)', y='Stress_Level (1-10)', hue='Cluster', data=students_with_clusters, palette='viridis')
plt.title('Clusters: Frequência vs. Nível de Estresse')
plt.show()