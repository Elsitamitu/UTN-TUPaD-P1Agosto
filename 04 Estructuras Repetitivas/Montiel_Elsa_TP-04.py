#Ejercicio1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

valor_inicial=0  #variable inicial
valor_final=101   #variable final
for i in range (valor_inicial,valor_final):  #ciclo para desde valor inicial hasta final para generar los numeros
    print(i)    #muestra los numeros en pantalla

print("/////////////////////////////////////////////////////////////////////////////")

#Ejercicio2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

print("Ingrese un numero entero")   #solicita al usuario que ingrese un entero
num=int(input())      #lo almacena en la variable num
cant_de_digitos=len(str(abs(num)))  #calcula su valor absoluto,lo convierte en un string y calcula su longitud
print("El numero ingresado tiene ",cant_de_digitos,"digitos")   #imprime la cantidad de digitos del numero

print("////////////////////////////////////////////////////////////////////////////")

#Ejercicio3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

suma=0  #inicializacion de la variable suma en cero
print("Ingrese el primer valor :")   #se solicita al usuario el primer numero
primer_valor=int(input())     # se lo almecena en la variable
print("Ingrese el segundo valor :")  #se solicita el segundo numero
segundo_valor=int(input())    # se lo almacena en la variable

inicio=min(primer_valor,segundo_valor)+1   #compara el minimo valor entre ambos y se suma 1 para que no lo incluya
fin=max(primer_valor,segundo_valor)   #compara el maximo valor entre ambos

for numero in range(inicio,fin):   # comienza el ciclo entre ambos valores
    suma=suma+numero    #calcula la suma entre los valores ingresados
    
print(f"La suma de los numeros en el intervalo es:{suma}") #devuelve por pantalla el resultado

print("////////////////////////////////////////////////////////////////////////")

#Ejercicio 4
#  Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

sum=0  #inicializacion del acumulador en cero
while num != 0:   #bucle para que el usuario ingrese los numeros con la condicion solicitada
    print("Ingrese los numeros a sumar, cero para finalizar:")  
    num=int(input())  #variable  que almacena los numeros ingresados
    sum=sum + num      #acumulador suma

print(f"la suma de los numeros ingresados es : ",sum) #imprime en pantalla el resultado

print("///////////////////////////////////////////////////////////////////////////")

#Ejercicio5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  #importa random para crear numeros aleatorios
inicio_rango=0   #comienzo del rango
fin_rango=9    #fin del rango
numero_aleatorio=random.randint(inicio_rango,fin_rango)  #variable que almacena el numero aleatorio

cont=1    #inicializa contador en 1
print(" Adivina el numero!! Ingresa un numero entre 0 y 9 y te dire si has adivinado!!") #solicita que ingrese el numero
num_usuario=int(input())    #almacena el numero en la variable
while num_usuario != numero_aleatorio:  # bucle que permite al usuario seguir intentando adivinar el numero
    print("Intenta nuevamente!!!")
    num_usuario=int(input())
    cont=cont+1    # contador para saber la cantidad de intentos ingresados

print("Has acertado!!,el numero ",numero_aleatorio,"en :",cont,"intentos") #salida por pantalla del numero aleatorio y la cantidad de intentos

print("////////////////////////////////////////////////////////////////////////")

#Ejercicio6:
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for i in range (100,-2,-2): #bucle que permite generar los numeros con la condicion solicitada
    print(i)    #imprime los numeros del 0 al 100 en forma decreciente

print("///////////////////////////////////////////////////////////////////////")

#Ejercicio7:
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

sum=0  #inicializa el acumulador
print("Por favor ingrese el numero hasta el que desea sumar") #solicita al usuario el numero
num_usuario=int(input())  #variable que almacena el  numero

while num_usuario<=0:  #buble de control de numeros enteros positivos
    print("El numero debe ser mayor que cero,ingrese un numero correcto")
    num_usuario=int(input())
for cont in range (0,num_usuario +1): # bucle para realizar la suma de enteros positivos hasta el valor inclusive
    sum=sum+cont
print("La suma es:",sum) #muestra el resultado en pantalla

print("//////////////////////////////////////////////////////////////////////////////")

#Ejercicio8:
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_par=0 #inicializa las variables par,impar,positivo y negativo en cero
num_impar=0
num_positivo=0
num_negativo=0

for i in range (1,5):  #bucle que permite al usuario ingresar los 100 numeros
    print("Ingrese un numero entero")
    num_usuario=int(input()) #variable ingresada por el usuario
    if num_usuario<0:   #condicion para ser negativo
        num_negativo=num_negativo+1 # contador de negativos
        if num_usuario %2==0 :  #condicion que siendo negativo sea par
            num_par=num_par+1  #contador de numeros pares
        else:
            num_impar=num_impar+1  #contador de numeros impares
    elif num_usuario>0:  # condicion para ser positivo
        num_positivo=num_positivo+1  # contador de numeros positivos
        if num_usuario %2==0 :  #condicion que siendo positivo sea par
            num_par=num_par+1   #contador de numeros pares
        else:
            num_impar=num_impar+1  #contador de numeros impares
    elif num_usuario==0:   #condicion en el caso que sea cero
        num_par=num_par+1   #contador de numeros pares

print("Cantidad de numeros pares",num_par,",Cantidad de impares",num_impar,",Cantidad de positivos",num_positivo,".Cantidad de negativos",num_negativo)
#Imprime los resultados por pantalla

print("//////////////////////////////////////////////////////////////////////////")

#Ejercicio9:
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

sum=0 #inicializacion de las variables para sumar y contar en cero
cont=0

for i in range (1,5):  #bucle al usuario ingresar los numeros
    print("Ingrese un numero distinto de cero")
    num_usuario=int(input()) #almacena los numeros en la variable
    while num_usuario==0 :  #condicion para validacion de los numeros distintos de cero
        print("El numero debe ser distinto de cero")
        num_usuario=int(input())
    sum=sum+num_usuario #acumula los numeros ingresados
    cont=cont+1 #registra la cantidad de veces que se realiza el ciclo 
med=sum/cont #calcula la media de los numeros validos

print(f"La media de los numeros ingresados es : ",med)  #muestra el resultado de la media

print("//////////////////////////////////////////////////////////////////////")

#Ejercicio10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("Ingrese el numero que desea invertir") #solicita al usuario el numero
num_usuario=int(input())  #almacena el numero que ingreso
num_ingresado=num_usuario    #lo reasigna a esa nueva variable
num_invertido=0  #variable inicializada en cero

if num_ingresado<0:  #condicion para que el numero sea positivo
    num_negativo=True
    num_ingresado=-num_ingresado #lo convierte a positivo
else:
    num_negativo=False

while num_ingresado>0: #bucle mientras el numero sea positivo
    digito=num_ingresado %10  #obtiene el ultimo digito resto de la division por 10
    num_invertido=num_invertido *10 + digito     #agrega el digito al numero invertido
    num_ingresado=num_ingresado//10   #elimina el ultimo digito al dividir por 10

if num_negativo: #condicion para el caso de que haya sido negativo
    num_invertido=-num_invertido #entonces le agrega al numero invertido el menos delante

print(f"El numero original es {num_usuario} y el invertido es: {num_invertido}") #imprime por pantalla el original y el invertido

print("////////////////////////////////////////////////////////////////////////////////")


