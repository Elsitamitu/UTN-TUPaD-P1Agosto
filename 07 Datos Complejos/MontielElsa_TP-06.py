#Ejercicio1
#Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas={'Banana':1200, 'Anana':2500,'Melon':300, 'Uva': 1450}
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300
print(precios_frutas)

print("###################################################")
#Ejercicio2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800
print(precios_frutas)

print("#############################################################")
#Ejercicio3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.
lista_claves=list(precios_frutas.keys())
print(lista_claves)

print("###########################################################")
#Ejercicio4
# Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
#Ejemplo:
#contactos={'Juan':123456, 'Ana':987654}
#consultar:'Juan'->muestra'123456'
contactos={}   #diccionario vacio
num_contactos=5   #cantidad de contactos permitidos
for i in range(num_contactos):   #Bucle para la carga de los 5 nombres
    while True:    #Bucle para ingresar cada uno y eliminar espacios
        nombre_usuario=input(f"[{i+1}/{num_contactos}] Ingrese el nombre: ").strip()
        if nombre_usuario:     #validar para que no ingrese vacio y conversión a minúscula
            nombre=nombre_usuario.lower()
            break
        else:
            print("Error el nombre no puede estar vacio")
    numero=input(f"Ingrese el numero de telefono para {nombre_usuario.title()}:").strip()
    contactos[nombre]=numero
    print("-"*20)      #para mejor visualizacion

print(f"Contactos cargados: {contactos}")

while True:    #Consulta de contactos
    nombre_a_consultar=input("Ingresa el nombre del contacto para conocer su número o 'salir'para terminar :").strip()
    if nombre_a_consultar.lower()=='salir':
        print("Gracias por usar la agenda")
        break
    if not nombre_a_consultar:  #validacion espacio en blanco
        print("Error..La consulta no puede estar vacía")
        continue
    nombre_busqueda=nombre_a_consultar.lower()  #convertimos consulta a minúscula 
    if nombre_busqueda in contactos:     #Verificamos si existe
        numero_encontrado=contactos[nombre_busqueda]
        print(f"El numero de telefono de {nombre_busqueda} es: {numero_encontrado}")
    else:
        print(f"Lo siento ese contacto {nombre_busqueda} no esta en tu agenda")

print("#################################################################")

#Ejercicio5
#) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 

def procesar_frase():
    frase=input("Por favor ingresa una frase: ").strip()
    frase_minuscula=frase.lower()

    if not frase:
        print("Error la frase no puede estar vacia")
        return
    
    caracteres_a_eliminar=[',','.',';',':','?','¿','¡','!']
    frase_limpia=frase_minuscula

    for caracter in caracteres_a_eliminar:
        frase_limpia=frase_limpia.replace(caracter,' ')  #reemplaza los signos por espacios en blanco

    palabras=frase_limpia.split()
    return palabras

def contar_palabras(lista_palabras):
    contador_palabras={}
    for palabra in lista_palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra]+=1
        else:
            contador_palabras[palabra]=1
    
    return contador_palabras

def funcion_final():
    lista_de_palabras=procesar_frase()  #obtiene la lista de palabras limpia
    frecuencia_palabras=contar_palabras(lista_de_palabras)
    palabras_unicas=set(lista_de_palabras)    #crea el set
    conteo_total=len(lista_de_palabras)   #calcula la longitud
    conteo_unico=len(palabras_unicas)

    print(f"La frase original tiene {conteo_total} palabras")
    print(f"Numero de palabras unicas :{conteo_unico}")
    print("las palabras unicas son")
    print(palabras_unicas)
    print("Direccionario de frecuencias de palabras :")
    print(frecuencia_palabras)

funcion_final()

print("###############################################################")
#Ejercicio6)
#Permiti ingresar los nombres de 3 alumnos y para cada uno una tupla de 3 notas.
#Luego mostra el promedio de cada uno
import re

def valido_numero(entrada_usuario):
    if ' ' in entrada_usuario or ',' in entrada_usuario:
        print("Error,no se permiten espacios en blanco,ni comas en las notas")
        return False
    if entrada_usuario.count('.') > 1:
        print("Error no se permite mas de un punto")
        return False
    if not entrada_usuario or entrada_usuario=='.':
        print("Error la entrada no puede estar vacia o solo un punto decimal")
        return False
    if not re.match(r'^\d*\.?\d+$', entrada_usuario):
        print("Error, la entrada no es un numero valido")
        return False
    return True

def calcular_promedio (notas):
    return sum(notas)/len(notas)

def ingresar_notas_y_promedio():
    estudiantes={}
    num_estudiantes=3
    num_notas=3
    for i in range(num_estudiantes):
        nombre=input("Ingrese el nombre del estudiante :").strip()
        lista_de_notas=[]
        while len(lista_de_notas)<num_notas:
            print(f"Ingrese la nota {len(lista_de_notas)+1} :")
            
            while True:
                entrada_nota=input(" nota: ").strip()
                if valido_numero(entrada_nota):
                    nota_float=float(entrada_nota)
                    lista_de_notas.append(nota_float)
                break
        
        notas_tupla=tuple(lista_de_notas)
        estudiantes[nombre]=notas_tupla

    print("Diccionario de estudiantes y notas")
    print(estudiantes)
    for nombre, notas in estudiantes.items():
        promedio=calcular_promedio(notas)
        print(f"Notas:{{'{nombre}': {notas}}}")
        print(f"Promedio:**{promedio}**")

ingresar_notas_y_promedio()

print("###########################################################")
#Ejercicio7)
#Dados 2 sets de numeros, representando 2 listas de estudiantes que aprobaron Parcial 1
# y Parcial 2
#Mostra los que aprobaron ambos parciales
#mostra los que aprobaron solo uno de los dos
#Mostra la lista total de estudiantes que aprobaron al menos 1 parcial
aprobado_parcial1={301,305,312,315,320,330}
aprobado_parcial2={305,312,325,330,340,350}
print(f"Parcial 1:{aprobado_parcial1}")
print(f"Parcial 2:{aprobado_parcial2}")

#Interseccion(aprobaron ambos)
ambos_parciales=aprobado_parcial1.intersection(aprobado_parcial2)
print(f"Aprobaron ambos:{ambos_parciales}")

#Diferencia simetrica(solo uno de los dos)
solo_uno=aprobado_parcial1^aprobado_parcial2
print(f"Aprobaron solo uno:{solo_uno}")

#Al menos un parcial es union
al_menos_uno=aprobado_parcial1.union(aprobado_parcial2)
print(f"Aprobaron al menos uno:{al_menos_uno}")

print("###########################################################")
#Ejercicio 8)
#Arma un diccionario donde las claves sean nombres de productos y los
#valores su stock
#Permiti al usuario:
#Consultar el stock de un producto ingresado, agregar unidades al stock 
#si el producto ya existe y agregar un nuevo producto si no existe
def numero_entero_positivo(entrada):
    if entrada.strip().isdigit():
        return int(entrada)>0
    return False

def inventario():
    productos={'leche':20,'queso':12}  #diccionario inicial
    while True:
        print("Inventario actual:",productos)
        print("Seleccione una opcion valida")
        print("Consultar stock de un producto:A")
        print("Agregar unidades a un producto o crear un artículo nuevo:B")
        print("o Presione S para salir del programa")
        opcion=input("Opcion: ").upper().strip()  
        if opcion=='A':
            nombre_producto=input("Ingrese el nombre del producto a consultar: ").lower().strip()
            stock_actual=productos.get(nombre_producto)
            if stock_actual is not None:
                print(f"El stock de '{nombre_producto}'es: {stock_actual}")
            else:
                print("Error el producto no existe en el inventario")
        elif opcion=='B':
            nombre_producto=input("Ingrese el nombre del producto : ").lower().strip()
            while True:
                entrada_unidades=input("Ingrese la cantidad a agregar: ").strip()
                if numero_entero_positivo(entrada_unidades):
                    unidades_a_agregar=int(entrada_unidades)
                    break
                else:
                    print("Por favor ingrese un entero positivo")
            if nombre_producto in productos:
                productos[nombre_producto]+=unidades_a_agregar
                print(f"El stock de '{nombre_producto}'es :{productos[nombre_producto]}")
            else:
                productos[nombre_producto]=unidades_a_agregar
                print(f"El producto '{nombre_producto}' agregado al inventario con: {unidades_a_agregar} unidades ")
        elif opcion=='S':
            print("Hasta luego")
            break
        else:
            print(f"Opcion ('{opcion}')No es valida")

inventario()

print("#########################################################")
#Ejercicio9)
#crea una agenda donde las claves sean tuplas de (dia,hora) y los
#valores sean eventos
#Permiti consultar qué actividad hay en cierto dia y hora
def crear_agenda():
    agenda={("lunes","10:00"):"Revisar agenda semanal",("lunes","12:00"):"Llamar a clientes",("martes","09:00"):"Enviar los formularios"}
    return agenda

def consultar_agenda(agenda):
    dia_consulta=input("Ingrese el dia a consultar :").lower().strip()
    hora_consulta=input("Ingrese la hora que desea consultar (Ej. 10:30): ").strip()
    busca_clave=(dia_consulta,hora_consulta)
    actividad_encontrada=agenda.get(busca_clave)   #busca la clave de la tupla
    if actividad_encontrada:
        print(f"Actidad encontada para el dia :{dia_consulta} es :{actividad_encontrada}")
    else:
        print(f"No hay actidades para el dia :{dia_consulta} en la hora :{hora_consulta}")

def prog_principal():
    mi_agenda=crear_agenda()
    print("Agenda:",mi_agenda)
    consultar_agenda(mi_agenda)

prog_principal()

print("###########################################################")
#Ejercicio10)
#Dado un diccionario que mapea nombres de paises con sus capitales,
#construi un nuevo diccionario donde:
#las capitales sean las claves y los paises los valores
paises_y_capitales={"Argentina":"Buenos Aires","Uruguay":"Montevideo","Chile":"Santiago de Chile"}
print(f"Diccionario original :{paises_y_capitales}")
capitales_y_paises={}
for pais, capital in paises_y_capitales.items():  #asignar la capital como clave y el pais como valor
    capitales_y_paises[capital]=pais
print(f"Diccionario Invertido : {capitales_y_paises}")

print("#####################################################")























