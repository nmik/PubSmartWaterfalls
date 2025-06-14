import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Read the csv file containing the UMAP embeddings
def read_umap_embeddings(file_path):
    df = pd.read_csv(file_path)
    return df

embedding_df = read_umap_embeddings('GRB_UMAP_2D_3D.csv')

# select some famous examples:
GRB_LIST = ['GRB170817529', 
            'GRB200415367', 'GRB180128215', 'GRB231115650', 
            'GRB221009553', 'GRB200826187', 'GRB230307656', 'GRB211211549',
            'GRB230812790']
GRB_TAGS = ['GRB 170817A', 
            'GRB 200415A', 'GRB 180128A', 'GRB 231115A',
            'GRB 221009A', 'GRB 200826A', 'GRB 230307A', 'GRB 211211A',
            'GRB 230812A']
GRB_COLOR = ['cornflowerblue', 
             'goldenrod', 'gold', 'yellow',
             'magenta', 'mediumpurple', 'limegreen', 'green', 
             'red']
GRB_MARKER = ['s', 
              'D', 'D', 'D',
              'X', 'o', 's', 's', 
              'p']

#plot the 2D UMAP embeddings

plt.figure(figsize=(10, 8))
plt.scatter(embedding_df['2dumap1'], embedding_df['2dumap2'], 
            color='lightgray', marker='o', s=10, alpha=0.5, label='Unlabeled')
# Plot the selected GRBs with their respective colors and markers
for i, grb in enumerate(GRB_LIST):
    grb_data = embedding_df[embedding_df['name'] == grb]
    plt.scatter(grb_data['2dumap1'], grb_data['2dumap2'], 
                color=GRB_COLOR[i], marker=GRB_MARKER[i], 
                label=GRB_TAGS[i], s=100)
plt.title('2D UMAP Embeddings of GRBs')
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.legend()

#same figure but with 3D UMAP embeddings
plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')      
ax.scatter(embedding_df['3dumap1'], embedding_df['3dumap2'], embedding_df['3dumap3'], 
           color='lightgray', marker='o', s=10, alpha=0.5, label='Unlabeled')
# Plot the selected GRBs with their respective colors and markers
for i, grb in enumerate(GRB_LIST):
    grb_data = embedding_df[embedding_df['name'] == grb]
    ax.scatter(grb_data['3dumap1'], grb_data['3dumap2'], grb_data['3dumap3'], 
               color=GRB_COLOR[i], marker=GRB_MARKER[i], 
               label=GRB_TAGS[i], s=100)
ax.set_title('3D UMAP Embeddings of GRBs')
ax.set_xlabel('UMAP 1')
ax.set_ylabel('UMAP 2')
ax.set_zlabel('UMAP 3')
ax.legend() 


plt.show()
