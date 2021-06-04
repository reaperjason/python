# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:38:56 2020

@author: carlos
"""
import numpy as np
import pandas as pd
import xlsxwriter

#archivo creado en clases
path_pickle = "./data/artwork_data.pickle"
df = pd.read_pickle(path_pickle)
sub_df = df.iloc[49980:50519,:].copy()

num_artistas = sub_df['artist'].value_counts()

ultimo_numero = len(num_artistas.index) + 1

artistas = num_artistas.index


path_grafico= './data/artwork_data_grafico.xlsx'

workbook = xlsxwriter.Workbook(path_grafico)
hoja_artistas = workbook.add_worksheet('Artistas')

hoja_artistas.write('A1', 'Artista')
hoja_artistas.write('B1', 'Total')

for i in range(num_artistas.size):
    hoja_artistas.write(f'A{i + 2}', artistas[i])
    hoja_artistas.write(f'B{i + 2}', num_artistas[artistas[i]])

chart = workbook.add_chart({'type': 'column'})
chart.set_title({'name': 'Artistas y número canciones'})
chart.set_size({'width': 720, 'height': 576})
chart.add_series({
    'categories': '=Artistas!$A$2:$A$85',
    'values':     '=Artistas!$B$2:$B$85',
    'line':       {'color': 'red'},
})
hoja_artistas.insert_chart('D7', chart)

workbook.close()
