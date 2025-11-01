class Pollo:
    def __init__(self, codigo: int, raza: str, edad_sem: int, peso_kg: float):
        self.codigo = codigo
        self.raza = raza
        self.edad_sem = edad_sem
        self.peso_kg = peso_kg
    
    def __str__(self):
        return (f"Codigo: {self.codigo} | Raza: {self.raza} | Edad: {self.edad_sem} semamas | Peso: {self.peso_kg} kg")

    def aumentar_edad(self, semanas: int):
        if semanas > 0:
            self.edad_sem += semanas
            
    def ganar_peso(self, kg_agregados: float):
        if kg_agregados > 0:
            self.peso_kg += kg_agregados

    def perder_peso(self, kg_restados: float):
        if kg_restados > 0:
            if self.peso_kg - kg_restados < 0:
                self.peso_kg = 0.0
            else:
                self.peso_kg -= kg_restados