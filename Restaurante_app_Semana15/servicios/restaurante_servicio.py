import json
import os
from datetime import datetime
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.ruta_usuarios = 'datos/usuarios.json'
        self.ruta_productos = 'datos/productos.json'
        self.ruta_ventas = 'datos/ventas.json'
        
        # Búsqueda O(1) con diccionarios
        self.usuarios = self.cargar_datos(self.ruta_usuarios)
        self.productos = self.cargar_datos(self.ruta_productos)
        self.ventas = self.cargar_datos(self.ruta_ventas)

    def cargar_datos(self, ruta):
        if not os.path.exists(ruta):
            return {}
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}

    def guardar_ventas(self):
        with open(self.ruta_ventas, 'w', encoding='utf-8') as f:
            json.dump(self.ventas, f, indent=4)

    def registrar_venta(self, cedula, codigo_producto):
        # Validaciones de la capa de servicio
        if cedula not in self.usuarios:
            return False, "El usuario no está registrado."
        if codigo_producto not in self.productos:
            return False, "El producto no existe."
        
        id_venta = str(len(self.ventas) + 1)
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        nueva_venta = {
            "id_venta": id_venta,
            "cedula_usuario": cedula,
            "codigo_producto": codigo_producto,
            "fecha": fecha_actual
        }
        
        self.ventas[id_venta] = nueva_venta
        self.guardar_ventas()
        
        return True, "Venta registrada exitosamente."
        
    def obtener_ventas(self):
        return list(self.ventas.values())
