# Ejercicio1:Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja. 

#Crea una lista vacía
notas=[2,3,5,6,7,3,6,9,3,8]
print(f"\nLista de notas: {notas}")  #muestra la lista
promedio=sum(notas)/len(notas)   #calcula el promedio
print(f"El promedio es: {promedio}")  #lo muestra
nota_Max=max(notas)   #busca la nota máxima
nota_Min=min(notas)   #busca la nota mínima
print(f"La nota más alta es : {nota_Max}")   #imprime cada una de ellas
print(f"La nota más baja es : {nota_Min}")

#####################################################################################################
#Ejercicio 2
#Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
productos=[]   #lista vacía
for i in range(5):   #ciclo para que el usuario ingrese los productos
    producto=input(f"Ingresa el nombre del producto :")
    productos.append(producto)     #los suma a la lista de productos
print(productos)

#Para ordenar la lista alfabéticamente
productos.sort()
print(f"La lista ordenada de productos es: {productos}")
#Opción eliminar elementos de la lista
opcion_elim=input("Desea eliminar algun producto si/no : ").lower()
if opcion_elim=="si" or opcion_elim=="sí":
    remover=input("Ingresa el elemento que deseas eliminar: ")
    if remover in productos:  #verifica si el producto pertenece a la lista
        productos.remove(remover)    #lo elimina y luego vuelve a mostrar la nueva lista
        print(f"{remover} ha sido eliminado de la lista")
        print(f"La nueva lista es: {productos}")
    else:
        print(f"El elemento {remover} no se encontró en la lista")
else:
    print("Gracias por su compra")

#######################################################################################################

#Ejercicio3
# Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista. 
import random 
lista=[random.randint(1,100) for i in range(15)]  #crear lista con numeros enteros aleatorios
print(f"La lista original es: {lista}")
#lista par y lista impar
pares=[]
impares=[]
for num in lista:
    if num %2 == 0:   #para verificar paridad
        pares.append(num)
    else:
        impares.append(num)
#Para imprimir y verificar la cantidad de elementos de cada una de las listas
print(f"La lista de numeros pares tiene {len(pares)} elementos")
print(pares)
print(f"La lista de numeros impares tiene {len(impares)} elementos")
print(impares)

###########################################################################################
#Ejercicio4
# Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.
datos=[1,3,5,3,7,1,9,5,3]
print(f"La lista original es :{datos}")
#nueva lista sin valores duplicados
nuevos_datos=list(set(datos))
print(f"Mi nueva lista es :{nuevos_datos}")

############################################################################################
#Ejercicio5
# Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 
presentes=["Elba","Fabio","Eliana","Marcelo","Juan","Pedro","Vero","Tatiana"]
print(f"La lista de presentes es: {presentes}")

#Para preguntar qué desea hacer
hacer=input("Seleccione la opción adecuada agregar o quitar: ")
if hacer=="agregar":
    alumno=input("Ingresa su nombre :")
    presentes.append(alumno)
elif hacer=="quitar":
    alumno=input("Ingresa su nombre :")
    if alumno in presentes:    #para corroborar que el nombre exista
        presentes.remove(alumno)
    else:
        print("El nombre no se encuentra en su lista")
    print("La lista modificada es :",presentes) #mostrar lista modificada
else:
    print("Usted no selecciono la opcion adecuadamente")

########################################################################################
#Ejercicio6
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 
lista_num=[1,2,3,4,5,6,7]
print("La lista de los numeros es :",lista_num)
#Para extraer el último elemento
extraer_ultimo=lista_num.pop()
#Para colocarlo al inicio
lista_num.insert(0,extraer_ultimo)
print("La lista rotada es:",lista_num)

################################################################################################
#Ejercicio7
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.
temp_de_semana=[[5,11],[3,9],[5,10],[-3,8],[1,7],[6,13],[3,9]]
print(temp_de_semana)
#Cálculo del promedio de cada una de las columnas
suma_prim_element=0   #inicializacion de los contadores
suma_seg_element=0
for fila in temp_de_semana:
    suma_prim_element+=fila[0]   #suma el primer elemento de cada fila
    suma_seg_element+=fila[1]    #suma los segundos elementos

#calculo de la cantidad de elementos y el promedio
promedio_prim=suma_prim_element/len(temp_de_semana)
promedio_seg=suma_seg_element/len(temp_de_semana)

dif_maxima=0  #inicializacion de la variable
fila_maxima_dif=0    #para guardar la posición de la fila
for i, fila in enumerate(temp_de_semana):
    diferencia=fila[1]-fila[0]  #calcula la diferencia entre ambas filas
    if diferencia>dif_maxima:   #condicion para hallar el minimo valor
        dif_maxima=diferencia
        fila_maxima_dif=i  #guarda el índice de la fila

print(f"El promedio de las temperaturas minimas es :{promedio_prim}")
print(f"El promedio de las temperaturas maximas es :{promedio_seg}")
print(f"El valor de la amplitud máxima es :{dif_maxima}°C")
print(f"Y se encuentra en el dia : {temp_de_semana[fila_maxima_dif]}")

##########################################################################################3
#Ejercicio8
#Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

# Notas de materias #materia1:"Matematica",#materia2:"CalculoI",3materia3:"Ingles"
notas=[[8,9,7],[6,5,9],[4,7,8],[2,4,6],[6,7,9]]   #1:Juan,#2:Pedro,#3:Clara, #4:Andres y #5:Martin

#Calculo del promedio de cada estudiante
promedio_estud=[]
print("Promedio de cada estudiante :")
for i, notas_de_estudiante in enumerate(notas):   
    promedio=sum(notas_de_estudiante)/len(notas_de_estudiante)
    promedio_estud.append(promedio)
    print(f"El estudiante {i+1} tiene de promedio: {promedio:.2f}")

#Calculo de promedio de cada materia
print("\nPromedio de cada materia")
num_materia=len(notas[0])  #calcula cuantas notas tiene cada estudiante
num_estudiante=len(notas)   #calcula cantidad de estudiantes
for j in range(num_materia):
    suma_materia=sum(notas[i][j] for i in range(num_materia))
    promedio_materia=suma_materia/num_estudiante
    print(f"Materia {j+1}:{promedio_materia:.2f}")

################################################################################################
#Ejercicio9
#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada.

tablero=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
jugador_actual='x'
ganador=False
movimientos=0

#Bucle para jugar
while movimientos<9 and not ganador:
    print("Tablero actual:")
    print(" 0 1 2")
    print("0" +tablero[0][0]+"|"+tablero[0][1]+"|"+tablero[0][2])
    print("1"+tablero[1][0]+"|"+tablero[1][1]+"|"+tablero[1][2])
    print("2"+tablero[2][0]+"|"+tablero[2][1]+"|"+tablero[2][2])
    entrada_valida=False   #Solicitar la jugada al jugador y validar
    while not entrada_valida:
        print(f"\nTurno de {jugador_actual}.Ingresa tu jugada (fila,columna): ")
        entrada=input().split(',')
        if len(entrada)==2 and entrada[0].strip().isdigit() and entrada[1].strip().isdigit():
            fila=int(entrada[0].strip())
            columna=int(entrada[1].strip())
            if 0<=fila<=3 and 0<=columna<=3 and tablero[fila][columna]==' ':
                tablero[fila][columna]=jugador_actual
                entrada_valida=True
            else:
                print("Movimiento incorrecto.La casilla esta ocupada o las coordenadas no son validas")
        else :
            print("Entrada incorrecta,usa el formato ej.1,1")
        movimientos +=1    #incrementa el contador
        if (tablero[0][0]==tablero[0][1]==tablero[0][2]!=' ' or tablero[1][0]==tablero[1][1]==tablero[1][2]!=' 'or  tablero[2][0]==tablero[2][1]==tablero[2][2]!=' ') :
            ganador=True
        elif (tablero[0][0]==tablero[1][0]==tablero[2][0]!=' ' or tablero[0][1]==tablero[1][1]==tablero[2][1]!=' ' or tablero[0][2]==tablero[1][2]==tablero[2][2]!=' ' ):
            ganador=True
        elif (tablero[0][0]==tablero[1][1]==tablero[2][2]!=' '):
            ganador=True
        if not ganador:  #cambiar el turno si no hay ganador
            if jugador_actual=='x':
                jugador_actual='0'
            else:
                jugador_actual ='x'                   
print("\n---juego terminado---")
print(" 0 1 2")  #imprime tablero final y resultado
print("0"+tablero[0][0]+"|"+tablero[0][1]+"|"+tablero[0][2])
print("1"+tablero[1][0]+"|"+tablero[1][1]+"|"+tablero[1][2])
print("2"+tablero[2][0]+"|"+tablero[2][1]+"|"+tablero[2][2])
if ganador:
    print(f"\n ¡Felicidades, el jugador {jugador_actual} ha ganado!")
else:
    print("\n ¡Es empate!")

##################################################################################################
#Ejercicio10
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.

#Matriz de ventas donde las filas son los productos y las columnas los días
ventas=[[7,7,7,7,7,7,7],[2,2,2,2,2,2,2],[3,2,3,2,3,2,3],[4,5,5,6,6,7,7]]
total_de_productos=[0,0,0,0] #inicialización de la matriz total de productos en cero
fila=0
while fila<4:
    columna=0
    while columna<7:
        total_de_productos[fila]+=ventas[fila][columna]
        columna+=1
    fila+=1
print("---Total de ventas de cada producto---") #muestra el total de ventas de cada producto
print(f"Producto1:{total_de_productos[0]}")
print(f"Producto2:{total_de_productos[1]}")
print(f"Producto3:{total_de_productos[2]}")
print(f"Producto4:{total_de_productos[3]}")
#Día con mayor venta
totales_dias=[0,0,0,0,0,0,0]  #inicialización de la matriz para día con mayor venta
columna=0
while columna<7:
    fila=0
    while fila<4:
        totales_dias[columna]+=ventas[fila][columna]
        fila+=1
    columna+=1

dia_mayor_venta=0
max_venta=-1
dia_actual=0
while dia_actual<7:
    if totales_dias[dia_actual]>max_venta:
        max_venta=totales_dias[dia_actual]
        dia_mayor_venta=dia_actual+1
    dia_actual+=1

print("\n---Días con mayores ventas totales---")
print(f"El día con mayores ventas totales es {dia_mayor_venta} con {max_venta} unidades")
#Producto más vendido de la semana
producto_mas_vendido=0
max_venta_producto=-1
producto_actual=0
while producto_actual<4:
    if total_de_productos[producto_actual]>max_venta_producto:
        max_venta_producto=total_de_productos[producto_actual]
        producto_mas_vendido=producto_actual+1
    producto_actual+=1

print("\n---Producto más vendido de la semana---")
print(f"El producto más vendido de la semana es el producto {producto_mas_vendido} con un total de {max_venta_producto} unidades")

