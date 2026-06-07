# Funciom Menu | Mirko Wesner

lst_identificadores = []
lst_montos = []
lst_distancias = []
lst_estados = []
lst_repartidores = []
lst_tiempo_estimado = []
lst_prioridades = []

#funcion para mostrar el menu de opciones al usuario y validar la opción ingresada
def menu(desde, hasta):
    print("1: Registrar nuevo pedido")
    print("2: Eliminar pedido")
    print("3: Modificar estado o repartidor")
    print("4: Informe general")
    print("5: Salir")
    print("--------------------------------------------\n")
    opcion = int(input("Ingrese una opción: "))
    while opcion < desde or opcion > hasta:
        print("Error, la opción ingresada no es válida. Pruebe nuevamente.")
        opcion = int(input("Ingrese una opción: "))
    return opcion

#el usuario ingresa el identificador del pedido
def identificador_del_pedido():
    identificador =input("Ingrese el identificador del pedido: ")
    while len(identificador) < 4 or len(identificador) > 10:
        print("Error, el identificador debe contener entre 4 y 10 caracteres. Pruebe de nuevo.")
        identificador = input("Ingrese el identificador del pedido: ")
    lst_identificadores.append(identificador)

#el usuario ingresa el monto total del pedido
def monto_total_pedido():
    monto_total = float(input("Ingrese el monto total del pedido: "))
    while monto_total < 0:
        print("Error, el monto total debe ser un número positivo. Intente de nuevo.")
        monto_total = float(input("Ingrese el monto total del pedido: "))
    lst_montos.append(monto_total)

#el usuario ingresa la distancia estimada al destino
def distancia_estimada_al_destino():
    distancia_estimada = float(input("Ingrese la distancia estimada al destino (Kilometros): "))
    while distancia_estimada < 0 or distancia_estimada > 20:
        print("Error, la distancia estimada debe ser un número positivo o que no supere los 20 kilómetros. Intente nuevamente.")
        distancia_estimada = float(input("Ingrese la distancia estimada al destino (Kilometros): "))
    lst_distancias.append(distancia_estimada)
    
#el usuario ingresa el estado operativo del pedido
def estado_operativo():
    print("1: Preparación")
    print("2: En reparto")
    print("3: Entregado")
    print("4: Cancelado")
    estado_operativo = int(input("Ingrese el estado operativo del pedido: "))
    while estado_operativo < 1 or estado_operativo > 4:
        print("Error, la opcion ingresada no es válida. Intente nuevamente.")
        estado_operativo = int(input("Ingrese el estado operativo del pedido: "))
    lst_estados.append(estado_operativo)

#el usuario ingresa el nombre del repartidor asignado al pedido
def repartidor_asignado():
    repartidor = input("Ingrese el nombre del repartidor asignado al pedido: ")
    lst_repartidores.append(repartidor)

#el usuario ingresa el tiempo estimado de entrega del pedido
def tiempo_estimado_de_entrega():
    tiempo_estimado = int(input("Ingrese el tiempo estimado de la entrega (Minutos): "))
    while tiempo_estimado < 0:
        print("Error, el tiempo estimado de entrega tiene que ser un número positivo. Pruebe de nuevo.")
        tiempo_estimado = int(input("Ingrese el tiempo estimado de la entrega (Minutos): "))
    lst_tiempo_estimado.append(tiempo_estimado)

#el usuario ingresa la prioridad del pedido
def prioridad_del_pedido():
    print("1: Normal")
    print("2: Alta")
    print("3: Urgente")
    prioridad = int(input("Ingrese la prioridad del pedido: "))
    while prioridad < 1 or prioridad > 3:
        print("Error, la prioridad del pedido debe ser un número entre 1 y 3. Intente nuevammente. ")
        prioridad = int(input("Ingrese la prioridad del pedido: "))
    lst_prioridades.append(prioridad)

#el usuario ingresa los datos para registrar un nuevo pedido
def registrar_nuevo_pedido():
    identificador_del_pedido()
    monto_total_pedido()
    distancia_estimada_al_destino()
    estado_operativo()
    repartidor_asignado()
    tiempo_estimado_de_entrega()
    prioridad_del_pedido()

#el usuario ingresa el identificador del pedido a eliminar, se valida que el identificador exista y se le pide confirmación al usuario para eliminar el pedido
def eliminar_pedido():
    confirmacion = False
    if len(lst_identificadores) == 0:
        print("Error, no hay pedidos registrados. No se puede eliminar ningún pedido.")
    else:
        print(lst_identificadores)
        identificador = input("Ingrese el identificador del pedido a eliminar: ")
        while identificador not in lst_identificadores:
            print("Error, el identificador ingresado no es válido. Intente de nuevo.")
            identificador = input("Ingrese el identificador del pedido a eliminar: ")
        
        print("Está seguro que desea eliminar el pedido con el identificador", identificador, "?")
        print("1: Si")
        print("2: No")
        opcion = int(input("Ingrese una opción: "))
        while opcion < 1 or opcion > 2:
            print("Error, la opción ingresada no es válida. Intente de nuevo.")
            opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            confirmacion = True
        if confirmacion == True:
            i = lst_identificadores.index(identificador)
            if lst_estados[i] != 4:
                print("Error, no se puede eliminar un pedido que no se encuentra cancelado. Cambie el estado operativo del pedido a cancelado para poder eliminarlo.")
            else:
                lst_identificadores.pop(i)
                lst_montos.pop(i)
                lst_distancias.pop(i)
                lst_estados.pop(i)
                lst_repartidores.pop(i)
                lst_tiempo_estimado.pop(i)
                lst_prioridades.pop(i)
                print("El pedido", identificador, "fue eliminado exitosamente.")

#el usuario ingresa el identificador del pedido a modificar, se valida que el identificador exista y se le pide al usuario que elija si desea modificar el estado operativo o el repartidor asignado al pedido
def modificar_estado_o_repartidor():
    if len(lst_identificadores) == 0:
        print("Error, no hay pedidos registrados. No se puede modificar ningún pedido.")   
    else:
        print(lst_identificadores)
        identificador = input("Ingrese el identificador del pedido a modificar: ")
        while identificador not in lst_identificadores:
            print("Error, el identificador ingresado no es válido. Intente de nuevo.")
            identificador = input("Ingrese el identificador del pedido a modificar: ")
        print("¿Qué desea modificar?")
        print("1: Estado operativo")
        print("2: Repartidor asignado")
        opcion = int(input("Ingrese una opción: "))
        while opcion < 1 or opcion > 2:
            print("Error, la opción ingresada no es válida. Intente de nuevo.")
            opcion = int(input("Ingrese una opción: "))
        i = lst_identificadores.index(identificador)
        if opcion == 1:
            estado_operativo()
            lst_estados[i] = lst_estados[-1]
            lst_estados.pop(-1)
        if opcion == 2:
            repartidor_asignado()
            lst_repartidores[i] = lst_repartidores[-1]
            lst_repartidores.pop(-1)

#funcion para ordenar los pedidos por prioridad, en caso de que dos pedidos tengan la misma prioridad, se ordenan por distancia estimada al destino
def ordenamiento_pedidos():
    for i in range(len(lst_prioridades)-1):
        indice_maximo = i
        for j in range(i+1, len(lst_prioridades)):
            if lst_prioridades[j] > lst_prioridades[indice_maximo]:
                indice_maximo = j
            elif lst_prioridades[j] == lst_prioridades[indice_maximo]:
                if lst_distancias[j] < lst_distancias[indice_maximo]:
                    indice_maximo = j
        
        lst_prioridades[i], lst_prioridades[indice_maximo] = lst_prioridades[indice_maximo], lst_prioridades[i]
        lst_tiempo_estimado[i], lst_tiempo_estimado[indice_maximo] = lst_tiempo_estimado[indice_maximo], lst_tiempo_estimado[i]
        lst_identificadores[i], lst_identificadores[indice_maximo] = lst_identificadores[indice_maximo], lst_identificadores[i]
        lst_montos[i], lst_montos[indice_maximo] = lst_montos[indice_maximo], lst_montos[i]
        lst_distancias[i], lst_distancias[indice_maximo] = lst_distancias[indice_maximo], lst_distancias[i]
        lst_estados[i], lst_estados[indice_maximo] = lst_estados[indice_maximo], lst_estados[i]
        lst_repartidores[i], lst_repartidores[indice_maximo] = lst_repartidores[indice_maximo], lst_repartidores[i]

#funcion para mostrar el informe general de pedidos, ordenados por prioridad
def informe_general():
    ordenamiento_pedidos()
    
    if len(lst_identificadores) == 0:
        print("---------------------------------------------")
        print("No hay pedidos registrados.")
        print("---------------------------------------------")
    else:
        for i in range(len(lst_identificadores)):
            print("Identificador del pedido:", lst_identificadores[i])
            print("Monto total del pedido:", lst_montos[i])
            print("Distancia estimada al destino:", lst_distancias[i], "km")
            print("Estado operativo del pedido:", lst_estados[i])
            print("Repartidor asignado al pedido:", lst_repartidores[i])
            print("Tiempo estimado de entrega:", lst_tiempo_estimado[i], "minutos")
            print("Prioridad del pedido:", lst_prioridades[i])
            print("---------------------------------------------")