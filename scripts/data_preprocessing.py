import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np


students_data = pd.read_csv('data/Students_Grading_Dataset.csv')


clustering_data = students_data[[
    'Attendance (%)', 'Total_Score', 'Study_Hours_per_Week',
    'Stress_Level (1-10)', 'Sleep_Hours_per_Night'
]].copy()


clustering_data['Attendance (%)'] = clustering_data['Attendance (%)'].fillna(clustering_data['Attendance (%)'].median())


scaler = StandardScaler()
clustering_data_scaled = scaler.fit_transform(clustering_data)
np.save('data/clustering_data_scaled.npy', clustering_data_scaled)
