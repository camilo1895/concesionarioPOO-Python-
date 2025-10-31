from vehiculo import Vehiculo


class Automovil(Vehiculo):

    def __init__(self,marca, modelo, precio_base, puertas: int):
        super().__init__(marca, modelo, precio_base)
        self._puertas = puertas
    
    # Getter  
    @property
    def puertas(self):
        return self._puertas

    # Método impuesto   
    def impuesto(self) -> float:
            
        if self._puertas == 5:
            return  self.precio_base * 0.07
        else:
            return self.precio_base * 0.08
            
    # Método ficha      
    def ficha(self) -> str:   
        return f"### Vehiculo: Automóvil ###\n" + \
            f"{super().ficha()},\n" + \
            f"Puertas: {self._puertas},\n" + \
            f"Precio Final: ${self.precio_final():.2f} COP\n"