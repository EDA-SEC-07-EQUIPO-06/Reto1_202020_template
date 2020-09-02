import config as cf
import sys
import csv
import modelo
import reto

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 


def ranking_peliculas()-> list:
    respuesta=[]
    best_count=[]
    worts_average=[]
    respuesta.append("10 BEST COUNT : ",best_count,"---","5 WORST AVERAGE : ",worts_average)
    lista_f={}
    filas= len(lst)
    columnas=0
    
    if filas>0:
        columnas=len(lst[0])
        
    for i in range(filas):
        for j in range(columnas): 

          dic= {}
          nombre= lst[i][6]
        
          dic[nombre] = movies[i][19]
          bC.append( dic )
          
    
    for i in range(filas):
        for j in range(columnas): 


          dic= {}
          nombre= lst[i][6]
        
          dic[nombre] = movies[i][18]
          wA.append( dic )

    #falta ordenar los resultados de mayor a menor
    r_final = insertionsort(r)
 
    return r_final



            

def conocer_actor(nombre:str, lst2:list, lst:list):
     
    id_1= lst[1][0] 
    id_2 =lst2[i][0]


    peliculas_que_participo= []
    numero_peliculas= len(peliculas_que_participo)
    promedio = 

    if filas>0:
        columnas=len(lst[0])
        
    for i in range(filas):
        for j in range(columnas):

            if (id_1 == id_2) and (nombre in lst2) :

                # buscar peliculas
                if lst2[i][j] == nombre:
                    id == lst2[i][0] 

                    if id in lst:
                        posicion= lst.index(id)
                        #
                        nombre_pelicula= 
                        peliculas_que_participo.append(nombre_pelicula)

                # buscar promedio
                # mas colaboraciones 


#catalogo 
peliculas = []

actores = []

calificacion_peliculas_x_actor= []

numero_peliculas_x_actor = len(peliculas_de_un_actor)

peliculas.append(peliculas_de_un_actor)

def promedio_calificacion_peliculas(calificacion_peliculas_x_actor:list) -> int:

    for i in calificacion_peliculas_x_actor:

        suma += i

    promedio = suma/ len(calificacion_peliculas_x_actor)
        
return promedio


def ranking_genero():

