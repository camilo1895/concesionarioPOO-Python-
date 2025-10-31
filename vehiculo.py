from abc import ABC, abstractmethod

class Vehiculo (ABC):
    def __init__(self, marca, modelo, precio_base):
        self._marca = marca # Protegido (convención)
        self._modelo = modelo # Protegido (convención)
        self._precio_base = max(precio_base, 0) # Protegido (convención)

    # Getter
    @property
    def marca(self):
        return self._marca

    # Getter
    @property
    def modelo(self):
        return self._modelo

    # Getter
    @property
    def precio_base(self):
        return self._precio_base

    # Metodo abstracto impuesto
    @abstractmethod
    def impuesto(self) -> float:
        pass

    # Método precio final
    def precio_final(self) -> float:
        return self._precio_base + self.impuesto()

    # Método ficha
    def ficha(self) -> str:
        return f"Marca: {self._marca},\n" + \
        f"Modelo: {self._modelo},\n" + \
        f"Precio Base: ${self._precio_base:.2f} COP"

    # Método str
    def __str__(self) -> str:
        return f"{self._marca} {self._modelo} - Precio Base: ${self._precio_base:.2f} COP"