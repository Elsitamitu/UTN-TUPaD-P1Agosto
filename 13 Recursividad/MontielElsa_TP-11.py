#Ejercicio1:Factorial recursivo
def factorial_recur(x):
    if x==0:
        return 1
    else:
        return x*factorial_recur(x-1)

def factorial():
    n=0
    while True:
        num_str=input("Ingresa un numero entero positivo n para calcular los factoriales hasta ese numero :")
        if not num_str.isdigit():
            print("Error entrada invalida")
            continue
        n=int(num_str)
        if n<1:
            print("Por favor ingresa numero mayor o igual a 1")
            continue
        break
    for i in range(1,n+1):
        resultado=factorial_recur(i)
        print(f"El factorial de {i} es {resultado}")
        print("-"*40)
factorial()
print("#"*40)
#Ejercicio2:Fibonacci recursivo
def fibonacci_recur(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_recur(num-1)+fibonacci_recur(num-2)
    
def fibonacci():
    n=-1
    while True:
        num_str=input("Ingresa la posicion n>=0 de la serie de Fibonacci: ")
        if not num_str.isdigit():
            print("Error entrada invalida")
            continue
        n=int(num_str)
        if n<0:
            print("Valor invalido la posicion debe ser cero 0 o mayor")
            continue
        break
    print(f"\n--Serie de Fibonacci hasta la posicion {n}-- ")
    print("Posicion|Valor")
    print("--------|-----")
    for i in range(n+1):
        resultado=fibonacci_recur(i)
        print(f"{i:<8}|{resultado}")
        print("-"*40)

fibonacci()
print("#"*40)
#Ejercicio3:Potencia Recursiva
def potencia_recur(n,m):  #calculo de potencia base n y exponente m
    if m == 0:
        return 1
    else:
        return n*potencia_recur(n,m-1)

def num_usuario(mensaje, debe_ser_positivo=False):  #solicita un numero y valida su entrada
    while True:
        entrada_usuario=input(mensaje).strip()
        es_negativo=entrada_usuario.startswith('-')   #en el caso de ser negativo validamos el resto de la cadena
        if es_negativo:valor_a_comprobar=entrada_usuario[1:]
        else:
            valor_a_comprobar=entrada_usuario
        if valor_a_comprobar.isdigit():       #validacion para el exponente 
            numero=int(entrada_usuario)
            if debe_ser_positivo and numero<0:
                print("El exponente debe ser un entero positivo (sin el signo +) o cero")
            else:
                return numero
        else:
            print("Error entrada no valida")

def calculadora():
    n=num_usuario("Ingrese la base,debe ser entero: ")
    m=num_usuario("Ingrese el exponente,debe ser positivo o cero: ",debe_ser_positivo=True)
    resultado=potencia_recur(n,m)
    print(f"\n Resultado: {n} elevado a la {m} es igual a {resultado}")

calculadora()

print("#"*40)
#Ejercicio 4):de Decimal a Binario recursivo
def decimal_a_binario_recur(n):   #convierte un numero decimal entero positivo a base 2
    if n==0:
        return ""
    else:
        return decimal_a_binario_recur(n//2)+str(n%2)  #concatena el resto de la division con el cociente 

def num_valido():
    while True:    #solicita un entero y valida la entrada
        entrada=input("Ingrese un entero positivo: ").strip()
        if entrada.isdigit():
            numero=int(entrada)
            if numero>0:
                return numero
            else:
                print("Error el numero debe ser positivo >0")
        else:
            print("Error entrada no valida")

def convertir():
    numero_usuario=num_valido()
    resultado_binario=decimal_a_binario_recur(numero_usuario)
    print(f"\n El numero decimal {numero_usuario} en binario es: {resultado_binario}")

convertir()
print("#"*40)
#Ejercicio 5   #Verifica si una cadena es un palíndromo
import unicodedata
def es_palindromo(palabra):
    if len(palabra)<=1:    #si la cedena tiene 0 o 1
        return True
    elif palabra[0]==palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def limpiar_palabra(cadena): #convierte a minuscula,elimina espacios y elimina tildes 
    cadena=cadena.lower()
    cadena= "".join(cadena.split())
    cadena_sin_tide=unicodedata.normalize('NFKD',cadena).encode('ascii','ignore').decode('utf-8') 
    return cadena_sin_tide

def principal():
    entrada_usuario=input("Ingrese la palabra para verificar si es palindromo: ")
    cadena_limpia=limpiar_palabra(entrada_usuario)
    print(f"Cadena usuario es {entrada_usuario} y cadena limpia es {cadena_limpia}")
    if es_palindromo(cadena_limpia):
        print("Es palindromo la palabra")
    else:
        print("No es palindromo la palabra")

principal()
print("#"*40)
#Ejercicio 6)  #suma de todos los dígitos
def suma_digitos(n):
    if n==0:
        return 0
    return(n%10)+suma_digitos(n//10)

def obtener_entero_pos():
    while True:
        entrada=input("Ingrese un entero positivo del que quiera saber su suma: ").strip()
        if entrada.isdigit():
            numero=int(entrada)
            if numero>0:
                return numero
            else:
                print("Error el numero debe ser positivo")
        else:
            print("Error entrada no válida")

def ingresar():
    numero_usuario=obtener_entero_pos()
    resultado_suma=suma_digitos(numero_usuario)
    print(f"\n La suma de los digitos de {numero_usuario} es {resultado_suma}")

ingresar()

print("#"*40)

#Ejercicio 7) #Número de bloques para la pirámide
def contar_bloques(n):   #calcula el total de bloques
    if n==1:
        return 1
    else:
        return n+contar_bloques(n-1)
    
def validacion_entero():
    n=0
    while n<=0:
        entrada_usuario=input("Ingrese el numero de bloques para la base de la piramide: ")
        if entrada_usuario.isdigit():
            n=int(entrada_usuario)
            if n<=0:
                print("Error debe ser positivo")
        else:
            print("Error debe ser entero positivo")
            n=0
    total_bloques=contar_bloques(n)
    print(f"\nEl total de bloques para una piramide con base {n} es {total_bloques}")

validacion_entero()
print("#"*40)
#Ejercicio 8) Contar cuantas veces aparece cierto digito en un numero
def contar_digito(numero,digito):
    if numero==0:
        return 0
    ultimo_digito=numero%10
    contador=1 if ultimo_digito==digito else 0
    return contador + contar_digito(numero // 10,digito)

def validar_entrada(mensaje,es_digito=False):
    while True:
        entrada_usuario=input(mensaje).strip()
        if entrada_usuario.isdigit():
            numero=int(entrada_usuario)
            if es_digito:
                if 0<= numero <=9:
                    return numero
                else:
                    print("Error el digito debe ser entre 0 y 9")
            else:
                if numero>0:
                    return numero
                else:
                    print("Error el numero debe ser positivo mayor que cero")
        else:
            print("Error ingrese solo digitos")

def principal():
    numero=validar_entrada("Ingrese el numero positivo: ",es_digito=False)
    digito=validar_entrada("Ingrese el digito a buscar: ",es_digito=True)
    cantidad_encontrada=contar_digito(numero,digito)
    print(f"\n El digito {digito} aparece en el numero {numero} {cantidad_encontrada} veces")

principal()













