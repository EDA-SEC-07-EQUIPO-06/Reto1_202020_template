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
    catalogo["best count"]= lt.newList('SINGLE_LINKED',compBCount)
    catalogo["vote_average"]= lt.newList('SINGLE_LINKED',compVAverage
    return catalogo


def nueva_entrada_pelicula(ID):

    pelicula={"ID":0, "pelicula":None"votacion":None, "calificacion":None}
    pelicula["ID"]=ID
    pelicula["pelicula"]=lt.newList("SINGLE_LINKED",compIDpelicula)
    pelicula["vote_count"] = lt.newList('SINGLE_LINKED',compBCount) 
    pelicula["vote_average"]= lt.newList('SINGLE_LINKED',compVAverage) 

    return pelicula


def nuevo_actor(nombre):

    actor ={"nombre": "","ref_peliculas":None,"Promedio peliculas ":0.0, "Director con mas colaboraciones: " , ""}
    actor["nombre"]=nombre
    actor["ref_peliculas"]=lt.newList('ARRAY_LIST',compIDpelicula)
    actor["Promedio peliculas "]=lt.newList('ARRAY_LIST',compIDpelicula)
    actor["Director con mas colaboraciones:"]=lt.newList('ARRAY_LIST',compIDpelicula)
    

    return actor

def nuevo_genero(nombre_genero):
    
    genero={"nombre":"", "peliculas":None, "promedio":0,"votacion":None, "calificacion":None}
    genero["nombre"]=nombre_genero
    genero["peliculas"]=lt.newList("SINGLE_LINKED",compGenero)
    genero["vote_count"] = lt.newList('SINGLE_LINKED',compBCount) 
    genero["vote_average"]= lt.newList('SINGLE_LINKED',compVAverage) 


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


def obtener_peeliculas_x_actor(catalogo, nombreActor):
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








#requerimientos 





def ranking_peliculas(catalogo,peliculas)-> list:
    respuesta1=[]
    best_count=[]
    worts_average=[]
    respuesta1.append("BEST COUNT : ",best_count,
    ,"---","5 WORST AVERAGE : ",worts_average)
    lista_f={}
    filas= len(catalogo["peliculas"])
    columnas=0
    
    if filas>0:
        columnas=len(catalogo["peliculas"])
        
    for i in range(filas):
        for j in range(columnas): 


          dic= {}
          nombre= peliculas["nombres"]
        
          dic[nombre] =  pelicula["vote_count"]
          v=list(dic.values())
          k=list(dic.keys())
          r_bc= insertionsort(k)
          best_count.append( dic )

          
    
    for i in range(filas):
        for j in range(columnas): 


          dic= {}
          nombre= peliculas["nombres"]
        
          dic[nombre] =  pelicula["vote_average"]
          v=list(dic.values())
          k=list(dic.keys())
          r_wa= insertionsort(k)
          best_count.append( dic )
          worts_average.append( dic )

    #falta ordenar los resultados de mayor a menor
    respuesta2 = {}
    respuesta2["BEST COUNT"] =r_bc
    respuesta2["vote_average"] =r_wa


 
    return "ordenados", respuesta2  ,"sin ordenar --> " , respuesta1


def conocer_actor(catalogo,actores, peliculas,nombreActor):

    resultados= {}

    filas= len(catalogo["actores"])
    columnas=0
    
    if filas>0:
        columnas=len(catalogo["actores"])
        
    for i in range(filas):
        for j in range(columnas): 
             
             lista_peliculas_x_actor= []
             lista_peliculas_x_actor.append(obtener_peeliculas_x_actor(catalogo , nombreActor))
             resultados["peliculas en las que participo"] = lista_peliculas_x_actor
             resultados["Numero de peliculas que participo"] = len(lista_peliculas_x_actor)
             resultados["Promedio de sus peliculas"] = promedio_actor(catalogo, nombreActor)
             resultados["director con mas colaboraciones"] = actor["Director con mas colaboraciones"]

    return resultados   




def ranking_genero(catalogo,peliculas)-> list:
    respuesta1=[]
    best_count=[]
    worts_average=[]
    respuesta1.append("BEST COUNT : ",best_count,
    ,"---","5 WORST AVERAGE : ",worts_average)
    lista_f={}
    filas= len(catalogo["generos"])
    columnas=0
    
    if filas>0:
        columnas=len(catalogo["generos"])
        
    for i in range(filas):
        for j in range(columnas): 


          dic= {}
          nombre= genero["nombre"]
        
          dic[nombre] =  genero["vote_count"]
          v=list(dic.values())
          k=list(dic.keys())
          r_bc= insertionsort(k)
          best_count.append( dic )

          
    
    for i in range(filas):
        for j in range(columnas): 


          dic= {}
          nombre= genero["nombre"]
        
          dic[nombre] =  genero["vote_average"]
          v=list(dic.values())
          k=list(dic.keys())
          r_wa= insertionsort(k)
          best_count.append( dic )
          worts_average.append( dic )

    #falta ordenar los resultados de mayor a menor
    respuesta2 = {}
    respuesta2["BEST COUNT"] =r_bc
    respuesta2["vote_average"] =r_wa


 
    return "ordenados", respuesta2  ,"sin ordenar --> " , respuesta1



    

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

def compBCount(voto1,voto2):
    if (voto1 == voto2):
        return 0
    elif voto1 > voto2:
        return 1
    else:
        return -1
