# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 07:25:55 2020

@author: carlos
"""
import numpy as np
from scipy import ndimage
from scipy import misc
import pandas as pd

#2
vector_zeros = np.zeros(10) 

#3
vector_zeros_uno = np.zeros(10)
vector_zeros_uno[4] = 1

#4
vector_cincuenta = np.arange(50)
vector_cincuenta = vector_cincuenta[::-1]

#5
matrix_3_por_3 = np.arange(9)
matrix_3_por_3 = matrix_3_por_3.reshape(3,3)

#6
arreglo = [1,2,0,0,4,0]
arreglo_zeros = np.equal(arreglo,0)
indices = np.arange(len(arreglo))
indices_cero = (indices[arreglo_zeros])

#7
m_identidad = np.eye(3)

#8
random = np.random.rand(3,3,3)
print(random)

#9
matrix_diez = np.arange(100)
matrix_diez = matrix_diez.reshape(10,10)
mayor = matrix_diez.max()
menor = matrix_diez.min()

#10
mapache = misc.face()
unicos = np.unique(mapache.reshape(-1, mapache.shape[2]), axis=0)

#11
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista =pd.Series(mylist)
serie_diccionario = pd.Series(mydict)

#12
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
dataframe = pd.DataFrame(ser, index = mylist)

#13
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
serie3 = pd.concat([ser1, ser2])

#14
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
def filtrar(valor_serie):
    aux = False
    for x in ser2:
        if(valor_serie != x):
            aux = True
        else:
            return None
    if(aux):
        return valor_serie
    
obtener_items = ser1.map(filtrar)
        
#15
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
df1= pd.DataFrame(ser1)
df2= pd.DataFrame(ser2)
serie_no_comunes = pd.concat([df1,df2]).drop_duplicates().reset_index(drop=True)


#16
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
numero_a = ser.str.count('a')
df16 = pd.DataFrame(numero_a)
numero_a_final = df16.sum(axis = 0)

#17


#18
ser = pd.Series(np.random.randint(1, 10, 35))
#shape(7,5)
ser_18 = ser.values.reshape(7,5)

#19
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
print(ser[pos])

#20
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
