# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:56:36 2020

@author: carlos
"""

import pandas as pd
import math
import numpy as np

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupar_artista = seccion_df.groupby('artist')

print(type(df_agrupar_artista))

for columna, df_agrupado in df_agrupar_artista:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)
    
    
    ##calculos
a = seccion_df["units"].value_counts()

##Verificar si la columna esta vacia
print(seccion_df['units'].empty)
print(a.empty)

def llenar_valores_vacios (series, tipo):
    lista_valores = series.value_counts()
    ##si esta vacio no hacemos nada
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores +1 
                    suma = suma + valor
                else:
                    pass
            promedio = suma /numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        if(tipo == 'mas repetido'):
            mas_repetido = series.value_counts().idxmax()
            series_valores_llenos = series.fillna(mas_repetido)
            return series_valores_llenos

def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista,df in df_artist:
        copia_df = df.copy()
        
        serie_w = copia_df['width']
        serie_h = copia_df['height']
        serie_u = copia_df['units']
        serie_t = copia_df['title']
        
        copia_df.loc[:,'width'] = llenar_valores_vacios(
                serie_w,
                'promedio')
        
        copia_df.loc[:,'height'] = llenar_valores_vacios(
                serie_h,
                'promedio')
        copia_df.loc[:,'units'] = llenar_valores_vacios(
                serie_u,
                'mas repetido')
        copia_df.loc[:, 'title'] = llenar_valores_vacios(
                serie_t,
                'mas repetido'
                )
        lista_df.append(copia_df)
    df_completo = pd.concat(lista_df)
    return df_completo

df_lleno = transformar_df(seccion_df)
        
        
        
        