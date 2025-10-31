# 🚗 Sistema de Gestión de Vehículos

**Fecha:** Octubre 2025
**Lenguaje:** Python  
**Paradigma:** Programación Orientada a Objetos

## 📋 Descripción

Sistema orientado a objetos para la gestión de vehículos. Calcula automáticamente impuestos y precios finales basados en características específicas de cada tipo de vehículo (automóviles y motocicletas).

## 📁 Estructura del Proyecto

├── vehiculo.py # Clase abstracta Vehiculo
├── moto.py # Clase Moto (hereda de Vehiculo)
├── automovil.py # Clase Automovil (hereda de Vehiculo)
└── main.py # Programa principal con demostración

## ▶️ Cómo Ejecutar

Ejecuta el programa principal con:

```bash
python main.py
```

## 📤 Salida Esperad

### Vehiculo: Automóvil

Marca: Toyota,
Modelo: Corolla,
Precio Base: $25000.00 COP,
Puertas: 5,
Precio Final: $26750.00 COP

### Vehiculo: Automóvil

Marca: Honda,
Modelo: Civic,
Precio Base: $22000.00 COP,
Puertas: 4,
Precio Final: $23760.00 COP

### Vehiculo: Motocicleta

Marca: Yamaha,
Modelo: MT-03,
Precio Base: $5000.00 COP,
CC: 321,
Precio Final: $5450.00 COP

### Vehiculo: Motocicleta

Marca: Honda,
Modelo: CBR125R,
Precio Base: $3000.00 COP,
CC: 125,
Precio Final: $3150.00 COP

--- Total del inventario ---

$59110.00 COP

## ⚙️ Funcionalidades

Clase Abstracta Vehiculo

- Propiedades: marca, modelo, precio_base
- Método abstracto: impuesto()
- Método: precio_final() (cálculo automático)
- Métodos: ficha() y **str**() para representación

Clase Moto

- Impuesto del 5% para motos ≤ 250cc
- Impuesto del 9% para motos > 250cc
  Clase Automovil
- Impuesto del 7% para autos de 5 puertas
- Impuesto del 8% para otros números de puertas

Programa Principal (main.py)

- Demostración con 4 vehículos de ejemplo
- Cálculo del total del inventario
- Presentación formateada de fichas técnicas

🧠 Características Técnicas

- Programación orientada a objetos
- Herencia y polimorfismo
- Encapsulación con propiedades
- Clases abstractas (ABC)
- Cálculos automáticos de impuestos
