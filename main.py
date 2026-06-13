import Funciones

def main():
    opcion = 0
    lst_identificadores = []
    lst_montos = []
    lst_distancias = []
    lst_estados = []
    lst_repartidores = []
    lst_tiempo_estimado = []
    lst_prioridades = []

    
    while opcion != 5:
        opcion = Funciones.menu(1, 5)
        if opcion == 1:
            Funciones.registrar_nuevo_pedido(lst_identificadores, lst_montos, lst_distancias, lst_estados, lst_repartidores, lst_tiempo_estimado, lst_prioridades)
        elif opcion == 2:
            Funciones.eliminar_pedido(lst_identificadores, lst_montos, lst_distancias, lst_estados, lst_repartidores, lst_tiempo_estimado, lst_prioridades)
        elif opcion == 3:
            Funciones.modificar_estado_o_repartidor(lst_identificadores, lst_montos, lst_distancias, lst_estados, lst_repartidores, lst_tiempo_estimado, lst_prioridades)
        elif opcion == 4:
            Funciones.informe_general(lst_identificadores, lst_montos, lst_distancias, lst_estados, lst_repartidores, lst_tiempo_estimado, lst_prioridades)
        elif opcion == 5:
            print("Saliendo del programa...")
    
main()