from Animal import Pollo
from Registro import RegistroProduccion

class Granja:
    def __init__(self):
        self.lista_pollos = {} 
        self.registro = RegistroProduccion() 
        self.proximo_codigo = 101

    def crear_pollo(self, raza: str, edad_sem: int, peso_kg: float):
        nuevo_pollo = Pollo(self.proximo_codigo, raza, edad_sem, peso_kg)
        self.lista_pollos[self.proximo_codigo] = nuevo_pollo
        self.proximo_codigo += 1
        return nuevo_pollo.codigo

    def ver_pollo(self, codigo: int):
        return self.lista_pollos.get(codigo)

    def actualizar_pollo(self, codigo: int, kg_a_ganar: float = 0, kg_a_perder: float = 0, semanas_a_crecer: int = 0):
        pollo = self.ver_pollo(codigo)
        if pollo:
            if semanas_a_crecer > 0:
                pollo.aumentar_edad(semanas_a_crecer)
            if kg_a_ganar > 0:
                pollo.ganar_peso(kg_a_ganar)
            if kg_a_perder > 0:
                pollo.perder_peso(kg_a_perder)
            return True
        return False
        
    def eliminar_pollo(self, codigo: int):
        if codigo in self.lista_pollos:
            del self.lista_pollos[codigo]
            if codigo in self.registro.registro_huevos:
                del self.registro.registro_huevos[codigo]
            return True
        return False
        
    def registrar_o_actualizar_produccion(self, codigo_pollo: int, semana: int, cantidad_huevos: int):
        if codigo_pollo not in self.lista_pollos:
            return False
        
        self.registro.registrar_produccion(codigo_pollo, semana, cantidad_huevos)
        return True

    def consultar_produccion(self, codigo_pollo: int, semana: int):
        return self.registro.consultar_produccion_semana(codigo_pollo, semana)

    def ver_todos_los_pollos(self):
        return self.lista_pollos.values()


def mostrar_menu():
    print("\n--- Sistema de Gestión Avícola ---")
    print("1. CRUD Pollo: Crear nuevo pollo")
    print("2. CRUD Pollo: Ver información de un pollo")
    print("3. CRUD Pollo: Ver todos los pollos")
    print("4. CRUD Pollo: Actualizar datos de un pollo")
    print("5. CRUD Pollo: Eliminar pollo")
    print("---------------------------------")
    print("6. CRUD Huevos: Registrar/Actualizar producción")
    print("7. CRUD Huevos: Consultar producción semanal")
    print("---------------------------------")
    print("0. Salir")
    return input("Elige una opción: ")

def procesar_crear_pollo(granja: Granja):
    try:
        raza = input("Raza: ")
        edad = int(input("Edad (semanas): "))
        peso = float(input("Peso (kg): "))
        codigo = granja.crear_pollo(raza, edad, peso)
        print(f"Pollo creado exitosamente con código: {codigo}")
    except ValueError:
        print("Error: Edad y peso deben ser números válidos.")

def procesar_ver_pollo(granja: Granja):
    try:
        codigo = int(input("Introduce el código del pollo a buscar: "))
        pollo = granja.ver_pollo(codigo)
        print(f"Información: {pollo}" if pollo else f"Error: No se encontró el pollo con código {codigo}.")
    except ValueError:
        print("Error: El código debe ser un número entero.")

def procesar_actualizar_pollo(granja: Granja):
    try:
        codigo = int(input("Código del pollo a actualizar: "))
        semanas = int(input("Semanas a aumentar (0 si no aplica): "))
        ganar = float(input("Kg a ganar (0 si no aplica): "))
        perder = float(input("Kg a perder (0 si no aplica): "))

        if granja.actualizar_pollo(codigo, ganar, perder, semanas):
            print(f"Datos del pollo {codigo} actualizados.")
            print(f"Nuevo estado: {granja.ver_pollo(codigo)}")
        else:
            print(f"Error: Pollo con código {codigo} no encontrado.")

    except ValueError:
        print("Error: Valores inválidos. Asegúrate de usar números.")

def procesar_eliminar_pollo(granja: Granja):
    try:
        codigo = int(input("Código del pollo a eliminar: "))
        print(f"Pollo con código {codigo} eliminado." if granja.eliminar_pollo(codigo) else f"Error: Pollo con código {codigo} no encontrado.")
    except ValueError:
        print("Error: El código debe ser un número entero.")

def procesar_registrar_produccion(granja: Granja):
    try:
        codigo = int(input("Código de la gallina: "))
        semana = int(input("Número de semana: "))
        huevos = int(input("Cantidad de huevos producidos: "))
        
        print(f"Producción registrada/actualizada." if granja.registrar_o_actualizar_produccion(codigo, semana, huevos) else f"Error: El pollo con código {codigo} no existe.")
    except ValueError:
        print("Error: Los valores deben ser números enteros válidos.")

def procesar_consultar_produccion(granja: Granja):
    try:
        codigo = int(input("Código de la gallina: "))
        semana = int(input("Número de semana a consultar: "))
        
        produccion = granja.consultar_produccion(codigo, semana)
        
        if produccion > 0:
            print(f"El pollo {codigo} produjo {produccion} huevos en la Semana {semana}.")
        elif granja.ver_pollo(codigo):
            print(f"El pollo {codigo} produjo {produccion} huevos (o no hay registro) en la Semana {semana}.")
        else:
            print(f"Error: Pollo con código {codigo} no encontrado.")
    except ValueError:
        print("Error: El código y la semana deben ser números enteros.")


def main():
    granja = Granja()
    
    granja.crear_pollo("Leghorn", 5, 2.5)
    granja.crear_pollo("Rhode Island Red", 6, 2.8)
    granja.registrar_o_actualizar_produccion(101, 1, 30)
    
    while True:
        opcion = mostrar_menu()
        
        match opcion:
            case '1':
                procesar_crear_pollo(granja)
            case '2':
                procesar_ver_pollo(granja)
            case '3':
                pollos = list(granja.ver_todos_los_pollos())
                if not pollos:
                    print("No hay pollos registrados en la granja.")
                    continue
                print("\n--- LISTA DE POLLOS REGISTRADOS ---")
                for pollo in pollos:
                    print(f"- {pollo}")
                print("---------------------------------")
            case '4':
                procesar_actualizar_pollo(granja)
            case '5':
                procesar_eliminar_pollo(granja)
            case '6':
                procesar_registrar_produccion(granja)
            case '7':
                procesar_consultar_produccion(granja)
            case '0':
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            case _:
                print("Opción no válida. Por favor, elige un número del menú.")

if __name__ == "__main__":

    main()
