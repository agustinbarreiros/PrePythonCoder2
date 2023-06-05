from paquete.clientes import Cliente


cliente1 = Cliente("Robertoide", "1134", "Calle falsa 123", 1134232145)
cliente2 = Cliente("Pepa", "1234", "moron 1234", 11232144)

cliente1.comprar_prod()
cliente2.comprar_prod()
print("----------------")
cliente1.mostrar_info()
print("----------------")
cliente2.mostrar_info()