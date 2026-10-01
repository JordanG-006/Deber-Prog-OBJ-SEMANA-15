from dataclasses import dataclass

@dataclass
class Venta:
    id_venta: str
    cedula_usuario: str
    codigo_producto: str
    fecha: str
