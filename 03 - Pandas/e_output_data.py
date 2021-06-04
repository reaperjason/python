# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:29:08 2020

@author: carlos
"""
import sqlite3
import pandas as pd

path_guardado = "./data/artwork_data.pickle"
df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519,:].copy()

#tipos archivos
#JSON
#Excel
#SQL

#conexion con excel
path_excel = "./data/artwork_data.xlsx"
sub_df.to_excel(path_excel)
sub_df.to_excel(path_excel, index = False)

columnas = ['artist','title','year']

sub_df.to_excel(path_excel, columns = columnas)

#Multiples hojas de trabajo
path_excel_mt = "./data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt,
                        engine = 'xlsxwriter')
sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save()

#formato condicional

num_artistas = sub_df['artist'].value_counts()

print(type(num_artistas))
print(num_artistas)

path_excel_colores = "./data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')

num_artistas.to_excel(writer,
                      sheet_name = 'Artistas')

hoja_artistas = writer.sheets['Artistas']

# Formato #

ultimo_numero = (len(num_artistas.index) + 1)

# rango_celdas = 'B2:B{}'.format()

rango_celdas = f'B2:B{ultimo_numero}' # B2:B85
rango_celdas_c = f'C2:C{ultimo_numero}' # C2:C85

print(rango_celdas)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}
hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

hoja_artistas.conditional_format(rango_celdas_c, formato_artistas)

writer.save()

#SQL
with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('tabla_mysql', conexion)

#Json
sub_df.to_json('artistas.json')

sub_df.to_json('artistas_tabla.json', orient = 'table')