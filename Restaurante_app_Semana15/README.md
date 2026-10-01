# Proyecto: restaurante_app - Semana 15

Este proyecto corresponde a la actividad de la semana 15 de la asignatura de Programación Orientada a Objetos.

## Evolución del Proyecto (Semana 15)
Para esta entrega, se ha integrado una nueva sección de **Ventas** manteniendo la arquitectura modular trabajada en semanas anteriores. 

### Conceptos Fundamentales de Manejo de Eventos
La interfaz principal implementa el manejo de eventos a través de un botón ("Registrar Venta"). Este botón utiliza el atributo `command=` para enlazar su ejecución a una función callback (`callback_registrar_venta`). 

Esta función actúa como intermediaria: recolecta los datos seleccionados por el usuario y le delega el procesamiento y las reglas de negocio a la clase `RestauranteServicio`. De esta forma, se asegura que la interfaz no manipule directamente los archivos.

### Persistencia
La persistencia de las nuevas transacciones se almacena en el archivo `datos/ventas.json`, el cual es gestionado únicamente por la capa de servicios, manteniendo la búsqueda con diccionarios para la validación de productos y usuarios.

### Ejecución
Para iniciar el sistema, simplemente ejecute:
```bash
python main.py
```
*(Asegúrese de contar con los recursos visuales en la carpeta `assets/` para la correcta visualización de la interfaz).*
