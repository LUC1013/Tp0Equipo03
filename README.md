# Fast Delivery

Este proyecto es un programa en Python creado para organizar y controlar los envíos de un servicio de delivery. Funciona a través de un menú de opciones sencillo, gestionando la informacion con listas paralelas.

---
Link al Github: https://github.com/LUC1013/Tp0Equipo03
---

## Objetivo

El objetivo del presente proyecto es desarrollar una herramienta interactiva que permita administrar pedidos, mantener información sincronizada y generar informes de análisis para apoyar la toma de decisiones de los coordinadores logísticos

---

## Funcionalidades

Las principales funcionalidades implementadas son:

* Registro de nuevos pedidos.
* Baja de pedidos.
* Modificación de pedidos.
* Generación de informes.

---

## Requisitos

Para ejecutar el proyecto se requiere:

* Python 3.x

---

## Instalación

1. Descargar o clonar el proyecto.
2. Abrir una terminal.
3. Ubicarse en la carpeta del proyecto.

---

## Ejecución

Ejecutar el siguiente comando:


"python main.py"


---

## Estructura del Proyecto

FastDelivery/
│
├── Funciones.py
├── main.py
└── README.md


---

## Organización del Código

### main.py

Contiene el programa principal y controla el flujo general de ejecución.

### Funciones.py

Contiene todas las funciones del programa.

---

## Tecnologías Utilizadas

* Python

---

## Conceptos de Programación Aplicados

Durante el desarrollo se utilizaron los siguientes conceptos:

* Variables
* Entrada y salida de datos
* Estructuras condicionales
* Ciclos repetitivos
* Funciones
* Listas
* Matrices
* Modularización
* Validación de datos

---

## Integrantes del Equipo

* Mirko Wesner
* Lucio Formia
* Martin Cywiner
* Valentino Silva
* Francisco Fernandez

---

## Distribución de Tareas

| Integrante          | Responsabilidad |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirko Wesner        | Menú principal (`menu`), Ordenamiento de pedidos (`ordenamiento_pedidos`)                                                                                     |
| Francisco Fernandez | Identificador del pedido (`identificador_del_pedido`), Estado operativo (`estado_operativo`), Tiempo estimado de entrega (`tiempo_estimado_de_entrega`)       |
| Martin Cywiner      | Monto total del pedido (`monto_total_pedido`), Prioridad del pedido (`prioridad_del_pedido`), Modificar estado o repartidor (`modificar_estado_o_repartidor`) |
| Valentin Spaho      | Distancia estimada al destino (`distancia_estimada_al_destino`), Repartidor asignado (`repartidor_asignado`)                                                  |
| Lucio Formia        | Eliminar pedido (`eliminar_pedido`), Informe general (`informe_general`)                                                                                      |

---

## Decisiones de Diseño

* Se utilizaron listas paralelas para almacenar la información.
* Principalmente nos centramos en la modularizacion del codigo.
* Aplicamos logica de algoritmia en funciones como busqueda secuencial y ordenamiento

---
## Licencia

Proyecto académico desarrollado para la asignatura PENSAMIENTO COMPUTACIONAL, ALGORITMIA Y PROGRAMACION
Su finalidad es exclusivamente educativa.
