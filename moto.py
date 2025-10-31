from vehiculo import Vehiculo


class Moto(Vehiculo):


    def __init__(self, marca, modelo, precio_base, cc: int):
        super().__init__(marca, modelo, precio_base)
        self._cc = cc

    # Getter
    @property
    def cc(self):
        return self._cc
    
    # Método impuesto
    def impuesto(self) -> float:
        if self._cc <= 250:
            return self.precio_base * 0.05
        else:
            return self.precio_base * 0.09

    # Método ficha    
    def ficha(self) -> str:
        return f"### Vehiculo: Motocicleta ###\n" + \
            f"{super().ficha()},\n" + \
            f"CC: {self._cc},\n" + \
            f"Precio Final: ${self.precio_final():.2f} COP\n"
    