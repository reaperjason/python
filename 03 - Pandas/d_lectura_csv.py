# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:10:12 2020

@author: carlos
"""
import pandas as pd
import os

path = "./data/artwork_data.csv"

df1 = pd.read_csv(
        path,
        nrows = 10
        )
columnas = ['id','artist','title',
            'medium','year'
            ,'acquisitionYear','width'
            ,'height','units']
df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas
        )

df3 = pd.read_csv(
        path,
        usecols = columnas,
        index_col='id'
        )

path_guardado = "./data/artwork_data.pickle"
#artwork_data.pickle

df3.to_pickle(path_guardado)
df4 = pd.read_pickle(path_guardado)

