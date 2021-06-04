# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:18 2020

@author: carlos
"""

import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc
filtrado_horizontal = df.loc[1035] #serie
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)
 
#f. vertical
serie_vertical = df['artist']
#print(serie_vertical)
#print(serie_vertical.index)

#filtado por indice
df_1035 = df[df.index == 1035]

#filtrar por indice
segundo = df.loc[1035]
#filtrar por arreglo de indices
segundo = df.loc[[1035, 1036]]
#filtrado desde x indice a y indice
segundo = df.loc[3:5]

segundo = df.loc[1035, 'artist']
#varios indices
segundo = df.loc[1035, ['artist', ' medium']]

#iloc -  indices en 0
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4]

#############

datos = {
        "nota 1":{
                "pepito": 7,
                "juanita": 8,
                "maria":9
                },
        "nota 2":{
                "pepito": 7,
                "juanita": 8,
                "maria":9
                },
        "disciplina":{
                "pepito": 4,
                "juanita": 9,
                "maria":2
                },
        }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] <= 7
condicion_nota2 = notas["nota 2"] <= 7
condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[ condicion_disc,["nota 1"]]
pasaron = notas.loc[condicion_nota][condicion_disc][condicion_nota2]

notas.loc["maria", "disciplina"] = 7
notas.loc[:,"discipina"] = 7

#################Promedio de las 3 notas
promedio = (notas["nota 1"]+notas["nota 2"]+notas["disciplina"])/3


