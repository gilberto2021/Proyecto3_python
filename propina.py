print("Bienvenidos a la calculadora de propinas")
factura = float(input("¿Cual es el monto de tu factura?:"))
propina = int(input("¿Cual es el porcentaje de propina que quieres dejar?:"))
personas = int(input("¿Entre cuantos personas hay que dividir la factura?:"))

importe_propina = (factura * propina)/100
factura_total = importe_propina + factura

importe_por_persona = factura_total/personas

print("El importe a pagar por persona es de: " + str(importe_por_persona))