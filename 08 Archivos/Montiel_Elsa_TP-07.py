#Ejercicio1)
#Crear un archivo inicial con productos.Crear un archivo de texto
#llamado productos.txt con 3 productos.Cada linea debe tener
#nombre, precio,cantidad
def crear_archivo():
    productos=["lapicera,120.5,30","cuaderno,320,12","goma,130,6"]

    with open("productos.txt","w")as archivo:
        archivo.write("Nombre,Precio,Cantidad\n")
        for producto in productos:
            archivo.write(producto +"\n")
            print(producto)

crear_archivo()
print("####################################################")
#Ejercicio2)
#Leer y mostrar productos:crear un programa que abra productos.txt, lea cada linea, 
#la procese con.strip() y .split(",") y muestre los productos

def procesar_archivo():
    with open("productos.txt","r")as archivo:
        next(archivo)    #salta la primera línea que son los titulos
        for linea in archivo:
            linea_limpia=linea.strip()
            if linea_limpia:    #divide la cadena en una lista de 3 elementos
                datos=linea_limpia.split(",")
                nombre=datos[0]
                precio=datos[1]
                cantidad=datos[2]
                print(f"Producto:{nombre}|"f"Precio: ${precio}|"f"Cantidad:{cantidad}")

procesar_archivo()
print("##########################################################")
#Ejercicio3)
#Agregar productos desde teclado:Modificar el programa para luego de mostrar los productos,
# le pida al usuario que ingrese un nuevo producto (nombre,precio,cantidad) y lo agregue
# al archivo sin borrar el contenido existente

def agregar_producto(nombre_archivo="productos.txt"):
    print("Agregar nuevo producto")
    while True:      
        nombre_ingresado=input("Ingrese el nombre de producto: ").strip()
        if not nombre_ingresado:
            print("El nombre del producto no puede estar vacio")
            continue
        break

    precio_str=input("Ingrese el precio: ").strip()   #solicita precio, cantidad y lo agrega
    cantidad_str=input("Ingrese la cantidad: ").strip()
    with open(nombre_archivo,"a")as archivo:
        linea=f"{nombre_ingresado},{precio_str},{cantidad_str}\n"
        archivo.write(linea)
        print(f"Producto:'{nombre_ingresado} adjuntado a '{nombre_archivo}'.")

agregar_producto()

print("################################################################")
#Ejercicio3)Carga mas de un producto
print("Ejercicio modificado carga mas de un Producto!!")
def agregar_mas_de_un_producto(nombre_archivo="productos.txt"):
    with open(nombre_archivo,"a")as archivo:
        continuar="s"
        while continuar.lower()=="s":
            print("Ingrese nuevo producto")
            nombre=input("Nombre del producto: ").strip()
            precio=input("Precio del producto: ").strip()
            cantidad=input("Cantidad del producto: ").strip()
            if not nombre or not precio or not cantidad:    #validacion para que los campos esten llenos
                print("Todos los campos deben estar completos")
                continue
            linea=f"{nombre},{precio},{cantidad}\n"
            archivo.write(linea)   #escribir la linea en el archivo
            print(f"Producto: '{nombre}' agregado correctamente")
            continuar=input("Desea agregar otro producto? (s/n): ").strip()
            if continuar.lower()!='s':
                break

agregar_mas_de_un_producto()
print("**************************************************************************")
#Ejercicio4)
#Cargar productos en una lista de diccionarios :Al leer el archivo, cargar los datos en una lista llamada productos 
#donde cada elemento sea un diccionario con claves: nombre,precio, cantidad
productos=[]
nombre_archivo="productos.txt"
with open (nombre_archivo,"r")as archivo:
    lineas=archivo.readlines()
    for linea in lineas:
        datos=[d.strip() for d in linea.strip().split(",")]  #limpiar la linea
        if len(datos)==3:
            nombre=datos[0]
            precio=datos[1]
            cantidad=datos[2]
            produc_diccionario={"nombre":nombre,"precio":precio,"cantidad":cantidad} #crea diccionario
            productos.append(produc_diccionario)

print("Contenido de la lista")
for p in productos:
    print(p)

print("#########################################################################")
#Ejercicio5)
#Buscar producto por nombre:Pedir al usuario que ingrese el nombre de un producto
#Recorrer la lista de productos y si lo encuentra mostrar todos sus datos
#Si no existe mostrar un mensaje de error
print("Ejercicio 5")
def buscar_producto(nombre_archivo="productos.txt"):
    buscar_nombre=input("Ingresa el nombre del producto a buscar: ").strip().lower()
    producto_encontrado=None
    with open (nombre_archivo,"r")as archivo:
        for linea in archivo:
            partes=[parte.strip() for parte in linea.strip().split(",")]  #limpiar la linea
            if len(partes) ==3:    #verificar los 3 elementos
                nombre=partes[0].lower()
                if nombre==buscar_nombre:   #comparar nombre ingresado con el del archivo
                    producto_encontrado={"nombre":partes[0],"precio":partes[1],"cantidad":partes[2]}
                    break
    if producto_encontrado:
        print(f"Nombre :{producto_encontrado['nombre']}")
        print(f"Precio :{producto_encontrado['precio']}")
        print(f"Cantidad :{producto_encontrado['cantidad']}")
    else:
        print(f"ERROR el producto: '{buscar_nombre}' NO EXISTE en la lista")

buscar_producto()
print("#######################################################################")

#Ejercicio6)
#despues de haber leido,buscado o agregado productos, sobreescribir el archivo productos.txt 
#escribiendo nuevamente todos los productos actualizados desde la lista
print("Ejercicio 6")
nombre_archivo="productos.txt"

def leer_productos_del_archivo(nombre_archivo):
    productos_leidos=[]
    with open(nombre_archivo,"r")as archivo:
        for linea in archivo:
            datos=[d.strip() for d in linea.strip().split(",")]
            if len(datos)==3:
                productos_leidos.append({"nombre":datos[0],"precio":datos[1],"cantidad":datos[2]})
    return productos_leidos

def guardar_actualizados(productos,nombre_archivo="productos.txt"):
    with open(nombre_archivo,"w")as archivo:
        for producto in productos:   #extraer los valores
            nombre=producto["nombre"]
            precio=producto["precio"]
            cantidad=producto["cantidad"]
            linea=f"{nombre},{precio},{cantidad}\n"
            archivo.write(linea)
print("Archivo actualizado")

productos=leer_productos_del_archivo(nombre_archivo)
guardar_actualizados(productos,nombre_archivo)
for p in productos:
    print(p)
    















