class RegistroProduccion:
    def __init__(self):
        self.registro_huevos: dict[int, dict[int, int]] = {}

    def registrar_produccion(self, codigo_pollo: int, semana: int, cantidad_huevos: int):
        if codigo_pollo not in self.registro_huevos:
            self.registro_huevos[codigo_pollo] = {}
            
        self.registro_huevos[codigo_pollo][semana] = cantidad_huevos

    def consultar_produccion_semana(self, codigo_pollo: int, semana: int) -> int:
        if codigo_pollo in self.registro_huevos:
            registro_semanal = self.registro_huevos[codigo_pollo]
            if semana in registro_semanal:
                return registro_semanal[semana]
        return 0