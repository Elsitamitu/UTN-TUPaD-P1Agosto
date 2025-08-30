#EJERCICIO1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#Ejercicio 1
edad_usuario= int(input("Ingrese su edad: ")) #se solicita al usuario su edad y se almacena la variable
if edad_usuario >=18: #se evalua la condicion
    print("Es usted mayor de edad") #imprimira el mensaje si cumple con la condicion
print("gracias") #saludara en cualquier caso

#####################################################################################
#EJERCICIO2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.
nota_usuario=float(input("Ingrese por favor su nota :")) #se solicita al usuario que ingrese la calificacion y se almacena la variable
if nota_usuario >= 6: #se evalua la condicion
    print("Aprobado") 
else:
    print("Desaprobado") 
print("Gracias")

####################################################################################
#EJERCICIO3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.
numero_usuario=int(input("Ingrese un numero par :")) #se solicita al usuario un numero par y se almacena la varible
if numero_usuario % 2==0: #se evalua la condicion de paridad
    print("Ha ingresado un numero par") 
else:
    print("Por favor ingrese un numero par") 
print("Gracias")

###################################################################################
#EJERCICIO4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.
edad_usuario=int(input("Ingrese su edad :")) #se solicita al usuario edad y se guarda en la variable
if edad_usuario <12: #se evalua la condicion
    print("Usted pertenece a la categoria niño") 
elif edad_usuario>=12 and edad_usuario<18: 
    print("usted pertenece a la categoria adolescente")
elif edad_usuario>=18 and edad_usuario<30: 
    print("Usted pertenece a la categoria adulto/joven")
else: 
    print("usted pertenece a la categoria adulto") 
print("Gracias")

####################################################################################
#EJERCICIO5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.
contraseña=input("Ingrese una contraseña de entre 8 y 14 caracteres :") #se solicita al usuario y se guarda en la variable contrseña
longitud=len(contraseña) #se calcula la longitud del strigs
if longitud>=8 and longitud<=14: # se evalua la condicion
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")
print("Gracias")

###################################################################################
#EJERCICIO6
# escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random  #importa a python esa funcion

numeros_aleatorios=[random.randint(1,100)for i in range(50)] #crea 50 numeros aleatorios entre 1 y 100
print (numeros_aleatorios ) #imprime los numeros generados aleatoriamente
from statistics import mode,median,mean #importa las tres funciones estadisticas
media= mean (numeros_aleatorios) #calcula la media
moda= mode (numeros_aleatorios) #calcula la moda
mediana= median(numeros_aleatorios) #calcula la mediana
print("La media es: ",media,"la moda es :",moda,"la mediana es :",mediana) #imprime por pantallala media,moda y mediana
if mediana>moda and mediana<media: #evalua condicion para determinar sesgo e imprime el resultado
    print("Hay sesgo positivo a la derecha")
elif mediana>media and mediana<moda:
    print("Hay sesgo negativo a la izquierda")
elif media==mediana and mediana==moda:
    print("Sin sesgo")
else:
    print("No es posible calcular el sesgo ")
print("Gracias")

###################################################################################
#EJERCICIO7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 
palabra=input("ingrese una palabra :") #se solicita al usuario ingresar una palabra y la almacena en la variable
vocales=("a","A","e","E","i","I","o","O","u","U") #se definen las vocales
if palabra.endswith(vocales): #se evalua la condicion y con endswith se determina si la palabra termina en vocal
    print(f"La palabra es :{palabra}!") #si la condicion es verdadera se le agrega al final de la palabra un signo de exclamacion
else:
    print(palabra) #caso contrario se imprime solo la palabra
print("Gracias)")

#########################################################################################
#EJERCICIO8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre=input("Ingrese su nombre :" ) #se solicita al usuario su nombre y se almacena en la variable
opcion=int(input("Ingrese 1 si quiere su nombre en mayusculas,2 si quiere minusculas o 3 si quiere solo la primer letra en mayusculas :")) #el usuario debe ingresar un numero opcion
texto_en_mayusculas=nombre.upper() #convierte el nombre en mayuscula
texto_en_minuscula=nombre.lower() #convierte en minuscula
texto_normal=nombre.title() #solo la primer letra mayuscula
if opcion==1: #analiza la condicion,opcion que ha ingresado el usuario
    print(f"Tu nombre es :",texto_en_mayusculas)
elif opcion==2:
    print(f"Tu nombre es :",texto_en_minuscula)
elif opcion==3:
    print(f"Tu nombre es :",texto_normal)
else:
    print("Usted ha ingresado un numero no valido como opcion") #en el caso que el usuario ingrese una opcion no valida
print("Gracias")

###############################################################################
#EJERCICIO9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
magnitud=float(input("Ingrese la magnitud del terremoto :"))  #ingreso de la variable
if magnitud<3: # cada una de las condiciones para poder determinar la magnitud del terremoto
    print("EL Terremoto es MUY LEVE")
elif 3<=magnitud<4:
    print("El Terremoto es LEVE")
elif 4<=magnitud<5:
    print("El Terremoto es MODERADO")
elif 5<=magnitud<6:
    print("El Terremoto es FUERTE ")
elif 6<=magnitud<7:
    print("El Terremoto es MUY FUERTE ")
else:
    print("El Terremoto es EXTREMO")

#############################################################################
#EJERCICIO10
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio_usuario=input("En que hemisferio te encuentras?_norte o sur: ")
mes_usuario=input("En que mes estamos?(enero,febrero,etc); ")
dia_usuario=int(input("Que dia es hoy? :"))
def determinar_estacion(hemisferio, mes, dia):
    mes=mes.lower()
    if hemisferio.lower() =='norte':    
        if mes in ['marzo']:
            if dia>=21:
                return'Primavera'
            else:
                return'Invierno'
        elif mes in ['abril','mayo']:
            return'Primavera'
        elif mes in ['junio']:
            if dia>=21:
                return'Verano'
            else:
                return'Primavera'
        elif mes in ['julio','agosto']:
            return'Verano'
        elif mes in ['septiembre']:
            if dia>=21:
                return'Otoño'
            else:
                return'Verano'
        elif mes in ['octubre','noviembre']:
            return'Otoño'
        elif mes in ['diciembre']:
            if dia >=21:
                return'Invierno'
            else:
                return'Otoño'
        elif mes in ['enero','febrero']:
            return'Invierno'
        else:
            return'Mes Invalido'
    elif hemisferio =='sur':
        if mes in ['marzo']:
            if dia>=21:
                return'Otoño'
            else:
                return'Verano'
        elif mes in ['abril','mayo']:
            return'Otoño'
        elif mes in  'junio':
            if dia>=21:
                return'Invierno'
            else:
                return'Otoño'
        elif mes in ['julio','agosto']:
            return'Invierno'
        elif mes in ['septiembre']:
            if dia>=21:
                return'Primavera'
            else:
                return'Invierno'
        elif mes in ['octubre','noviembre']:
            return'Primavera'
        elif mes in ['diciembre']:
            if dia >=21:
                return'Verano'
            else:
                return'Primavera'
        elif mes in ['enero','febrero']:
            return'Verano'
        else:
            return'Mes Invalido'
    else:
        return'Hemisferio Invalido'
estacion= determinar_estacion(hemisferio_usuario, mes_usuario, dia_usuario)
print(f"\nEn el hemisferio {hemisferio_usuario} durante el mes de {mes_usuario} y el dia {dia_usuario}, la estacion es :{estacion}")

################################################################################
