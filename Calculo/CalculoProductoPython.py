def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (opcional, por defecto 10%).
    :return: Monto del descuento y monto final después del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final


# Llamadas a la función
monto_1 = 100  # Primera compra de 100
monto_2 = 200  # Segunda compra de 200 con 15% de descuento

# Primera llamada con el porcentaje de descuento por defecto (10%)
descuento1, total1 = calcular_descuento(monto_1)

# Segunda llamada con un porcentaje de descuento personalizado (15%)
descuento2, total2 = calcular_descuento(monto_2, 15)

# Mostrar resultados
print(f"Compra 1: Monto original = ${monto_1}, Descuento aplicado = ${descuento1:.2f}, Total a pagar = ${total1:.2f}")
print(f"Compra 2: Monto original = ${monto_2}, Descuento aplicado = ${descuento2:.2f}, Total a pagar = ${total2:.2f}")
