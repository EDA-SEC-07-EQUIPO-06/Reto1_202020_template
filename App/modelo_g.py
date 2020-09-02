import config as cf
import sys
import csv
import controlador
import reto

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 


def new_catalogo():
    catalogo={"peliculas_1":None, "apuntadorSegunId":None, "directores":None, "generos":None, "actores":None}
    catalogo["peliculas_1"]=lt.newList('ARRAY_LIST',compIDpelicula)
    catalogo["apuntadorSegunId"]=lt.newList('ARRAY_LIST',compIDpelicula)
    catalogo["directores"]=lt.newList("ARRAY_LIST",compDirectores)
    catalogo["generos"]=lt.newList('SINGLE_LINKED',compGenero)
    catalogo["actores"]=lt.newList("ARRAY_LIST",compActores)
    return catalogo


def nueva_entrada_pelicula(ID):

    pelicula={"ID":0, "pelicula":None}
    pelicula["ID"]=ID
    pelicula["pelicula"]=lt.newList("SINGLE_LINKED",compIDpelicula)

    return pelicula


def nuevo_actor(nombre):

    actor={"nombre": "","ref_peliculas":None,"Promedio peliculas ":0.0, "Director con mas colaboraciones: " , ""}
    actor["nombre"]=nombre
    actor["ref_peliculas"]=lt.newList('ARRAY_LIST',compIDpelicula)
    actor["Promedio peliculas "]=lt.newList('ARRAY_LIST',compIDpelicula)
    actor["Director con mas colaboraciones:"]=lt.newList('ARRAY_LIST',compIDpelicula)

    return director

def nuevo_genero(nombre_genero):
    
    genero={"nombre":"", "peliculas":None, "promedio":0}
    genero["nombre"]=nombre_genero
    genero["peliculas"]=lt.newList("SINGLE_LINKED",compGenero)


# agreagar catalagos 

def agregar_pelicula_(catalogo, pelicula):
    
    lt.addLast(catalogo["peliculas_1"], pelicula)

def agregarApuntador (catalogo, ID, pelicula_1):

    peliculas= catalogo["apuntadorSegunId"]
    
    Identidad=nuevaEntradaPelicula(ID)
    lt.addLast(peliculas, Identidad)
    lt.addLast(Identidad["pelicula"], pelicula_1)

def agregar_actor(catalogo, nombre_actor, ID_pelicula):
   
    actores= catalogo["actores"]
    nombres=lt.newList('SINGLE_LINKED',compActores)
    for i in range(1,lt.size(actores)):
        directo=lt.getElement(actores,i)
        nombre=directo["nombre"]
        lt.addLast(nombres,nombre)
    posible_actor= lt.isPresent(nombres, nombre_actor)
    if posible_actor > 0:
        actor=lt.getElement(directores, posibleDirector)
    else:
        actor=nuevo_actor(nombre_actor)
        lt.addLast(actores, actor)
    lt.addLast(actor["ref_peliculas"],ID_pelicula)           #el ID_pelicula es un diccionario
    
    pelicula=ID_pelicula["pelicula"]
    for i in range(1):
        datos=lt.getElement(pelicula,i)
        calificacion=datos["vote_average"]

    actor["promedio"]+=float(promedio)

    #funciones de consulta

def promedio_actor(catalogo, nombre_actor):
    nombres=lt.newList('SINGLE_LINKED',compActores)
    for i in range(1,lt.size(catalogo["actores"])):
        actorr=lt.getElement(catalogo["actores"],i)
        nombre=actor["nombre"]
        lt.addLast(nombres,nombre)
    posible_actor= lt.isPresent(nombres, nombreActores)
    if posibleDirector > 0:
        actorf=lt.getElement(catalogo["actores"], posible_actor)
    else:
        print("error, no encontro actor")
    
    promedio=actorf["promedio"]/lt.size(actorf["ref_peliculas"])

    return promedio


def obtener_peeliculas_x_actor(catalogo, nombreDirector):
    nombres=lt.newList('SINGLE_LINKED',compActores)
    for i in range(1,lt.size(catalogo["actores"])):
        actor=lt.getElement(catalogo["actores"],i)
        nombre=actor["nombre"]
        lt.addLast(nombres,nombre)

    posicion_actor=lt.isPresent(nombres, nombreActor)

    if posicion_actor >0:
        info_actor= lt.getElement(catalogo["actores"],posicion_actor)
        return info_actor
    return None

#Funciones de comparacion

def compIDpelicula(id1,id2):
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compDirectores(nombre1, nombre2):
    
    if (nombre1 == nombre2):
        return 0
    elif nombre1 > nombre2:
        return 1
    else:
        return -1
        
def compGenero(genero1, genero2):
    
    if (genero1 == genero2):
        return 0
    elif genero1 > genero2:
        return 1
    else:
        return -1

def compActores(actor1, actor2):
    
    if (actor1 == actor2):
        return 0
    elif actor1 > actor2:
        return 1
    else:
        return -1

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1