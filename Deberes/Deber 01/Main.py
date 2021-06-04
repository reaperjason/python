from Director import Director
from Pelicula import Pelicula

def main():
    
    ruta_archivo_director = "archivos/directores.txt"
    ruta_archivo_peliculas = "archivos/peliculas.txt"

    id_director_max = obtener_id_final(ruta_archivo_director)
    id_pelicula_max = obtener_id_final(ruta_archivo_peliculas)
    
    opcion_archivo = input("""En que archivo desea trabajar:
    directores (D)
    peliculas (P)\n""")

    print(opcion_archivo)

    if(opcion_archivo.lower() == 'd'):     
        print("director")
        operacion = escoger_operacion()
        
        if(operacion.lower() == 'c'):
            print("Crear")            

            id_director = int(id_director_max)+1
            nombre_apellido_director = input("Ingrese el nombre y apellido\n")
            anio_nacimiento_director = input("Ingrese anio nacimiento\n")
            anio_debut_director = input("Ingrese anio debut\n")
            while(True):
                casado_director_str = input("director actualmente casado S/N\n")
                casado_bool = False
                if(casado_director_str.lower()=='s'):
                    casado_bool = True
                    break;
                elif(casado_director_str.lower()=='n'):
                    casado_bool = False
                    break;
                else:
                    print("ingrese S para si o N para no\n")
                
            calificacion_pelicula_alta_IMDB_director = input("Ingrese pelicula mejor rankeada (IMDB)\n")
            #agregar pelicula del director
            while(True):
                pelicula_nueva = input("Ingresar nueva película(N) o tomar de la lista(L)\n")
                if(pelicula_nueva.lower()=='n'):
                    print("nueva pelicula")
                    #creacion director
                    director = crear_director(id_director, nombre_apellido_director, anio_nacimiento_director,
                    anio_debut_director, casado_bool, calificacion_pelicula_alta_IMDB_director)
                    #datos pelicula
                    id_pelicula = int(id_pelicula_max)+1
                    
                    nombre_pelicula = input("Ingrese nombre de la pelicula\n")
                    fecha_estreno = input("Ingrese año de estreno\n")
                    genero = input("Ingrese el genero de la pelicula\n")
                    while(True):
                        secuela_str = input("La pelicula tiene una secuela S/N\n")
                        secuela_bool = False
                        if(secuela_str.lower() == 's'):
                            secuela_bool = True
                            break;
                        elif(secuela_str.lower() == 'n'):
                            secuela_bool = False
                            break;
                        else:
                            print("Ingrese S o N\n")
                    calificacion_IMDB = input("Ingrese la calificacion de la pelicula(IMDB)\n")
                    #creacion pelicula
                    director.set_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
                    genero, secuela_bool, calificacion_IMDB)
                    #fin creacion director con creacion pelicula
                    #grabar archivo pelicula
                    texto_grabar_pelicula =("\n"+str(id_pelicula)+"\t"+str(id_director)+"\t"+str(nombre_pelicula)+"\t"+str(fecha_estreno)
                    +"\t"+str(genero)+"\t"+str(secuela_bool)+"\t"+str(calificacion_IMDB))
                    archivo_grabar_pelicula=establecer_archivo(ruta_archivo_peliculas,'a')
                    escribir_archivo(archivo_grabar_pelicula,texto_grabar_pelicula)
                    archivo_grabar_pelicula.close()
                    
                    #grabar director
                    id_peliculas_director_final = obtener_id_peliculas_director(director)
                    
                    texto_grabar_director =("\n"+str(id_director)+"\t"+str(nombre_apellido_director)+"\t"+str(anio_nacimiento_director)
                    +"\t"+str(anio_debut_director)+"\t"+str(casado_bool)+"\t"+str(calificacion_pelicula_alta_IMDB_director)+"\t"+str(id_peliculas_director_final))
                    archivo_grabar_director=establecer_archivo(ruta_archivo_director,'a')
                    escribir_archivo(archivo_grabar_director,texto_grabar_director)
                    archivo_grabar_director.close()
                    
                    #nueva pelicula denuevo
                    while(True):
                        otra_pelicula=input("Desea ingresar otra pelicula? S/N\n")
                        if(otra_pelicula.lower() == 's'):
                            print("nueva pelicula")
                            #datos pelicula
                            id_pelicula = int(id_pelicula)+1
                            
                            nombre_pelicula = input("Ingrese nombre de la pelicula\n")
                            fecha_estreno = input("Ingrese año de estreno\n")
                            genero = input("Ingrese el genero de la pelicula\n")
                            while(True):
                                secuela_str = input("La pelicula tiene una secuela S/N\n")
                                secuela_bool = False
                                if(secuela_str.lower() == 's'):
                                    secuela_bool = True
                                    break;
                                elif(secuela_str.lower() == 'n'):
                                    secuela_bool = False
                                    break;
                                else:
                                    print("Ingrese S o N\n")
                            calificacion_IMDB = input("Ingrese la calificacion de la pelicula(IMDB)\n")
                            #creacion pelicula
                            director.set_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
                            genero, secuela_bool, calificacion_IMDB)
                            #fin creacion director con creacion pelicula
                            #grabar archivo pelicula
                            texto_grabar_pelicula =("\n"+str(id_pelicula)+"\t"+str(id_director)+"\t"+str(nombre_pelicula)+"\t"+str(fecha_estreno)
                            +"\t"+str(genero)+"\t"+str(secuela_bool)+"\t"+str(calificacion_IMDB))
                            archivo_grabar_pelicula=establecer_archivo(ruta_archivo_peliculas,'a')
                            escribir_archivo(archivo_grabar_pelicula,texto_grabar_pelicula)
                            archivo_grabar_pelicula.close()
                            
                            #grabar director
                            id_peliculas_director_final = obtener_id_peliculas_director(director)
                            
                            actualizar_archivo_menos_final(ruta_archivo_director)
                            
                            texto_grabar_director =(str(id_director)+"\t"+str(nombre_apellido_director)+"\t"+str(anio_nacimiento_director)
                            +"\t"+str(anio_debut_director)+"\t"+str(casado_bool)+"\t"+str(calificacion_pelicula_alta_IMDB_director)+"\t"+str(id_peliculas_director_final))
                            archivo_grabar_director=establecer_archivo(ruta_archivo_director,'a')
                            escribir_archivo(archivo_grabar_director,texto_grabar_director)

                        elif(otra_pelicula.lower() == 'n'):
                            break;
                        else:
                            print("Escoja N o S")
                    break;
                #tomar de lista
                elif(pelicula_nueva.lower()=='l'):
                    print("Lista")
                    peliculas_lista_archivo = establecer_archivo(ruta_archivo_peliculas, 'r')
                    peliculas_lista = leer_archivo_lineas(peliculas_lista_archivo)
                    peliculas_lista_archivo.close()
                    
                    for pelicula in peliculas_lista:
                        print(pelicula)
                    
                    while(True):
                        id_pelicula = input("escriba el numero(id) de la pelicula\n")
                        #creacion director
                        director = crear_director(id_director, nombre_apellido_director, anio_nacimiento_director,
                        anio_debut_director, casado_bool, calificacion_pelicula_alta_IMDB_director)
                        #creacion pelicula
                        datos_pelicula = obtener_datos_peli_id(peliculas_lista, id_pelicula)
                        if(len(datos_pelicula)== 0):
                            print("Ingrese un id valido")
                        else:
                            nombre_pelicula = datos_pelicula[2]
                            fecha_estreno = datos_pelicula[3]
                            genero = datos_pelicula[4]
                            secuela = datos_pelicula[5]
                            calificacion_IMDB = datos_pelicula[6]
                            director.set_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
                            genero, secuela, calificacion_IMDB)

                            #grabar director
                            id_peliculas_director_final = obtener_id_peliculas_director(director)
                            
                            texto_grabar_director =("\n"+str(id_director)+"\t"+str(nombre_apellido_director)+"\t"+str(anio_nacimiento_director)
                            +"\t"+str(anio_debut_director)+"\t"+str(casado_bool)+"\t"+str(calificacion_pelicula_alta_IMDB_director)+"\t"+str(id_peliculas_director_final))
                            
                            archivo_grabar_director=establecer_archivo(ruta_archivo_director,'a')
                            escribir_archivo(archivo_grabar_director,texto_grabar_director)
                            archivo_grabar_director.close()
                            break;                  
                    break;
                else:
                    print("Escoja N o L")

        elif(operacion.lower() == 'r'):
            print("read")
            while(True):
                opcion_busqueda= input("Desea buscar un director (B)o mostrar todos(T)")
                if(opcion_busqueda.lower()=='b'):
                    id_pelicula_buscar = input("Ingrese id del director")
                    archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
                    lineas = leer_archivo_lineas(archivo_leer_director)
                    archivo_leer_director.close()
                    datos_pelicula=obtener_datos_peli_id(lineas,id_pelicula_buscar)
                    print("id_director	nombre_apellido	anio_nacimiento	anio_debut	casado	calificacion_pelicula_alta_IMDB peliculas_dirigidas(id)")
                    print(datos_pelicula)
                    break;
                elif(opcion_busqueda.lower()=='t'):
                    archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
                    lineas = leer_archivo_lineas(archivo_leer_director)
                    archivo_leer_director.close()
                    for linea in lineas:
                        print(linea)
                    break;
                else:
                    print("Ingrese B o T")
                
        
        elif(operacion.lower() == 'u'):
            print("update")
            archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
            lineas = leer_archivo_lineas(archivo_leer_director)
            archivo_leer_director.close()
            for linea in lineas:
                print(linea)
            while(True):
                id_director = input("\nEscoja el id del director que desea modificar\n")
                indice_director = obtener_indice_lista_id(lineas, id_director)
                print(indice_director)
                if(indice_director <0):
                    print("Ingrese un id valido")
                else:
                    nombre_apellido_director = input("Ingrese el nombre y apellido\n")
                    anio_nacimiento_director = input("Ingrese anio nacimiento\n")
                    anio_debut_director = input("Ingrese anio debut\n")
                    while(True):
                        casado_director_str = input("director actualmente casado S/N\n")
                        casado_bool = False
                        if(casado_director_str.lower()=='s'):
                            casado_bool = True
                            break;
                        elif(casado_director_str.lower()=='n'):
                            casado_bool = False
                            break;
                        else:
                            print("ingrese S para si o N para no\n")
                    calificacion_pelicula_alta_IMDB_director = input("Ingrese pelicula mejor rankeada (IMDB)\n")
                    id_peliculas_director_final = input("Ingrese id de la pelicula\n")
                    while(True):
                        otra_pelicula = input("Desea ingresar otra pelicula S/N\n")
                        if(otra_pelicula.lower()=='s'):
                            id_otra_pelicula =input("Ingrese id de la pelicula\n")
                            id_peliculas_director_final = str(id_peliculas_director_final)+','+str(id_otra_pelicula)
                            
                        elif(otra_pelicula.lower()=='n'):
                            texto_grabar_director =(str(id_director)+"\t"+str(nombre_apellido_director)+"\t"+str(anio_nacimiento_director)
                                +"\t"+str(anio_debut_director)+"\t"+str(casado_bool)+"\t"+str(calificacion_pelicula_alta_IMDB_director)+"\t"+str(id_peliculas_director_final)+"\n")
                            
                            lineas[indice_director] = texto_grabar_director
                            nuevo_archivo_director = establecer_archivo(ruta_archivo_director, 'w')
                            escribir_lineas_archivo(nuevo_archivo_director,lineas)
                            nuevo_archivo_director.close()
                            break;
                        else:
                            print("ingrese S para si o N para no")
                    break;

        elif(operacion.lower() == 'd'):
            print("Delete")
            archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
            lineas = leer_archivo_lineas(archivo_leer_director)
            archivo_leer_director.close()
            for linea in lineas:
                print(linea)
            while(True):
                id_director = input("\nEscoja el id del director que desea eliminar\n")
                indice_director = obtener_indice_lista_id(lineas, id_director)
                print(indice_director)
                if(indice_director <0):
                    print("Ingrese un id valido")
                else:
                    del lineas[indice_director]
                    archivo_director_nuevo = establecer_archivo(ruta_archivo_director, 'w+')
                    for linea in lineas:
                        archivo_director_nuevo.write(linea)
                    
                    archivo_director_nuevo.close()
                    break;
        else:
            print("Escoja una opcion C,R,U,D")

    elif(opcion_archivo.lower() == 'p'):
        print("pelicula")
        operacion = escoger_operacion()
        print(operacion)
        if(operacion.lower() == 'c'):
            print("Crear")
            print("nueva pelicula")
                       
            #datos pelicula
            id_pelicula = int(id_pelicula_max)+1
            
            nombre_pelicula = input("Ingrese nombre de la pelicula\n")
            fecha_estreno = input("Ingrese año de estreno\n")
            genero = input("Ingrese el genero de la pelicula\n")
            while(True):
                secuela_str = input("La pelicula tiene una secuela S/N\n")
                secuela_bool = False
                if(secuela_str.lower() == 's'):
                    secuela_bool = True
                    break;
                elif(secuela_str.lower() == 'n'):
                    secuela_bool = False
                    break;
                else:
                    print("Ingrese S o N\n")
            calificacion_IMDB = input("Ingrese la calificacion de la pelicula(IMDB)\n")
            #mostrar directores
            archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
            lineas = leer_archivo_lineas(archivo_leer_director)
            archivo_leer_director.close()
            for linea in lineas:
                print(linea)
            id_director = input("Ingrese id del director\n")
            #creacion pelicula
            #fin creacion director con creacion pelicula
            #grabar archivo pelicula
            texto_grabar_pelicula =("\n"+str(id_pelicula)+"\t"+str(id_director)+"\t"+str(nombre_pelicula)+"\t"+str(fecha_estreno)
            +"\t"+str(genero)+"\t"+str(secuela_bool)+"\t"+str(calificacion_IMDB))
            
            archivo_grabar_pelicula=establecer_archivo(ruta_archivo_peliculas,'a')
            escribir_archivo(archivo_grabar_pelicula,texto_grabar_pelicula)
            archivo_grabar_pelicula.close()

        elif(operacion.lower() == 'r'):
            print("read")
            archivo_leer_peliculas = establecer_archivo(ruta_archivo_peliculas,'r')
            lineas = leer_archivo_lineas(archivo_leer_peliculas)
            archivo_leer_peliculas.close()
            for linea in lineas:
                print(linea)
        
        elif(operacion.lower() == 'u'):
            print("update")
            archivo_leer_pelicula = establecer_archivo(ruta_archivo_peliculas,'r')
            lineas = leer_archivo_lineas(archivo_leer_pelicula)
            archivo_leer_pelicula.close()
            for linea in lineas:
                print(linea)
            while(True):
                id_pelicula = input("\nEscoja el id de la pelicula que desea modificar\n")
                indice_pelicula = obtener_indice_lista_id(lineas, id_pelicula)
                print(indice_pelicula)
                if(indice_pelicula <0):
                    print("Ingrese un id valido")
                else:
                    nombre_pelicula = input("Ingrese nombre de la pelicula\n")
                    fecha_estreno = input("Ingrese año de estreno\n")
                    genero = input("Ingrese el genero de la pelicula\n")
                    while(True):
                        secuela_str = input("La pelicula tiene una secuela S/N\n")
                        secuela_bool = False
                        if(secuela_str.lower() == 's'):
                            secuela_bool = True
                            break;
                        elif(secuela_str.lower() == 'n'):
                            secuela_bool = False
                            break;
                        else:
                            print("Ingrese S o N\n")
                    calificacion_IMDB = input("Ingrese la calificacion de la pelicula(IMDB)\n")
                    #mostrar directores
                    archivo_leer_director = establecer_archivo(ruta_archivo_director,'r')
                    lineas_director = leer_archivo_lineas(archivo_leer_director)
                    archivo_leer_director.close()
                    for linea in lineas_director:
                        print(linea)
                    id_director = input("Ingrese id del director\n")

                    texto_grabar_pelicula =(str(id_pelicula)+"\t"+str(id_director)+"\t"+str(nombre_pelicula)+"\t"+str(fecha_estreno)
                            +"\t"+str(genero)+"\t"+str(secuela_bool)+"\t"+str(calificacion_IMDB)+"\n")
              
                    lineas[indice_pelicula] = texto_grabar_pelicula
                    nuevo_archivo_pelicula = establecer_archivo(ruta_archivo_peliculas, 'w')
                  
                    escribir_lineas_archivo(nuevo_archivo_pelicula,lineas)
                    nuevo_archivo_pelicula.close()
                    break;
        elif(operacion.lower() == 'd'):
            print("Delete")
            archivo_leer_pelicula = establecer_archivo(ruta_archivo_peliculas,'r')
            lineas = leer_archivo_lineas(archivo_leer_pelicula)
            archivo_leer_pelicula.close()
            for linea in lineas:
                print(linea)
            while(True):
                id_pelicula = input("\nEscoja el id de la pelicula que desea eliminar\n")
                indice_pelicula = obtener_indice_lista_id(lineas, id_pelicula)
                
                if(indice_pelicula <0):
                    print("Ingrese un id valido")
                else:
                    del lineas[indice_pelicula]
                    archivo_pelicula_nueva = establecer_archivo(ruta_archivo_peliculas, 'w+')
                    for linea in lineas:
                        archivo_pelicula_nueva.write(linea)
                    
                    archivo_pelicula_nueva.close()
                    break;
        else:
            print("Escoja una opcion C,R,U,D")
    else:
        print("escoja 'D' o 'P'")



def escoger_operacion():
        opcion_operacion = input(""""Operacion a realizar
    Crear(C)
    Leer(R)
    Actualizar(U)
    Borrar(D)\n""")
        return opcion_operacion
  
def crear_director(id_director, nombre_apellido, anio_nacimiento,
 anio_debut, casado, calificacion_pelicula_alta_IMDB_director):
    
    director = Director()
    
    director.set_id_director = director
    director.set_nombre_apellido = nombre_apellido
    director.set_anio_nacimiento = anio_nacimiento
    director.set_anio_debut = anio_debut
    director.set_casado = casado
    director.set_calificacion_pelicula_alta_IMDB = calificacion_pelicula_alta_IMDB_director
    
    return director

def crear_pelicula(id_pelicula, id_director, nombre_pelicula, fecha_estreno,
genero, secuela, calificacion_IMDB):
    pelicula = Pelicula()
    pelicula.set_id_pelicula = id_pelicula
    pelicula.set_id_director = id_director
    pelicula.set_nombre_pelicula = nombre_pelicula
    pelicula.set_fecha_estreno = fecha_estreno
    pelicula.set_genero = genero
    pelicula.set_secuela = secuela
    pelicula.set_calificacion_IMDB = calificacion_IMDB

    return pelicula

def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def leer_archivo_linea(archivo):
    contenido = archivo.read()
    return contenido

def leer_archivo_lineas(archivo):
    contenido = archivo.readlines()
    return contenido

def escribir_archivo(archivo, texto):
    archivo.write(texto)

def escribir_lineas_archivo(archivo, texto):
    archivo.writelines(texto)

def obtener_id_final(ruta):
    archivo_leer = establecer_archivo(ruta, 'r')
    contenido = archivo_leer.readlines()
    indices = []
    for lineas in contenido[1:]:
        indices.append(lineas.split("\t")[0])
    archivo_leer.close()
    if(len(indices)!=0):
        indice_max=max(indices, key=int)
    else:
        indice_max = 0
    return indice_max

def obtener_id_peliculas_director(director):
    id_peliculas_director=[]
    for pelicula in director.peliculas:
        id_peliculas_director.append(pelicula.get_id_pelicula())
    
    id_peliculas_director_str = str(id_peliculas_director[0])
    for indice in id_peliculas_director[1:]:
        id_peliculas_director_str=id_peliculas_director_str+','+str(indice)
    
    return id_peliculas_director_str
                    
def actualizar_archivo_menos_final(ruta):
    archivo_antiguo = establecer_archivo(ruta, 'r')
    lines = archivo_antiguo.readlines()
    archivo_antiguo.close()
    
    w = open(ruta,'w')
    w.writelines([item for item in lines[:-1]])
    w.close()

def obtener_datos_peli_id(lista_peliculas, id_pelicula):
    arreglo_datos=[]
    for peliculas in lista_peliculas:
        arreglo_datos = peliculas.split()
        if(arreglo_datos[0]==id_pelicula):
            print("encontrado")
            break;
        else:
            arreglo_datos = []
    return arreglo_datos

def obtener_indice_lista_id(lista, id):
    arreglo_datos=[]
    encontrado = False
    contador = 0
    for director in lista[1:]:
        contador=contador+1
        arreglo_datos = director.split()
        if(arreglo_datos[0]==id):
            print("indice encontrado")
            encontrado=True
            break;
        else:
            arreglo_datos = []
    if(encontrado):
        return contador
    else:
        return -1


if __name__ == "__main__":
    while(True):
        main()
