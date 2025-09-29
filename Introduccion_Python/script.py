# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------
# EJEMPLOS DE PYTHON PARA CONFERENCIA
# Este archivo contiene ejemplos prácticos de los conceptos básicos de Python.
# ---------------------------------------------------------------------------

print("### 1. Variables y Tipado Dinámico ###\n")

# Ejemplo 1: Asignación básica de variables
nombre_curso = "Python Total"  # String (cadena de texto)
participantes = 150            # Integer (entero)
precio = 19.99                 # Float (decimal)
es_presencial = False          # Boolean (booleano)

print(f"Curso: {nombre_curso}, Precio: ${precio}")
print(f"Participantes: {participantes}, Es presencial: {es_presencial}")

# Ejemplo 2: El tipado es dinámico, una variable puede cambiar de tipo
valor = "Soy un texto"
print(f"El valor es '{valor}' y su tipo es {type(valor)}")
valor = 100
print(f"Ahora el valor es {valor} y su tipo es {type(valor)}")

# Ejemplo 3: Impresión de múltiples variables
print("\n----------------------------------------\n")


print("### 2. Operadores ###\n")

a = 10
b = 3

# Ejemplo 1: Operadores Aritméticos
print(f"Suma: 10 + 3 = {a + b}")
print(f"Resta: 10 - 3 = {a - b}")
print(f"Multiplicación: 10 * 3 = {a * b}")
print(f"División: 10 / 3 = {a / b}")
print(f"División Entera: 10 // 3 = {a // b}")
print(f"Módulo (Residuo): 10 % 3 = {a % b}")
print(f"Potencia: 10 ** 3 = {a ** b}")

# Ejemplo 2: Operadores Relacionales (devuelven True o False)
print(f"\n¿Es 10 > 3?  {a > b}")
print(f"¿Es 10 <= 3? {a <= b}")
print(f"¿Es 10 == 10? {a == 10}")
print(f"¿Es 10 != 3?  {a != b}")

# Ejemplo 3: Operadores Lógicos
edad = 25
es_estudiante = True
print(f"\n¿Tiene 25 años Y es estudiante? {edad == 25 and es_estudiante}")
print(f"¿Tiene más de 30 O es estudiante? {edad > 30 or es_estudiante}")
print(f"¿NO es estudiante? {not es_estudiante}")

print("\n----------------------------------------\n")


print("### 3. Condicionales (if, elif, else) ###\n")

# Ejemplo 1: if/else simple
calificacion = 65
if calificacion >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")

# Ejemplo 2: if/elif/else
hora = 14
if hora < 12:
    print("Buenos días")
elif 12 <= hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")

# Ejemplo 3: Condicional anidado
es_mayor_de_edad = True
tiene_licencia = False
if es_mayor_de_edad:
    print("Es mayor de edad.")
    if tiene_licencia:
        print("Puede conducir.")
    else:
        print("Pero no tiene licencia para conducir.")
else:
    print("No es mayor de edad, no puede conducir.")

print("\n----------------------------------------\n")


print("### 4. Bucles (while y for) ###\n")

# Ejemplo 1: Bucle `while`
contador = 5
print("Cuenta regresiva con while:")
while contador > 0:
    print(contador)
    contador -= 1 # Equivalente a contador = contador - 1
print("¡Despegue!")

# Ejemplo 2: Bucle `for` iterando sobre una lista
nombres = ["Ana", "Luis", "Marta"]
print("\nLista de nombres:")
for nombre in nombres:
    print(f"- {nombre}")

# Ejemplo 3: Bucle `for` con la función `range`
print("\nTabla de multiplicar del 5:")
for i in range(1, 11): # Genera números del 1 al 10
    print(f"5 x {i} = {5 * i}")

print("\n----------------------------------------\n")


print("### 5. Listas, Tuplas y Diccionarios ###\n")

# --- Listas ---
print("--- Listas (mutables) ---")
# Ejemplo 1: Creación y acceso a elementos
frutas = ["manzana", "banana", "cereza", "naranja", "kiwi"]
print(f"Lista original: {frutas}")
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Ejemplo 2: Métodos de listas
frutas.append("uva") # Añade al final
print(f"Después de append('uva'): {frutas}")

frutas.insert(2, "mango") # Inserta en una posición específica
print(f"Después de insert(2, 'mango'): {frutas}")

fruta_eliminada = frutas.pop() # Elimina y devuelve el último elemento
print(f"Fruta eliminada con pop(): {fruta_eliminada}, Lista ahora: {frutas}")

frutas.remove("banana") # Elimina la primera ocurrencia de un valor
print(f"Después de remove('banana'): {frutas}")

# Ejemplo 3: Slicing (sublistas)
primeras_dos = frutas[0:2] # Elementos desde el índice 0 hasta el 2 (sin incluir el 2)
print(f"Primeras dos frutas (slicing): {primeras_dos}")


# --- Tuplas ---
print("\n--- Tuplas (inmutables) ---")
# Ejemplo 1: Creación y acceso
coordenadas = (10.5, -75.3)
print(f"Tupla de coordenadas: {coordenadas}")
print(f"Latitud: {coordenadas[0]}")

# Ejemplo 2: Inmutabilidad (esto daría error si se descomenta)
# coordenadas[0] = 11.0 # TypeError: 'tuple' object does not support item assignment

# Ejemplo 3: Desempaquetado de tuplas
lat, lon = coordenadas
print(f"Latitud (desempaquetada): {lat}, Longitud: {lon}")


# --- Diccionarios ---
print("\n--- Diccionarios (pares clave:valor) ---")
# Ejemplo 1: Creación y acceso a valores por su clave
alumno = {
    "nombre": "Carlos",
    "edad": 22,
    "curso": "Ingeniería de Software",
    "activo": True
}
print(f"Diccionario original: {alumno}")
print(f"El nombre del alumno es: {alumno['nombre']}")

# Ejemplo 2: Añadir, modificar y eliminar
alumno["universidad"] = "Universidad Politécnica" # Añadir nuevo par
print(f"Diccionario con universidad: {alumno}")

alumno["edad"] = 23 # Modificar un valor existente
print(f"Diccionario con edad modificada: {alumno}")

curso_eliminado = alumno.pop("curso") # Elimina un par por su clave
print(f"Curso eliminado: {curso_eliminado}, Diccionario final: {alumno}")

# Ejemplo 3: Iterar sobre un diccionario
print("\nClaves y valores del diccionario:")
for clave, valor in alumno.items():
    print(f"- {clave.capitalize()}: {valor}")

print("\n----------------------------------------\n")


print("### 6. Programación Orientada a Objetos (POO) ###\n")

# Ejemplo: Una clase sencilla para representar un Coche

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