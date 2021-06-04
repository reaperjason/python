from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import random

def generarBloques(n,ancho,alto):
    blocks = []
    
    bloque_size = ancho/int(n)
    bloque_size= int(bloque_size)
    
    for y in range(0, alto, bloque_size):
        for x in range(0, ancho, bloque_size):
            blocks.append(img_array[y:y+bloque_size, x:x+bloque_size])
            
    return blocks


def graficarMatrix(n,blocks,num_pieza_sacada,lista):
    aux = 0
    n = int(n)
    f, axarr = plt.subplots(n,n)
    for x in range(n):
        for y in range(n):
            if(lista[aux] != num_pieza_sacada):
                axarr[x,y].imshow(blocks[lista[aux]])        
                axarr[x,y].axis('off')
            aux= aux+1
    plt.axis('off')
    plt.show()

def tranformarMatrixList(n, matrix):
    lista =[]
    n = int(n)
    for j in range(n):
        for i in matrix[j]:
            lista.append(i)
    return lista
            
#img = Image.open('helmet.jpg')
img = Image.open('heinseberg.jpg')
ancho = 600
alto = 600
new_img = img.resize((ancho,alto))

img_array = np.array(new_img)


plt.imshow(img_array, interpolation='nearest')
plt.show()
        
        
pieza=()
movimientos = 0
pieza_sacada=()
lista_4x4 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_3x3 = [0,1,2,3,4,5,6,7,8]
lista_aux=[]

while True:
    lista_escogida_numero = input("Escoja: Matrix de 4x4 (4) o de 3x3 (3)")
    if(lista_escogida_numero == '3'):
        lista_escogida= lista_3x3           
        lista_aux = lista_3x3           
        break;
    elif(lista_escogida_numero == '4'):
        lista_escogida= lista_4x4
        lista_aux = lista_4x4
        break;
    else:
        print("Escoja 4 o 3 para la dimensión de la matriz")
random.shuffle(lista_escogida)
print('\n'*2)


matrix=[]
while lista_escogida !=[]:
    matrix.append(lista_escogida[:int(lista_escogida_numero)])
    lista_escogida = lista_escogida[int(lista_escogida_numero):]

pieza_sacada = (0,0)
num_pieza_sacada = matrix[0][0]
while True:
    if(lista_escogida_numero == '3'):
        print('\n+----+----+---|')        
    else:
        print('\n+----+----+----+---|')    
    
    for x in range (len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == num_pieza_sacada:
                print('|XX' , end='  ')
            else:
                 print('|' + '{:02d}' .format(matrix[x][y]), end='  ') 
        if(lista_escogida_numero == '3'):
            print('\n+----+----+---|')        
        else:
            print('\n+----+----+----+---|') 

    bloques =  generarBloques(lista_escogida_numero,ancho,alto)
    
    lista_cambiada = tranformarMatrixList(lista_escogida_numero, matrix)
    graficarMatrix(lista_escogida_numero, bloques, num_pieza_sacada, lista_cambiada)
    
    num = input('\nIngresar pieza a mover : ( q ) para salir ')
    if num in ['q','Q']:
        break
    num = int(num)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                pieza = (i,j)
                print(pieza)
    if num > 15:
        print('Movimiento inválido')
    else:
        if(pieza_sacada==(pieza[0]-1,pieza[1]))\
           or(pieza_sacada==(pieza[0]+1,pieza[1]))\
           or(pieza_sacada==(pieza[0],pieza[1]-1))\
           or(pieza_sacada==(pieza[0],pieza[1]+1)):
            matrix[pieza_sacada[0]][pieza_sacada[1]]=num
            matrix[pieza[0]][pieza[1]]=num_pieza_sacada
            pieza_sacada=(pieza[0],pieza[1])
            movimientos = movimientos +1
            print()
            print('Movimientos realizados ',movimientos)
            print(2*'\n')
        else:
            print('Movimiento invalido')
print('Game Over')


