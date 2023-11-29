import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic as GD


# transform to snake_case, lower column names and strip
def clean_column_names(df):
    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a valid DataFrame.")
    
    # create copy
    clean_df = df.copy()
    
    #cleaning
    clean_df.columns= [col.strip() for col in clean_df.columns]
    clean_df.columns= [col.lower() for col in clean_df.columns]
    clean_df.columns= [col.replace(' ', '_') for col in clean_df.columns]
    
    return clean_df

def plot_discrete_var(df):
    for col in df.columns:
        plt.figure(figsize=(10,5))
        ax = sns.countplot(data=df, x=col, hue=col, palette = "crest", legend=False)

        plt.title(f"Distribution of {col}")
        plt.ylabel("Count")
        ax.tick_params(axis='x', rotation=90)
        plt.show()
        
        
def involved_partners(row):
    partners = []
    if row['is_car'] == 1:
        partners.append('car')
    if row['is_bicycle'] == 1:
        partners.append('bicycle')
    if row['is_pedestrian'] == 1:
        partners.append('pedestrian')
    if row['is_motorcycle'] == 1:
        partners.append('motorcycle')
    if row['is_truck'] == 1:
        partners.append('truck')
    if row['is_puplic_transport'] == 1:
        partners.append('puplic_transport')

    return '-'.join(partners)

def cluster_involved(row):
    value_list = ['car','car-bicycle', 'car-motorcycle', 'car-pedestrian', 'car-puplic_transport', 'bicycle', 'bicycle-puplic_transport', 'motorcycle', 'bicycle-pedestrian', 'car-truck',
                  'pedestrian-puplic_transport', 'puplic_transport', 'motorcycle-puplic_transport', 'bicycle-truck', 'bicycle-motorcycle', 'pedestrian-motorcycle', 'car-bicycle-puplic_transport' ]
    if row['involved'] in value_list:
        return row['involved']
    else: 
        return 'other'
    
def get_distance(row):
    latitude = row['latitude']
    longitude = row['longitude']
    point = (latitude, longitude)
    city_center = (52.51916459, 13.405665044) # Alexanderplatz
    distance = round(GD(point, city_center).km,3)
    return distance 
    
