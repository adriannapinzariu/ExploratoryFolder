#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib as ax
from matplotlib import pyplot as plt


# In[10]:


path = "/Users/adriannapinzariu/Desktop/LIDC_newMode_2022 (1).csv"


# In[11]:


df = pd.read_csv(path)


# In[12]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Size - Area
df.hist(column='Area', figsize=[10, 10], bins=15)
plt.xlabel('Area')
plt.ylabel('Frequency')
plt.title('Area Frequency Distribution of Lung Nodules in LIDC Data')
plt.show()


# In[26]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Size - Perimeter
df.hist(column='Perimeter', figsize=[10, 10], bins=15)
plt.xlabel('Perimeter')
plt.ylabel('Frequency')
plt.title('Perimeter Frequency Distribution of Lung Nodules in LIDC Data')
plt.show()


# In[25]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Shape - Circularity
df.hist(column='Circularity', figsize=[10, 10], bins=15)
plt.xlabel('Circularity') 
plt.ylabel('Frequency')
plt.title('Circularity Frequency Distribution of Lung Nodules in LIDC Data')
plt.show()


# In[13]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Shape - Solidity
df.hist(column='Solidity', figsize=[10, 10], bins=15)
plt.xlabel('Solidity') # find what metric to use for area 
plt.ylabel('Frequency')
plt.title('Solidity Frequency Distribution of Lung Nodules in LIDC Data')
plt.show()


# In[27]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Intensity - Standard Deviation of the Grey Level of Pixels
df.hist(column='SDIntensity', figsize=[10, 10], bins=15)
plt.xlabel('Standard Deviation Intensity') # find what metric to use for area 
plt.ylabel('Frequency')
plt.title('Standard Deviation Frequency Distribution of the Grey Level of Pixels of Lung Nodules in LIDC Data')
plt.show()


# In[14]:


# Historgram (Frequency Measurement) Graphs for Image Features:
    # Nodule Intensity - Mean Intensity of the Grey Level of Pixels
df.hist(column='MeanIntensityBG', figsize=[10, 10], bins=15)
plt.xlabel('Mean Intensity') # find what metric to use for area 
plt.ylabel('Frequency')
plt.title('Mean Intensity Frequency Distribution of the Grey Level of Pixels of Lung Nodules in LIDC Data')
plt.show()


# In[17]:


ratings = [1,2,3,4,5]
frequency = [337,562,1196,357,235]
plt.bar(ratings, frequency)
plt.xlabel('Malignancy Rating')
plt.ylabel('Frequency of Rating')
plt.title('Malignancy Ratings of Lung Nodules in LIDC Data')
plt.show()


# In[21]:


area_data = df['Spiculation']
area_data.value_counts()


# In[28]:


ratings2 = [1,2,3,4,5]
frequency2 = [1850, 476, 187, 100, 74]
plt.bar(ratings2, frequency2)
plt.xlabel('Spiculation')
plt.ylabel('Frequency')
plt.title('Spiculation of Lung Nodules in LIDC Data')
plt.show()


# In[29]:


area_data = df['Texture']
area_data.value_counts()


# In[30]:


ratings3 = [1,2,3,4,5]
frequency3 = [62,145,210,259,2011]
plt.bar(ratings3, frequency3)
plt.xlabel('Texture')
plt.ylabel('Frequency')
plt.title('Texture of Lung Nodules in LIDC Data')
plt.show()


# In[ ]:




