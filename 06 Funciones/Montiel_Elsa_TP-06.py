#Ejercicio1)
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#Funciones
def imprimir_hola_mundo():
    print("Hola Mundo")
    return

#Programa principal
imprimir_hola_mundo()

print("###########################################################################")#####
#Ejercicio2)
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#Funciones
def saludar_usuario(nombre):
    print(f"Hola,{nombre}!")
    return
    

#Programa principal
nombre_usuario=input("Por favor dime tu nombre: ")
saludar_usuario(nombre_usuario)

print("###########################################################################")
#Ejercicio3)
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#egresados.

#Funciones
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return

#Programa principal
nombre_usuario=input("Por favor dime tu nombre: ")
apellido_usuario=input("Por favor dime tu apellido: ")
edad_usuario=input("Por favor dime tu edad: ")
residencia_usuario=input("Por favor dime donde vives: ")
informacion_personal(nombre_usuario,apellido_usuario,edad_usuario,residencia_usuario)
print("############################################################################")

#Ejercicio4)
# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados


import math    #importar el valor de PI
valor_de_pi=math.pi
#Funciones
def calcular_area_circulo(radio):   #Calcula el area
    area=valor_de_pi*(radio**2)
    area_redondeada=round(area,2)
    return(area_redondeada)

def calcular_perimetro_circulo(radio):    #calcula el perímetro
    perimetro=2*valor_de_pi*radio
    perimetro_redondeado=round(perimetro,2)
    return(perimetro_redondeado)

#Programa principal
radio=0.0 
while radio<=0:        #valida la entrada con while
    entrada=input("Introduce el radio(debe ser positivo): ").strip()
    if not entrada:
        print(" Error La entrada no puede estar vacia")
        continue
    num_puntos=entrada.count('.')   #validacion del formato,solo digitos y maximo 1 punto
    cadena_sin_punto=entrada.replace('.', '',1)
    if num_puntos<=1 and cadena_sin_punto.isdigit():
        radio_temp=float(entrada)
        if radio_temp>0:   #validacion del radio>0
            radio=radio_temp
            break
        else:
            print("Error el radio debe ser mayor a cero")
    else:
        print("Error solo se permiten numeros positivos(dígitos y un punto decimal)")

area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)
print(f"El área es: {area}")
print(f"El perímetro es : {perimetro}")

print("##################################################################")

#Ejercicio5)
# Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

#Funciones
def segundos_a_horas (segundos):
    hora=segundos/3600
    hora_redondeada=round(hora,2)
    return(hora_redondeada)

#Programa
segundos_usuario=int(input("Por favor ingresa la cantidad de segundos a convertir: "))
print(f"La conversion es: ", segundos_a_horas(segundos_usuario),"horas")

print("#############################################################")

#Ejercicio6)
# Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

#Funciones
def tabla_de_multiplicar(numero):
    for i in range(1,11):
        resultado=numero*i
        print(resultado)
    
#Programa principal
numero_usuario=int(input("Por favor ingrese el numero para obtener su tabla de multiplicar: "))
tabla_de_multiplicar(numero_usuario)

print("##################################################################")
#Ejercicio7)
# Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara.

#Funciones
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=0    #bandera para evitar la division por cero
    estado_de_division=True
    if b!=0:
        division=a/b
    else:
        estado_de_division=False
    return(suma,resta,multiplicacion,division,estado_de_division)

#Programa principal
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
s,r,m,d,estado=operaciones_basicas(num1,num2)
print(f"Resultados de las operaciones con {num1} y {num2}")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicacion: {m}")
if estado:        #sólo si es True muestra el resultado de la division
    print(f"Division: {d:.2f}")
else:
    print("division: ERROR, el divisor es cero")

print("###############################################################")

#Ejercicio8)
# Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales

#Funciones
def calcular_imc(peso,altura):
    return (peso/(altura**2))   # retorna calculo IMC

#Programa principal
peso_Kg=0.0  # validacion del peso
while peso_Kg <=0:
    entrada_peso=input("Ingrese su peso en Kilogramos (Ej: 83.5): ").strip()
    if not entrada_peso:   #validacion no vacío
        print("Error el peso no puede estar vacio")
        continue
    num_puntos=entrada_peso.count('.')   #validacion formato max 1 punto,solo digitos
    cadena_sin_punto=entrada_peso.replace('.', '',1)
    if num_puntos<=1 and cadena_sin_punto.isdigit():
        peso_temp=float(entrada_peso)
        if peso_temp>0:
            peso_Kg=peso_temp
            break
        else:
            print("Error el peso debe ser positivo")
    else:
        print("Error solo se permiten numeros>0 y un unico punto decimal")

altura_m=0.0   #validacion de la altura
while altura_m <=0:
    entrada_altura=input("Ingrese su altura en metros (Ej: 1.75): ").strip()
    if not entrada_altura:   #validacion no vacío
        print("Error la altura no puede estar vacio")
        continue
    num_puntos=entrada_altura.count('.')   #validacion formato max 1 punto,solo digitos
    cadena_sin_punto=entrada_altura.replace('.', '',1)
    if num_puntos<=1 and cadena_sin_punto.isdigit():
        altura_temp=float(entrada_altura)
        if altura_temp>0:
            altura_m=altura_temp
            break
        else:
            print("Error la altura debe ser positiva")
    else:
        print("Error solo se permiten numeros>0 y un unico punto decimal")

imc=calcular_imc(peso_Kg,altura_m)
print(f"Su peso ingresado es: {peso_Kg:.2f}")
print(f"Su altura ingresada es: {altura_m:.2f} metros")
print(f"Su IMC es: {imc:.2f}")

print("######################################################")

#Ejercicio9)
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#Funciones
def celsius_a_fahrenheit(celsius):
    return((celsius*9/5)+32)
    

#Programa principal
celsius_temp=None   #validacion de la entrada numérica
es_valido=False
while not es_valido:
    entrada_str=input("Ingrese la temperatura en celsius: ").strip()
    if not entrada_str:     
        print("Error la entrada no puede estar vacia")
        continue
    cadena_a_verificar=entrada_str
    if entrada_str.startswith('-'):  #validacion solo digitos,con posible signo 
        cadena_a_verificar=entrada_str[1:]       #negativo y max 1 punto decimal
    if not cadena_a_verificar:     #por si al quitar el signo está vacía
        print("Error ingrese un valor numerico")
        continue
    num_puntos=cadena_a_verificar.count('.')    #cuántos decimales hay
    cadena_sin_punto=cadena_a_verificar.replace('.', '',1) #reemplaza el 1° y unico punto
    if num_puntos<=1 and cadena_sin_punto.isdigit():
        celsius_temp=float(entrada_str)
        es_valido=True
    else:
        print("Error solo se permiten numeros(No letras,No vacio,Ni mas de 1 punto decimal)")

fahrenheit_temp=celsius_a_fahrenheit(celsius_temp)
print(f"Temperatura ingresada en Celsius: {celsius_temp:.2f}°C ")
print(f"Temperatura equivalente en Fahrenheit: {fahrenheit_temp:.2f}°F ")

print("#########################################################")

#Ejercicio10)
#.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función
#Funciones
def calcular_promedio(a,b,c):
    return((a+b+c)/3)

#Programa principal
numeros=[]   #lista para almacenar los numeros validados
for i in range(3):
    numero_valido=False
    while not numero_valido:
        mensaje=f"Ingrese el numero #{i+1}: "
        entrada=input(mensaje).strip()  #elimina espacios en blanco
        if not entrada:
            print("Error la entrada no puede estar vacia")
            continue
        if entrada.count('.')>1:  #solo un punto decimal
            print("Error solo se permite un punto decimal")
            continue
        es_valido_caracter=True
        for caracter in entrada:
            if not (caracter.isdigit() or caracter =='.'):
                es_valido_caracter=False
                break
        if not es_valido_caracter:
            print("Error solo se permiten numeros y un punto decimal")
            continue
        if entrada =='.':   #entrada sólo un punto
            print("Error la entrada no puede ser solo un punto")
            continue
        num_flotante=float(entrada)
        if num_flotante<0:    #validacion numero negativo
            print("Error no se permiten numeros negativos")
            continue
        numeros.append(num_flotante)  #si paso las validaciones los agrega a la lista
        numero_valido=True

num1,num2,num3=numeros[0],numeros[1],numeros[2]
promedio=calcular_promedio(num1,num2,num3)
print(f"Los numeros ingresados son: {num1}, {num2}, {num3}")
print(f"El promedio de los numeros es: {promedio:.2f}")


print("#################################################")












