# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:53:48 2021

@author: Neypatraiky, Rimbot & Habert
"""

# for loading/processing the images  
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 
from keras.applications.vgg16 import preprocess_input 

# models 
from keras.applications.vgg16 import VGG16 
from keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# for everything else
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle

def extract_features(file, model):
    """ Extract features on images
        INPUT:
            - (string) file: path of the images
            - (Model) model: model to use to extract features on images
        OUTPUT:
            - (array) features: features on images got with the input model
    """
    # load the image as a 224x224 array
    img = load_img(file, target_size=(224,224))
    # convert from 'PIL.Image.Image' to numpy array
    img = np.array(img) 
    # reshape the data for the model reshape(num_of_samples, dim 1, dim 2, channels)
    reshaped_img = img.reshape(1,224,224,3) 
    # prepare image for model
    imgx = preprocess_input(reshaped_img)
    # get the feature vector
    features = model.predict(imgx, use_multiprocessing=True)
    return features


# function that lets you view a cluster (based on identifier)        
def view_cluster(cluster, groups):
    """ Plot clusters with belonging images
        INPUT:
            - (int) cluster: number of the cluster
            - (string) groups: paths of files
        OUTPUT:
            - (plot) clusters with belonging images
    """
    fig = plt.figure(figsize = (25,25))
    fig.suptitle("Cluster " + str(cluster), fontsize=16)
    # gets the list of filenames for a cluster
    files = groups[cluster]
    # only allow up to 30 images to be shown at a time
    if len(files) > 30:
        print(f"Clipping cluster size from {len(files)} to 30")
        files = files[:29]
    # plot each image in the cluster
    for index, file in enumerate(files):
        plt.subplot(10,10,index+1);
        img = load_img(file)
        img = np.array(img)
        plt.imshow(img)
        plt.axis('on')

def vgg16_cluster(path,SD):
    """ CLustering with VGG16 Neural Network
        INPUT:
            - (string) path: path of the set of images
            - (list) SD: list of labels of set of images
        OUTPUT:
            - (list) feat: features of VGG clustering for each image
            - (path) filenames: filenames of images in each cluster
    """
    
    # change the working directory to the path where the images are located
    os.chdir(path)
    
    # this list holds all the image filename
    raw_images = []
    
    # creates a ScandirIterator aliased as files
    with os.scandir(path) as files:
      # loops through each file in the directory
        for file in files:
            if file.name.endswith('.jpg'):
              # adds only the image files to the raw_images list
                raw_images.append(file.name)
            
    model = VGG16()
    model = Model(inputs = model.inputs, outputs = model.layers[-2].output)
    
    data = {}

    # loop through each image in the dataset
    for image in raw_images:
        # try to extract the features and update the dictionary
        try:
            feat = extract_features(image,model)
            data[image] = feat
        # if something fails, save the extracted features as a pickle file (optional)
        except:
            with open(path,'wb') as file:
                pickle.dump(data,file)
                
        # get a list of the filenames
    filenames = np.array(list(data.keys()))
    
    # get a list of just the features
    feat = np.array(list(data.values()))
    
    # reshape so that there are 210 samples of 4096 vectors
    feat = feat.reshape(-1,4096)
    
    # get the unique labels (from the Labels_Raw_StreetViewImages.xlsx)
    df = SD.copy()
    label = df.index.tolist()
    unique_labels = list(set(label))
    
    return feat, filenames

    
def vgg16_groups(feat, filenames, n_clusters, n_components, random_state):
    """ Group images given the amount of clusters and features' components
        INPUT:
            - (list) feat: features of VGG clustering for each image
            - (path) filenames: filenames of images in each cluster
            - (int) n_clusters: number of clusters chosen to perform the clustering
            - (int) n_components: number of components to keep in PCA to reduce dimensionality
            - (int) random_state: seed that will always yield the same result
        OUTPUT:
            - (array) groups: array with cluster IDs and images belonging to each cluster
    """
    
    # reduce the amount of dimensions in the feature vector
    pca = PCA(n_components= n_components, random_state = random_state)
    pca.fit(feat)
    x = pca.transform(feat)
    
    # cluster feature vectors ------ changed from n_clusters=len(unique_labels)
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(x)
    
    # holds the cluster id and the images { id: [images] }
    groups = {}
    for file, cluster in zip(filenames,kmeans.labels_):
        if cluster not in groups.keys():
            groups[cluster] = []
            groups[cluster].append(file)
        else:
            groups[cluster].append(file)

    return groups

def groups_int(groups):
    """ Sort images within each cluster
        INPUT:
            - (array) groups: array with cluster IDs and images belonging to each cluster
        OUTPUT:
            - (array) sorted groups: sorted array with cluster IDs and images belonging to each cluster
    """
    group_list = []
    length = len(groups)
    for i in range(length):
        coord = groups[i].find(".jpg")
        group_list.append(groups[i][0:coord])
    
    group = [int(el) for el in group_list]
    return np.transpose(sorted(group))

def groups_to_int(groups):
    """ Lis of images within each cluster
        INPUT:
            - (array) groups: array with cluster IDs and images belonging to each cluster
        OUTPUT:
            - (array) list groups: list with cluster IDs and images belonging to each cluster
    """
    groups_list = []
    for i in range(10):
        gr = groups_int(groups[i])
        groups_list.append(gr)
    return groups_list


def onehot_groups(groups,nb_views):
    """ Sort images within each cluster
        INPUT:
            - (array) groups: array with cluster IDs and images belonging to each cluster
            - (int) nb_views: number of images within the dataset
        OUTPUT:
            - (array <n_clusters>x<nb_views>) group_onehot: one hot encoded array of images in clusters
    """
    n_clusters = len(groups)
    group_onehot = np.zeros((n_clusters,nb_views))
    for i,groups in enumerate(groups):
        group_onehot[i,groups] = 1
    
    return group_onehot