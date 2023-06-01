# Definir los costos de las entradas 
costo_niño = 5500
costo_joven = 7000
costo_adulto = 9000


# Inicializar las variables para el total y la cantidad de entradas
total_pagar = 0
cantidad_entradas = 0 

# Ciclo iterativo para registrar las ventas
while True: 
    # Solicitar el tipo de entrada al usuario 
    print("********************************************************")
    cantidad = input("Ingrese la categoria de la entrada (niño, joven, adulto): ")
    print("********************************************************")

    # Solicitar la cantidad de entradas al usuario 
    print("********************************************************")
    cantidad = int(input("Ingrese la cantidad de entradas: "))
    print("********************************************************")

    # Calculas el costo total de las entradas segun la categoria 
    if categoria.lower() == "niño":
        costo_total = cantidad * costo_niño
    elif categoria.lower() == "joven":
        costo_total = cantidad * costo_joven
    elif categoria.lower() == "adulto":
        costo_total = cantidad * costo_adulto 
    else: 
        print("***********************************************************")
        print("Categoria no valida. Por favor, Ingrese una categoria valida.")
        print("***********************************************************") 
        continue 

    # Actualizar el total a pagar y la cantidad de entradas vendidas
    total_pagar += costo_total
    cantidad_entradas += cantidad 

    # Solicitar al usuario si desea continuar registrando ventas 
    respuesta = input("¿Desea registrar otra venta? (s/n): ")
    if respuesta.lower() != "s":
        break

# Mostrar el resultado final por pantalla 
print("****************************************************")
print("Tipo de categoria: " + categoria)
print("Cantidad de entradas: " + str(cantidad_entradas))
print("Total a pagar: $" + str(total_pagar))
print("****************************************************")