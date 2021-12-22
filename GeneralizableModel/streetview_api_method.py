# -*- coding: utf-8 -*-
"""

@author: Neypatraiky, Rimbot & Habert
"""

# Load libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import urllib as url
import urllib as url2
import requests as req
import os
import math
import pickle


def angleFromCoordinate(node1,node2): 
    """" 
    returns the bearing angle between the two nodes
    
    """

    startLong= math.radians(node1[1])
    startLat= math.radians(node1[0])
    endLong = math.radians(node2[1])
    endLat= math.radians(node2[0])
    
    dLong = endLong - startLong

    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0)/math.tan(startLat/2.0+math.pi/4.0))
    
    if abs(dLong) > math.pi:
        if dLong > 0.0:
            dLong = -(2.0 * math.pi - dLong)
        else:
            dLong = (2.0 * math.pi + dLong)

    bearing = (math.degrees(math.atan2(dLong, dPhi)) + 360.0) % 360.0
    
    return int(bearing)
    
def create_api(lati,long,width,height,head,pitch,key):
    
    """" 
    creates a streetview API link with the specified paremeters
    lati, long : latitude and longitude coordinates
    width, height: size in pixels of the streetview image
    head,picth: horizontal and verticasl orientation of the image
    key: unique personal API key
    
    """
    
    # the following lines are to ensure that the length of the coordinates is long enough
    lat = str(lati)
    if len(lat) < 14:
        i = 14 - len(lat)
        for j in range(i):
            lat = lat + '0'
            
    lng = str(long)
    if len(lng) < 14:
        i = 14 - len(lat)
        for j in range(i):
            lng = lat + '0'
    

    # create the url link
    api = f'https://maps.googleapis.com/maps/api/streetview?size={width}x{height}+&location='+lat+','+lng+f'&heading={head}&pitch={pitch}&key={key}'
    
    return api

def create_metadata(lati,long,width,height,head,pitch,key):
    """" 
    creates a streetview API metadata with the specified paremeters
    lati, long : latitude and longitude coordinates
    width, height: size in pixels of the streetview image
    head,picth: horizontal and verticasl orientation of the image
    key: unique personal API key
    
    """
    
    # the following lines are to ensure that the length of the coordinates is long enough
    lat = str(lati)
    if len(lat) < 14:
        i = 14 - len(lat)
        for j in range(i):
            lat = lat + '0'
    lng = str(long)
    if len(lng) < 14:
        i = 14 - len(lat)
        for j in range(i):
            lng = lat + '0'
    
    # create the metadata url link
    metadata = f'https://maps.googleapis.com/maps/api/streetview/metadata?size={width}x{height}+&location='+lat+','+lng+f'&heading={head}&pitch={pitch}&key={key}'
    
    return metadata


def get_metadata_info(link):
    """ 
    get the metadata info as a string
    
    """
    f = req.get(link)
    info = f.text
    return info


def get_location(metadata):
    """
    get the location in the metadata
    
    """
    coord_lat = metadata.find('"lat" : ')
    end_lat = metadata.find(',\n      "lng"')
    coord_lng= metadata.find('"lng" : ')
    end_lng = metadata.find('\n   }')
    return [float(metadata[coord_lat+8:end_lat]),float(metadata[coord_lng+8:end_lng])]       

