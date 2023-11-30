"""Primera parte. Definir función (laberinto).
    Valores de entrada un número entero (medida) para dar la dimensión del laberinto
    y una lista de tuplas (muro) donde están los muros.
    Devuelve la lista de listas que forman el laberinto."""
def laberinto(medida, muro):
    laberinto = []
    #Crea la lista vacía del laberinto
    for i in range(medida):
     #Bucle (for) que añade las filas del laberinto según la (medida) dada.
        fila = []
        #Crea la lista vacía (fila) para añadir las filas del laberinto.
        for j in range(medida):
         #Bucle (for) para seguir las columnas del laberinto.
            if tuple([i, j]) in muros:
             #Condicional (if) para saber si la tupla (i,j) está en la lista (muros).
                fila.append("X")
                #Si está en (muros) escribe una equis ("X").
            else:
                fila.append(" ")
                #Si no está en (muros) escribe un espacio en blanco(" ").
        laberinto.append(fila)
        #Añade la fila al laberinto.
    return laberinto
    #Devuelve la lista de listas del laberinto formado (laberinto).

"""Segunda parte. Definir muros."""
muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
#Escribe las coordenadas con muro en la lista de tuplas (muros).
lado=5
#Variable que indica la dimensión del laberinto 5x5.
lab = laberinto(lado, muros)   
#Llama a la función (laberinto) con medidas 5x5 y con los (muros).
#Luego recoge lista de listas devuelta por la función en la lista (lab).

"""Tercera parte. Imprimir laberinto."""
for i in lab:
 #Recorre la lista (lab).
    print("".join(i))
    #Imprime cada elemento fila de la lista (lab).

"""Cuarta parte. Solucionar laberinto."""

def recorre_laberinto(laberinto):
    '''Función que busca la salida de un laberinto. La entrada es el laberinto definido anteriormente como una matriz cuadrada (lista de listas) 
    que representa el laberinto con el caracter X donde hay un muro.
    Decuelve una lista con los pasos que hay que dar para recorrer el laberinto y salir de él.'''
    # Fila y columnas iniciales
    fila = columna = 0
    # Lista de movimientos
    n=lado
    movimientos = ["Abajo"]
    #Comienza con valor (Abajo) porque la entrada siempre está arriba del laberinto
    while (fila < n-1 and columna < n-1):
        if movimientos[-1] != "Arriba" and fila + 1 < n and laberinto[fila + 1][columna] != "X":
         #En este caso cumple que el movimiento anterior es distinto de (Arriba), 
         # la fila de abajo (fila+1) está dentro de las dimensiones y no tiene muro.
            fila += 1
            #Suma una fila porque hemos bajado.
            movimientos.append("Abajo")
            #Añade el movimiento hacia abajo.
        elif movimientos[-1] != "Abajo" and fila - 1 > 0 and laberinto[fila - 1][columna] != "X":
         #En este caso cumple que el movimiento anterior es distinto de (Abajo), 
         # la fila de arriba (fila-1) está dentro de las dimensiones y no tiene muro.
            fila -= 1
            #Resta una fila porque hemos subido.
            movimientos.append("Arriba")
            #Añade el movimiento hacia arriba.
        elif movimientos[-1] != "Izquierda" and columna + 1 < n and laberinto[fila][columna + 1] != "X":
         #En este caso cumple que el movimiento anterior es distinto de (Izquierda), 
         # la columna de la derecha (columna+1) está dentro de las dimensiones y no tiene muro.
            columna += 1
            #Suma una columna porque hemos pasado a la derecha.
            movimientos.append("Derecha")
            #Añade el movimiento hacia la derecha.
        elif movimientos[-1] != "Derecha" and columna - 1 > 0 and laberinto[fila][columna - 1] != "X":
         #En este caso cumple que el movimiento anterior es distinto de (Derecha), 
         # la columna de la izquierda (columna-1) está dentro de las dimensiones y no tiene muro.
            columna -= 1
            #Resta una columna porque hemos pasado a la izquierda.
            movimientos.append("Izquierda")
            #Añade el movimiento hacia la izquierda.
        else:
            movimientos.append('No hay salida')
            #En caso de que llegue a un punto sin salida.
    return movimientos
    #Devuelve la lista con los movimientos añadimos a través de (append) en los condicionales anteriores.

# Mostrar por pantalla la lista de movimientos
print("La solución para recorrer el laberinto es: ", recorre_laberinto(lab))