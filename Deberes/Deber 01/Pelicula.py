class Pelicula:
    __id_pelicula = None
    __id_director = None

    __nombre_pelicula = None    
    __fecha_estreno = None
    __genero = None
    __secuela = None
    ___calificacion_IMDB = None
    
    def __init__(self):
        print("contructor pelicula")

    def set_id_pelicula(self, id_pelicula):
        self.__id_pelicula = id_pelicula
    
    def set_id_director(self, id_director):
        self.__id_director = id_director
    
    def set_nombre_pelicula(self, nombre_pelicula):
        self.__nombre_pelicula = nombre_pelicula

    def set_fecha_estreno(self, fecha_estreno):
        self.__fecha_estreno = fecha_estreno

    def set_genero(self, genero):
        self.__genero = genero

    def set_secuela(self, secuela):
        self.__secuela = secuela

    def set_calificacion_IMDB(self, calificacion_IMDB):
        self.__calificacion_IMDB = calificacion_IMDB


    def get_id_pelicula(self):
        return self.__id_pelicula
    
    def get_id_director(self):
        return self.__id_director
    
    def get_nombre_pelicula(self):
        return self.__nombre_pelicula

    def get_fecha_estreno(self):
        return self.__fecha_estreno

    def get_genero(self):
        return self.__genero

    def get_secuela(self):
        return self.__secuela

    def get_calificacion_IMDB(self):
        return self.__calificacion_IMDB
    
