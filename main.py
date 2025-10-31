# Crear la lista de vehículos
from automovil import Automovil
from moto import Moto


vehiculos = [
    # Autos (uno de 5 puertas y otro de 4 puertas)
    Automovil("Toyota", "Corolla", 25000, 5),
    Automovil("Honda", "Civic", 22000, 4),
    
    # Motos (una de ≤ 250cc y otra de > 250cc)
    Moto("Yamaha", "MT-03", 5000, 321),
    Moto("Honda", "CBR125R", 3000, 125)
]

# Calcular el total del inventario
total_inventario = 0

# Mostrar la información de cada vehículo
for vehiculo in vehiculos:
    total_inventario += vehiculo.precio_final()
    print(vehiculo.ficha())

print("\n--- Total del inventario ---")
print(f"\n${total_inventario:.2f} COP\n")