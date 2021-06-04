# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:15:17 2020

@author: carlos
"""

import numpy as np
import pandas as pd

#1
filas = np.array(range(60)).reshape((10,6))
data_frame = pd.DataFrame(
        filas,
        columns = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F'
                ],
        index = [
                'Carlos',
                'Charles',
                'Dave',
                'Ignacio',
                'Saul',
                'Pedro',
                'Alejandro',
                'Alex',
                'Jill',
                'Walter',
                ]
        )
#5 primeros
print(data_frame.head(5))
#5 ultimos
print(data_frame.tail(5))

#2
arreglo = np.random.randint(0,10, 24).reshape(6,4)
dates = pd.date_range('1/1/2000', periods=6)
data_frame2 = pd.DataFrame(
        arreglo,
        columns = [
            'A',
            'B',
            'C',
            'D'
                ],
        index =  dates
        )

#4
arreglo = np.random.randint(0,10,size=(10,6))
data_frame4 = pd.DataFrame(arreglo)
print("columnas")
print(data_frame4.columns)
print("valores")
print(data_frame4.values)

#5
arreglo = np.random.randint(0,10,size=(10,6))
data_frame5 = pd.DataFrame(arreglo)
print(data_frame.describe())

#6
arreglo = np.random.randint(0,10,size=(10,6))
data_frame6 = pd.DataFrame(arreglo)
print(data_frame6.transpose())

#7
arreglo = np.random.randint(0,10,size=(10,6))
data_frame7 = pd.DataFrame(arreglo)
print("Pregunta 7")
print(data_frame7.sort_values([0], ascending=True))
print('\n')
print(data_frame7.sort_values([0], ascending=False))
print('\n')
print(data_frame7.sort_values([1], ascending=True))
print('\n')
print(data_frame7.sort_values([1], ascending=False))
print('\n')
print(data_frame7.sort_values([2], ascending=True))
print('\n')
print(data_frame7.sort_values([2], ascending=False))
print('\n')
print(data_frame7.sort_values([3], ascending=True))
print('\n')
print(data_frame7.sort_values([3], ascending=False))
print('\n')
print(data_frame7.sort_values([4], ascending=True))
print('\n')
print(data_frame7.sort_values([4], ascending=False))
print('\n')
print(data_frame7.sort_values([5], ascending=True))
print('\n')
print(data_frame7.sort_values([5], ascending=False))
print('\n')

#8
arreglo = np.random.randint(0,10,size=(10,6))
data_frame8 = pd.DataFrame(arreglo)
mayores_7 = data_frame8 > 7
data_frame8_filtrado = data_frame8[mayores_7]

#9
arreglo = np.random.randint(0,10,size=(10,6))
data_frame9 = pd.DataFrame(arreglo)
mayores_7 = data_frame9 > 3
data_frame9_NaN = data_frame9[mayores_7]
data_frame9_llenado = data_frame9_NaN.fillna(0)

#10
arreglo = np.random.randint(0,10,size=(10,6))
data_frame10 = pd.DataFrame(arreglo)
media10 = (data_frame10.mean())
mediana10=(data_frame10.median())
promedio10 =(data_frame10.std())

#11
arreglo = np.random.randint(0,10,size=(10,6))
data_frame11A = pd.DataFrame(arreglo)

arreglo = np.random.randint(0,10,size=(10,6))
data_frame11B = pd.DataFrame(arreglo)

data_frame11_final = vertical_stack = pd.concat([data_frame11A, data_frame11B])

#12
data = [[         
        'Carlos0',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ],
['Carlos1',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ],
['Carlos2',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ],
['Carlos3',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ],
['Carlos4',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ],
['Carlos5',
        'Charles',
        'Dave',
        'Ignacio',
        'Saul',
        'Pedro',
        'Alejandro',
        'Alex',
        'Jill',
        'Walter',
        ]
]

data_frame12 = pd.DataFrame(data)
data_frame12 = data_frame12.transpose()

data_frame12['01'] = data_frame12[[0, 1]].agg('-'.join, axis=1)
data_frame12['23'] = data_frame12[[2, 3]].agg('-'.join, axis=1)
data_frame12['45'] = data_frame12[[4, 5]].agg('-'.join, axis=1)

#13
arreglo = np.random.randint(0,10,size=(10,6))
data_frame13 = pd.DataFrame(arreglo)
columna0= (data_frame13[0].value_counts())
columna1= (data_frame13[1].value_counts())
columna2= (data_frame13[2].value_counts())
columna3= (data_frame13[3].value_counts())
columna4= (data_frame13[4].value_counts())
columna5= (data_frame13[5].value_counts())

#14
arreglo = np.random.randint(0,10,size=(10,3))
data_frame14 = pd.DataFrame(
        arreglo,
        columns = [
            'A',
            'B',
            'C'
                ],
        )

data_frame14['D'] = data_frame14['A']*data_frame14['B']
data_frame14['D'] = data_frame14['D']/data_frame14['C']
