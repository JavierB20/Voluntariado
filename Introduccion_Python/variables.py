class Coche:
    # 1. Método Constructor (__init__): Se ejecuta al crear un nuevo objeto.
    #    Inicializa los atributos del objeto.
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False # Por defecto, el coche está apagado
        self.velocidad = 0

    # 2. Métodos: Definen el comportamiento del objeto.
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} se ha encendido.")
        else:
            print("El coche ya está encendido.")

    def apagar(self):
        if self.encendido and self.velocidad == 0:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        elif self.velocidad > 0:
            print("No puedes apagar el coche mientras está en movimiento.")
        else:
            print("El coche ya está apagado.")
            
    def acelerar(self, cantidad):
        if self.encendido:
            self.velocidad += cantidad
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h.")
        else:
            print("No puedes acelerar. El coche está apagado.")
            
    def frenar(self, cantidad):
        if self.velocidad > 0:
            self.velocidad -= cantidad
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"Frenando. Velocidad actual: {self.velocidad} km/h.")
        else:
            print("El coche ya está detenido.")
            
    # Método para mostrar el estado del coche
    def estado(self):
        print(f"--- Estado de: {self.marca} {self.modelo} ({self.anio}) ---")
        estado_motor = "Encendido" if self.encendido else "Apagado"
        print(f"Motor: {estado_motor}")
        print(f"Velocidad: {self.velocidad} km/h")


# --- Uso de la clase Coche ---

# Creación de objetos (instancias de la clase)
mi_coche = Coche("Toyota", "Corolla", 2022)
coche_de_ana = Coche("Honda", "Civic", 2023)

# Interactuando con el primer objeto
mi_coche.estado()
mi_coche.encender()
mi_coche.acelerar(50)
mi_coche.estado()
mi_coche.frenar(20)
mi_coche.estado()
mi_coche.frenar(30)
mi_coche.apagar()

print("\n") # Separador

# Interactuando con el segundo objeto
coche_de_ana.estado()
coche_de_ana.encender()
coche_de_ana.acelerar(80)
coche_de_ana.estado()