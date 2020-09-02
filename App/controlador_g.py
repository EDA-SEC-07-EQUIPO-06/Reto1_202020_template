import config as cf
import sys
import csv
import modelo
import reto

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 

def iniciarCatalogo():
    """
    Inicia catalogo vacio desde el modelo
    """
    catalogo=modelo.newCatalog()
    return catalogo


def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

def load_peliculas():
    lst = loadCSVFile(peliculas,compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def load_actores():
    lst = loadCSVFile(actores,compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def cargarDatos(catalogo,actores,peliculas):
    """
    Carga datos desde archivos csv al modelo
    """
    cargar_peliculas(catalogo, peliculas)
    cargar_actores(catalogo, actores)

def cargar_peliculas(catalogo, peliculas):
    """
    Carga datos de peliculas al catalogo bajo la lista de peliculas
    Crea apuntador que relaciona ID con datos de pelicula
    """
    archivo=load_peliculas(peliculas)
    for i in range(1,lt.size(archivo)):
        elemento=lt.getElement(archivo,i)
        modelo.agregar_pelicula(catalogo, elemento)
        ID=int(elemento["id"])
        modelo.agregarApuntador(catalogo, ID, elemento)

def cargar_actores(catalogo, actores):

    """
    Carga datos de peliculas al catalogo bajo la lista de actores
    Crea apuntador que relaciona ID con datos de actores
    """"

    archivo=load_actores(actores)
    for i in range(1,lt.size(archivo)):
        elemento=lt.getElement(archivo,i)
        modelo.agregar_actores(catalogo, elemento)
        ID=int(elemento["id"])
        modelo.agregarApuntador(catalogo, ID, elemento)

def cargar_actores_1(catalogo, actores):
    """
    Carga actor al catalogo
    """
    archivo= load_actores(actores)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombre_actor= linea["actor1_name;"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")

def cargar_actores_2(catalogo, actores):
    """
    Carga actor al catalogo
    """
    archivo= load_actores(actores)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombre_actor= linea["actor2_name;"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")


def cargar_actores_3(catalogo, actores):
    """
    Carga actor al catalogo
    """
    archivo= load_actores(actores)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombre_actor= linea["actor3_name;"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")

def cargar_actores_4(catalogo, actores):
    """
    Carga actor al catalogo
    """
    archivo= load_actores(actores)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombre_actor= linea["actor4_name;"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")


def cargar_actores_5(catalogo, actores):
    """
    Carga actor al catalogo
    """
    archivo= load_actores(actores)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombre_actor= linea["actor5_name;"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")

#consultas

def obtener_peliculas_x_actor(catalogo, nombre_actor):
    """
    retorna peliculas de un director
    """
    info_actor=modelo.obtener_peliculas_x_actor(catalogo, nombre_actor)
    return info_actor

def promedio_x_actor(catalogo, nombre_actor):
    """
    retorno puntaje promedio de un director
    """

    calificacion =modelo.actor_promedio(catalogo, nombre_actor)
    return calificacion

    