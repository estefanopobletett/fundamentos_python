nombre_producto = "Cuaderno"
precio_unitario = 2500
cantidad = 3
disponible = True
dinero_cliente = 10000
precio_subtotal = precio_unitario * cantidad
precio_total = precio_subtotal*0.9
print(f'''Nombre: {nombre_producto}
Precio: {precio_unitario}
Cantidad: {cantidad}
Disponible: {disponible}
Precio subtotal: {precio_subtotal}
Precio con 10% de descuento: {precio_total}
Presupuesto despues de pagar: {dinero_cliente - precio_total}
''')

print(type(nombre_producto))
print(type(precio_unitario))
print(type(disponible))


