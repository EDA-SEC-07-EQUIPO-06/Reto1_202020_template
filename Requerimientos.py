import operator

def crear_ranking (list):
    cantidad=int(input("�De cuantas peliculas desea hacer el ranking?"))
    if cantidad >= 10 : 
       peliculas=[]
       for i in range (0,cantidad) :
           nombre=input("Ingrese el nombre de la pelicula numero "+ str(i))
           if nombre not in peliculas:
               peliculas.append(nombre)
           else: 
                print("Ya menciono esa pelicula.")
    else: 
         print("El ranking tiene que ser de minino 10 peliculas")
    
    criterio=input("Si quiere hacer el ranking de acuerdo a la votacion escriba True y si lo quiere hacer de acuerdo al promedio escriba False.") 
    if criterio == "True": 
       ranking={}
       for i in range(0,len(list[0])):
           posicion=list[0][i]
           if posicion=="vote_count":
              for j in range(0,len(list)):
                  nombre=list[j][6]
                  if nombre in peliculas: 
                     votos=int(list[j][i])
                     ranking[nombre]=votos 
    if criterio == "False":  
       ranking={}
       for i in range(0,len(list[0])):
           posicion=list[0][i]
           if posicion=="vote_average":
              for j in range(0,len(list)):
                  nombre=list[j][6]
                  if nombre in peliculas: 
                     average=int(list[j][i])
                     ranking[nombre]=average
    else:
         print("Ingrese una forma de criterio correcta")
    
    orden=input("Si quiere ordenar el ranking de forma descendente escriba True y si lo quiere ordenar de forma ascendente escriba False.")
    if orden=="True":
       ranking_valores=sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)
    if orden=="False":
       ranking_valores=sorted(ranking.items(), key=operator.itemgetter(1), reverse=False) 
    else: 
         print("Ingrese una forma de orden correcta")

    for name in enumerate(ranking_valores):
        print(name[1][0], ':', ranking[name[1][0]])



def conocer_un_director(list_casting,list_movies):
    nombre=input("Ingrese el nombre del director que desea buscar:")
    ids=[]
    for i in range(0,len(list_casting[0])):
        posicion=list_casting[0][i]
        if posicion=="director_name":
           for j in range (0,len(list_casting)):
               nombre_dir=list_casting[j][i]
               if nombre_dir==nombre:
                  id=list_cansting[j][0]
                  if id not in ids:
                     ids.append(id)
    peliculas={}
    if len(ids) > 0:     
       for id in ids:
           for j in range(0,len(list_movies)):
               id_movie=list_movies[j][0]
               if id == id_movie:
                  titulo=list_movies[0][6]
                  promedio=list_movies[0][18]
                  peliculas[titulo]=promedio
    else: 
         print("No se hallaron registros del director que busca.")
  
    print("El director que busca ha dirigido "+ str(len(ids)) +"peliculas y son las siguientes:")
    return (peliculas)




          





def crear_ranking_genero(list):    
    cantidad=int(input("�De cuantas peliculas desea hacer el ranking?"))
    genero=input("Ingrese el genero de las peliculas")
    if cantidad >= 10 : 
       peliculas=[]
       for i in range (0,cantidad) : 
           nombre=input("Ingrese el nombre de la pelicula n�mero "+ str(i))
           for i in range(0,len(list[0])):
                 posicion=list[0][i]
                 if posicion=="genres":
                     for j in range(0,len(list)):
                         nombre_list=list[j][6] 
                         if nombre_list==nombre:
                            genero_lista=list[j][i]
                            if genero in genero_lista: 
                               if nombre not in peliculas:
                                  peliculas.append(nombre)
                               else: 
                                    print("Ya menciono esa pelicula.")
                         else:
                              print("El genero de esta pelicula no corresponde con el deseado")
    else: 
         print("El ranking tiene que ser de minino 10 peliculas")


    criterio=input("Si quiere hacer el ranking de acuerdo a la votacion escriba True y si lo quiere hacer de acuerdo al promedio escriba False.") 
    if criterio == "True": 
       ranking={}
       for i in range(0,len(list[0])):
           posicion=list[0][i]
           if posicion=="vote_count":
              for j in range(0,len(list)):
                  nombre=list[j][6]
                  if nombre in peliculas: 
                     votos=int(list[j][i])
                     ranking[nombre]=votos 
    if criterio == "False":  
       ranking={}
       for i in range(0,len(list[0])):
           posicion=list[0][i]
           if posicion=="vote_average":
              for j in range(0,len(list)):
                  nombre=list[j][6]
                  if nombre in peliculas: 
                     average=int(list[j][i])
                     ranking[nombre]=average
    else:
         print("Ingrese una forma de criterio correcta")
    
    orden=input("Si quiere ordenar el ranking de forma descendente escriba True y si lo quiere ordenar de forma ascendente escriba False.")
    if orden=="True":
       ranking_valores=sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)
    if orden=="False":
       ranking_valores=sorted(ranking.items(), key=operator.itemgetter(1), reverse=False) 
    else: 
         print("Ingrese una forma de orden correcta")

    for name in enumerate(ranking_valores):
        print(name[1][0], ':', ranking[name[1][0]])
   

