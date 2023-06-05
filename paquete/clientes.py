import json

class Cliente:        
    def __init__(self, nombre, codigo, direccion, telefono):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono

    def comprar_prod(self):
        nombre_producto = input("Escriba el producto a comprar: \n")
        with open("./productos.json", "r") as file:
            data = json.load(file)        
            for producto in data["productos"]:
                if producto["nombre"] == nombre_producto:
                    print(f"Has comprado una {producto['nombre']}, con estado {producto['estado']} a un valor de {producto['precio']}")
                    break
            else:
                print("No tenemos ese producto")

    def mostrar_info(self):
        print("Información del cliente:")
        print(f"Nombre: {self.nombre}")
        print(f"Codigo: {self.codigo}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
