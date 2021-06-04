# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:54 2020

@author: carlos
"""
#c_dataframes.py
import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)
df1 = pd.DataFrame(arr_pand)
s1 = df1[0]

#operacion con la serie

s2 = df1[1]
s3 = df1[2]
df1[3] = s1
df1[4] = s1* s2

datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns = [
            'Estatura(cm)',
            'Peso(kg)',
            'Edad(anios)'
                ],
        index = [
                'Carlos',
                'Charles']
        )

serie_peso = datos_fisicos_uno['Peso(kg)']
datos_carlos = serie_peso['Carlos']
print(serie_peso)
print(datos_carlos)
#modificar los indices

df1.index =  ['Carlos', 'Charles']
df1.index = ['Wendy', 'Carolina']
df1.columns= ['A','B','C','D','E']

