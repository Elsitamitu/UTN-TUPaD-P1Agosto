#README: Gestor de Catálogo de Países
##Descripcion del Programa
Este es un programa de gestión de catálogo de países desarrollado en Python que permite a los usuarios administrar, consultar y analizar datos geográficos y demográficos.
El sistema está diseñado modularmente para manipular una **Lista de Diccionarios** y garantiza la **persistencia de datos** utilizando el formato **CSV** (Valores separados por comas).
El código cumple con las siguientes consideraciones:
* **La validación** se realiza mediante inspección de archivos (`os.path.exists`)
e inspección de cadenas (`.isdigit()`).
* **El ordenamiento** se realiza mediante el método de lista **`.sort()`** y a funciones `key`definidas explícitamente.
##Instrucciones de Uso
###Requisitos
El programa sólo requiere tener instalado ##Python 3.10 o superior** 
###Ejemplos de entrada y salida
1.##Agregar un País (Opción 1)
Entrada:1          Salida:Nombre del País:
Entrada:España     Salida:Población:
Entrada:47000000   Salida:Superficie:
Entrada:505000     Salida:Continente:
Entrada:Europa     Salida:País España agregado, Datos guardados correctamente en paises.csv

2.##Búsqueda parcial (Opción 3)
Entrada:3          Salida:Ingrese el nombre o parte del nombre del país
Entrada:ar         Salida:Resultados de la búsqueda para ar, Salida:Argentina, Salida:Argelia

3. ##Ordenar Países(Opción 5)
Entrada:5         Salida: (luego de mostrar por pantalla las opciones 1,2,3 ) Seleccione la opcion de ordenamiento
Entrada:1         Salida: Paises ordenados por Nombre: ,Salida:Argelia, Salida:Argentina, Salida:España



