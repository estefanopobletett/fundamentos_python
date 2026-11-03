nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = int(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))
disponible = True
dinero_cliente = int(input("Ingrese el dinero del cliente: "))

precio_subtotal = precio_unitario * cantidad
descuento = precio_subtotal*0.10
precio_total = precio_subtotal - descuento
print(f'''Nombre: {nombre_producto}
Precio: {precio_unitario}
Cantidad: {cantidad}
Disponible: {disponible}
Precio subtotal: {precio_subtotal}
descuento del 10%: {descuento}
Precio con 10% de descuento: {precio_total}
Presupuesto despues de pagar: {dinero_cliente - precio_total}
''')
print(type(nombre_producto))
print(type(precio_unitario))
print(type(disponible))

