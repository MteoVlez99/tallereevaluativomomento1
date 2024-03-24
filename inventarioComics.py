from collections import defaultdict
import random

Productos = []
Producto = {}

ubicacion = defaultdict(lambda: 50, {'A': 50, 'B': 50, 'C': 50, 'D': 50})

def generarId():
    
    """numeros = list(range(1,101))
    id_aleatorio = random.sample(numeros, k=1)
    return id_aleatorio"""
    
   
    ids = list(range(1,100))

    ids_generados = random.sample(ids,1)[0]
    return ids_generados

id=generarId()


id = generarId()

def validar_opcion():
    while True:
        opcion = input("Elige una opción: ")
        if opcion.isdigit():  
            return int(opcion)  
        else:
            print("Por favor, ingresa un número válido.")

def validar_precio():
    while True:
        precio = input("Digite el precio unitario del producto: ")
        if precio.isdigit():  
            return int(precio)  
        else:
            print("Por favor, ingresa un precio válido.")

def validar_unidades():
    while True:
        unidades = input("Digite el numero de unidades compradas de este producto: ")
        if unidades.isdigit():  
            return int(unidades)  
        else:
            print("Por favor, ingresa un valor válido.")
            
while True:
    
    Producto = {}

    print("\n ********Administrador De Inventario*********")
   
    print("\n 1° Registrar Producto ")
    print(" 2° Buscar y Mostrar Productos Bodega")
    print(" 3° Buscar y Mostrar Producto Especifico ")
    print(" 4° Buscar y Modificar Unidades Compradas ")
    print(" 5° Eliminar Producto ")
    print(" 6° Finalizar ")
    
    opcion = validar_opcion()
    
    if opcion == 1:
    
        Producto["id"] = print("\nID generado automáticamente: ", id)
        Producto["nombre"] = input("Digite el nombre del producto: ").upper()
        Producto["precio"] = validar_precio()
        Producto["ubicacion"] = input("Digite la zona del producto (A,B,C,D): ").upper()
        Producto["descripcion"] = input("Digite la descripcion del producto: ").upper()        
        Producto["casa"] = input("Digite la casa a la cual pertenece el producto (Marvel, DC): ").upper()
        Producto["pais"] = input("Digite el pais de origen del producto: ").upper()
        Producto["unidades"] = validar_unidades()
        Producto["garantia"] = input("¿El producto tiene garantía extendida? : ").upper()
    
        if Producto["unidades"] <=ubicacion[Producto["ubicacion"]]:
            ubicacion[Producto["ubicacion"]] -= Producto["unidades"]
            print(f"Productos restantes en la zona {Producto["ubicacion"]}: {ubicacion[Producto["ubicacion"]]}")
    
        else:
            print("No hay suficientes productos en esta zona.")

        Productos.append(Producto)
    
    elif opcion == 2:
       
       buscarZona = input("Ingrese la letra de la zona a la cual desea acceder: ").upper()
       for inventario in Productos:
           if inventario ["ubicacion"] == buscarZona:
               print(f"el numero del id es: {inventario["id"]},\nel nombre del producto es: {inventario["nombre"]},\nprecio del producto es: {inventario["precio"]},\nla casa a la cual pertenece es: {inventario["casa"]},\nel pais de origen es: {inventario["pais"]},\nel numero total de unidades compradas es de: {inventario["unidades"]}\n")
    
    elif opcion == 3:
       
       buscarProducto = input("Ingrese el nombre del producto que desea buscar: ").upper()
       for nombreProducto in Productos:
           if nombreProducto["nombre"] == buscarProducto:
               print(f"el numero del id es: {nombreProducto["id"]},\nel nombre del producto es: {nombreProducto["nombre"]},\nprecio del producto es: {nombreProducto["precio"]},\nla descripsion del producto es: {nombreProducto["descripcion"]} \n")
               
    elif opcion == 4:
        buscarProducto = input("Ingrese el nombre del producto que desea buscar: ").upper()
        for producto in Productos:
            if producto["nombre"] == buscarProducto:
                print(f"Unidades compradas actualmente: {producto['unidades']}")
                nuevas_unidades = validar_unidades()
                if nuevas_unidades <= producto["unidades"]:
                    producto["unidades"] = nuevas_unidades
                    print("Unidades compradas modificadas correctamente.")
                else:
                    print("La cantidad de unidades compradas no puede ser mayor a la cantidad inicial.")
            else:
                print("Producto no encontrado.")
                
    elif opcion == 5:
        buscarProducto = input("Ingrese el nombre del producto que desea buscar: ").upper()
        for producto in Productos:
            if producto["nombre"] == buscarProducto:
                confirmacion = input(f"¿Está seguro de que desea eliminar el producto '{buscarProducto}'? (S/N): ").upper()
                if confirmacion == "S":
                    Productos.remove(producto)
                    print(f"El producto '{buscarProducto}' ha sido eliminado del inventario.")
                break
            else:
                print("Producto no encontrado.")


        