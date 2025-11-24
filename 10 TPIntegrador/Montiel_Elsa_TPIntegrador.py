import csv
import os
mi_archivo_csv='paises.csv'
def cargar_paises():  #carga la lista de pises desde el archivo csv
    paises=[]
    os.path.exists(mi_archivo_csv)
    if os.path.exists(mi_archivo_csv):
        print(f"Archivo encontrado.")
        with open(mi_archivo_csv,'r') as archivo:
            lector=csv.DictReader(archivo)
            for fila in lector:   #convertir poblacion y superficie a entero
                fila['Poblacion']=int(fila['Poblacion'])
                fila['Superficie']=int(fila['Superficie'])
                paises.append(fila)
                print(f"Se gargaron {len(paises)} paises desde {mi_archivo_csv}")
    else:
        print(f"Archivo {mi_archivo_csv} no encontrado")
    return paises


def guardar_paises(paises): #guarda la lista de paises
    if not paises:
        encabezados=['Pais','Poblacion','Superficie','Continente']
    else:
        encabezados=list(paises[0].keys())
        with open(mi_archivo_csv,'w')as archivo:
            escritor=csv.DictWriter(archivo,fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(paises)
            print(f"Datos guardados correctamente en {mi_archivo_csv}")
            return True
        
def obtener_input(mensaje,tipo=str,puede_ser_vacio=False): #solicita entrada, que no este vacia y sea sel tipo correcto
    while True:
        entrada=input(mensaje).strip()
        if not entrada and not puede_ser_vacio:
            print("El campo no puede estar vacio")
            continue
        if tipo==int:
            if entrada.isdigit():
                return int(entrada)
            else:
                print("Error entrada invalida")
                continue
        return entrada

def encontrar_paises_por_nombre(paises,nombre_buscado,coincidencia_exacta=False):  #Busca un pais por nombre coincidencia exacta o parcial
    resultados=[]
    nombre_buscado_lower=nombre_buscado.lower()
    for pais in paises:
        nombre_pais_lower=pais['Nombre'].lower()
        if coincidencia_exacta and nombre_pais_lower==nombre_buscado_lower:
            return [pais] #retorna pais en busqueda exacta
        elif not coincidencia_exacta and nombre_buscado_lower in nombre_pais_lower:
            resultados.append(pais)
    return resultados

def mostrar_lista_paises(lista_a_mostrar):
    if not lista_a_mostrar:
        print("No se encontraron paises")
        return
    print("\n***Lista de Paises***")
    print(f"{'Nombre':<20}{'Poblacion':>20}{'Superficie':>18}{'Continente':<15}")
    print("*"*73)
    for pais in lista_a_mostrar:
        print(f"{pais['Nombre']:<20}{pais['Poblacion']:>20,}{pais['Superficie']:>18,}{pais['Continente']:<15}")
    print("#"*73)


def agregar_pais(paises):   #Agregar un nuevo pais(Opcion1)
    print("\n***Agregar un nuevo Pais***")
    nombre=obtener_input("Nombre del Pais: ")
    poblacion=obtener_input("Poblacion: ",tipo=int)
    superficie=obtener_input("Superficie: ",tipo=int)
    continente=obtener_input("Continente: ")
    nuevo_pais={'Nombre':nombre,'Poblacion':poblacion,'Superficie':superficie,'Continente':continente}
    paises.append(nuevo_pais)
    print(f"Pais {nombre} agregado")
    guardar_paises(paises)

def actualizar_datos(paises):  #Actualizar poblacion y superficie de un pais(Opcion2)
    nombre_buscado=obtener_input("Nombre del pais a actualizar (exacto): ")
    resultados=encontrar_paises_por_nombre(paises,nombre_buscado,coincidencia_exacta=True)
    if not resultados:
        print(f"Pais {nombre_buscado} no encontrado")
        return
    pais=resultados[0]
    print(f"\n---Actualizando datos de {pais['Nombre']}---")
    nueva_poblacion=obtener_input(f"Nueva Poblacion (Actual:{pais['Poblacion']:,}): ",tipo=int,puede_ser_vacio=True)
    nueva_superficie=obtener_input(f"Nueva Superficie(Actual:{pais['Superficie']:,}): ",tipo=int,puede_ser_vacio=True)
    if nueva_poblacion is not None:
        pais['Poblacion']=nueva_poblacion
        print("Poblacion actualizada")
    if nueva_superficie is not None:
        pais['Superficie']=nueva_superficie
        print("Superficie actualizada")
    if nueva_poblacion is None and nueva_superficie is None:
        print("No se realizaron cambios")
    guardar_paises(paises)

def buscar_pais(paises):  #Buscar pais por nombre(Opcion3)
    nombre_buscado=obtener_input("Ingrese el nombre o parte del nombre del pais: ")
    resultados=encontrar_paises_por_nombre(paises,nombre_buscado,coincidencia_exacta=False)
    if resultados:
        print(f"\n Resultados de la busqueda para {nombre_buscado}: ")
        mostrar_lista_paises(resultados)
    else:
        print(f"No se encontraron coincidencias para {nombre_buscado}")

def filtrar_paises(paises):  #Filtar Paises por Continente,rango de poblacion o rengo de superficie(Opcion4)
    print("\n---Opciones de filtrado---")
    print("A) Filtrar por Continente")
    print("B) Filtrar por rango poblacion")
    print("C) Filtara por rango superficie")
    opcion_filtro=obtener_input("Seleccione una opcion (A,B,C): ").upper()
    paises_filtrados=paises
    if opcion_filtro=='A':
        continente_buscado=obtener_input("Ingrese el continente a filtrar: ").capitalize()
        paises_filtrados=[p for p in paises if p['Continente'].capitalize()==continente_buscado]
    elif opcion_filtro=='B':
        print("\nIngrese el rango de poblacion(dejar vacio para no limitar):")
        pob_min=obtener_input("Poblacion Mínima: ",tipo=int,puede_ser_vacio=True)
        pob_max=obtener_input("Poblacion Máxima: ",tipo=int,puede_ser_vacio=True)
        paises_filtrados=[p for p in paises if (pob_min is None or p['Poblacion']>=pob_min)and (pob_max is None or p['Poblacion']<=pob_max)]
    elif opcion_filtro=='C':
        print("\nIngrese el rango de superficie (dejar vacio para no limitar):")
        sup_min=obtener_input("Superficie Mínima:",tipo=int,puede_ser_vacio=True)1
        
        sup_max=obtener_input("Superficie Máxima:",tipo=int,puede_ser_vacio=True)
        paises_filtrados=[p for p in paises if (sup_min is None or p['Superficie']>=sup_min)and (sup_max is None or p['Superficie']>=sup_max)]
    else:
        print("Opcion de filtro invalida")
        return
    print("\n---Paises Filtados---")
    mostrar_lista_paises(paises_filtrados)

def ordenar_paises(paises): #Ordena paises en forma ascendente(Opcion5)
    if not paises:
        print("El catálogo está vacío")
        return
    print("\n***Opciones de ordenamiento ascendente***")
    print("\n---Opciones de ordenamiento ascendente---")
    print("1) Ordenar por nombre")
    print("2) Ordenar por poblacion")
    print("3) Ordenar por superficie")
    opcion_orden=obtener_input("Seleccione la opción de ordenamiento: ",tipo=int)
    clave_orden=None
    if opcion_orden==1:
        clave_orden='Nombre'
    elif opcion_orden==2:
        clave_orden='Poblacion'
    elif opcion_orden==3:
        clave_orden='Superficie'
    else:
        print("Opción de ordenamiento inválida")
        return
    lista_a_ordenar=list(paises)
    n=len(lista_a_ordenar)
    for i in range(n):   #bucle interno realiza las comparaciones y los intercambios
        for j in range(0,n-i-1):
            if lista_a_ordenar[j][clave_orden]>lista_a_ordenar[j+1][clave_orden]: #comparacion de los valores de la clave
                lista_a_ordenar[j],lista_a_ordenar[j+1]=lista_a_ordenar[j+1],lista_a_ordenar[j] #realiza el intercambio
    print(f"\n***Paises ordenados por {clave_orden}***")
    mostrar_lista_paises(lista_a_ordenar)

def mostrar_estadisticas(paises):   #Mostrar estadísticas(Opcion6)
    if not paises:
        print("El catálogo está vacio. No hay estadísticas para mostrar")
        return
    pais_mayor_pob=paises[0]   #inicialización asignamos el 1° país como el extremo
    pais_menor_pob=paises[0]
    pais_mayor_sup=paises[0]
    pais_menor_sup=paises[0]
    for pais in paises:   #bucle para encontrar los extremos
        if pais['Poblacion']>pais_mayor_pob['Poblacion']:  #lógica para poblacion
            pais_mayor_pob=pais
        if pais['Poblacion']<pais_menor_pob['Poblacion']:
            pais_menor_pob=pais
        if pais['Superficie']>pais_mayor_sup['Superficie']: #lógica para superficie
            pais_mayor_sup=pais
        if pais['Superficie']<pais_menor_sup['Superficie']:
            pais_menor_sup=pais
    print("\n---Estadisticas---")
    print(f"Pais con mayor poblacion: {pais_mayor_pob['Nombre']}({pais_mayor_pob['Poblacion']:,} hab)")
    print(f"Pais con menor poblacion: {pais_menor_pob['Nombre']}({pais_menor_pob['Poblacion']:,} hab)")
    print(f"Pais con mayor superficie: {pais_mayor_sup['Nombre']} ({pais_mayor_sup['Superficie']:,})")
    print(f"Pais con menor superficie: {pais_menor_sup['Nombre']} ({pais_menor_sup['Superficie']:,})")
    print("*"*40)
    total_poblacion=sum(p['Poblacion']for p in paises)
    total_superficies=sum(p['Superficie']for p in paises)
    num_paises=len(paises)
    promedio_pob=total_poblacion/num_paises
    promedio_sup=total_superficies/num_paises
    print(f"Promedio de poblacion: {promedio_pob:,.0f} hab.")
    print(f"Promedio de superficie: {promedio_sup:,.2f}")
    print("*"*40)
    paises_por_continente={}   #cantidad de paises por continente
    for pais in paises:
        continente=pais['Continente']
        if continente in paises_por_continente:
            paises_por_continente[continente] +=1
        else:
            paises_por_continente[continente]=1
    print("\n Cantidad de paises por continenete:")
    for cont, count in paises_por_continente.items(): #variable cont(nombre del continente) y count(numero total de países para ese continente)
        print(f" - {cont}:{count} paises")


#Menu principal
def menu_principal():
    paises=cargar_paises()
    while True:
        print("\n"+"="*40)
        print("Gestion de Catalogo de Paises")
        print("="*40)
        print("1-Agregar pais")
        print("2-Actualizar poblacion y superficie")
        print("3-Buscar pais por nombre")
        print("4-Filtar paises")
        print("5-Ordenar paises")
        print("6-Mostrar estadísticas")
        print("7-Salir")
        print("-"*40)
        opcion=obtener_input("Seleccione una opcion (1-7): ",tipo=str)
        match opcion: #uso de match case para la seleccion
            case '1':
                agregar_pais(paises)
            case '2':
                actualizar_datos(paises)
            case '3':
                buscar_pais(paises)
            case '4':
                filtrar_paises(paises)
            case '5':
                ordenar_paises(paises)
            case '6':
                mostrar_estadisticas(paises)
            case '7':
                print("Saliendo del programa")
                break
            case _:     
                print("opcion invalida")

menu_principal()

