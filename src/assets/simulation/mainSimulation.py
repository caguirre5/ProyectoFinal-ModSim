# Importa las clases Animal y Terreno (asumiendo que están definidas en archivos separados)
from animal import Animal
from terrain import Terreno
import random

# Instancia de la clase Leon (Animal)
animal = Animal(
    "León Africano",
    8,  # Edad
    "Macho",  # Género
    180,  # Peso en kg
    200,  # Tamaño en cm
    60,  # Velocidad en m/s
    0.7,  # Capacidad de reproducción (0 - 1)
    8,  # Tasa de alimentación en kg/día
    1,  # Dieta (por ejemplo, 1 para Carnívora)
    12,  # Expectativa de vida en años
    3,  # Comportamiento Social (por ejemplo, 3 para Manada)
    [],  # Depredadores
    [4, 5, 6],  # Presas
    0.8,  # Nivel de Agresividad (0 - 1)
    0.3,  # Capacidad de Movimiento (0 - 1)
    0.85,  # Resistencia a Enfermedades (0 - 1)
    4,  # Fertilidad (promedio de crías)
    15,  # Longevidad en años
)

# Instancia de la clase Entorno
entorno = Terreno(
    1,  # Tipo de terreno
    1,  # Clima
    4,  # Estaciones
    3,  # Disponibilidad de alimentos (por ejemplo, Abundante)
    0.8,  # Riesgos Ambientales
    2,  # Topografía (por ejemplo, Montañoso)
    0.8,  # Vegetación
    0.6,  # Humedad
    0.2,  # Contaminación
    0.9,  # Calidad del agua
    800,  # Nivel de precipitación
    1500,  # Nivel de altitud
    0.7,  # Calidad del suelo
    25,  # Rango de temperaturas
    0.6,  # Razón día/noche
    300,  # Nivel de radiación solar
    40,  # Nivel de ruido ambiental
    0.2,  # Nivel de polución lumínica
    0.5,  # Razón depredadores/presas
    0.8  # Calidad del hábitat
)


def calcularPeso(animal, entorno):
    # El cambio de peso del animal puede depender de la disponibilidad de alimentos y la calidad del hábitat.
    # Una fórmula simple podría ser:
    variacion_peso = (entorno.disponibilidadAlimentos *
                      0.2 - 0.1) * random.uniform(0.8, 1.2)
    peso_actual = animal.peso
    nuevo_peso = peso_actual + variacion_peso
    return nuevo_peso


def calcularNivelHidratacion(animal, entorno):
    # El nivel de hidratación puede depender de la calidad del agua en el entorno y la humedad.
    # Una fórmula podría ser una combinación ponderada de estos factores:
    nivel_hidratacion = (entorno.calidadAgua * 0.6 +
                         entorno.humedad * 0.4) * random.uniform(0.8, 1.2)
    return nivel_hidratacion


def calcularNivelEnergia(animal, entorno):
    # El nivel de energía del animal puede depender de su actividad, la disponibilidad de alimentos y la temperatura.
    # Una fórmula podría ser:
    nivel_actividad = random.uniform(0.8, 1.2)
    disponibilidad_alimentos = entorno.disponibilidadAlimentos
    temperatura_ambiente = entorno.rangoTemperaturas
    nivel_energia = (nivel_actividad * 0.4 + disponibilidad_alimentos *
                     0.4 - (temperatura_ambiente - 25) * 0.05)
    return nivel_energia


def calcularTemperaturaCorporal(animal, entorno):
    # La temperatura corporal del animal podría depender de la temperatura ambiente y la tasa de actividad.
    # Una fórmula podría ser:
    temperatura_ambiente = entorno.rangoTemperaturas
    nivel_actividad = random.uniform(0.8, 1.2)
    temperatura_corporal = 38 + \
        (temperatura_ambiente - 25) * 0.1 + (nivel_actividad - 1) * 0.2
    return temperatura_corporal


def calcularRespiracion(animal, entorno):
    # La tasa de respiración del animal podría depender de la altitud y la temperatura ambiente.
    # Una fórmula podría ser:
    altitud = entorno.nivelAltitud
    temperatura_ambiente = entorno.rangoTemperaturas
    tasa_respiracion = 10 + (temperatura_ambiente - 20) * \
        0.2 - (altitud - 1000) * 0.1
    return tasa_respiracion


def calcularSaturacionOxigeno(animal, entorno):
    # La saturación de oxígeno podría depender de la tasa de respiración del animal.
    # Una fórmula podría ser:
    tasa_respiracion = calcularRespiracion(animal, entorno)
    saturacion_oxigeno = 100 - (tasa_respiracion * 0.1)
    return saturacion_oxigeno


def calcularFrecuenciaCardiacaIdeal(animal):
    # La frecuencia cardíaca normal en reposo de un león puede variar, pero
    # en promedio, se estima en alrededor de 60-90 latidos por minuto.
    frecuenciaCardiacaEnReposo = random.randint(60, 90)

    # Ajustamos la frecuencia cardíaca en función de la edad del león.
    # Los leones más jóvenes tienden a tener frecuencias cardíacas más altas.
    factorEdad = min(1, animal.edad / 10)

    # Ajustamos la frecuencia cardíaca en función de la agresividad.
    # Los leones más agresivos pueden tener frecuencias cardíacas ligeramente más altas.
    factorAgresividad = 1 + (animal.nivelAgresividad - 0.5) * 0.1

    # Ajustamos la frecuencia cardíaca en función del comportamiento social.
    # Los leones que viven en manadas pueden tener frecuencias cardíacas más bajas.
    factorComportamientoSocial = 1 - (animal.comportamientoSocial - 1) * 0.1

    # Calculamos la frecuencia cardíaca ideal.
    frecuenciaCardiacaIdeal = frecuenciaCardiacaEnReposo * \
        factorEdad * factorAgresividad * factorComportamientoSocial

    return round(frecuenciaCardiacaIdeal)


def simularEpoca(poblacion, entorno):

    for specimen in poblacion:

        # Realiza cálculos y actualizaciones para cada variable de estado
        FrecuenciaCardiaca = calcularFrecuenciaCardiacaIdeal(specimen)


# Incializar poblacion
n_poblacion = 10
poblacion = []


for i in range(n_poblacion):
    nombre = "León Africano"
    genero = random.randint(0, 1)
    expectativa_vida = 12
    capacidad_reproduccion = 0.7
    tasa_alimentacion = 8
    dieta = 1
    comportamiento_social = 3
    nivel_agresividad = 0.8
    resistencia_enfermedades = 0.85
    fertilidad_promedio = 4

    poblacion.append(Animal(
        nombre,
        random.randint(0, expectativa_vida),  # Edad
        genero,  # Género
        random.randint(150, 250) if genero == 0 else random.randint(
            128, 182),  # Peso en kg
        random.randint(170, 250) if genero == 0 else random.randint(
            140, 175),  # Tamaño en cm
        random.randint(50, 60),  # Velocidad en km/h
        capacidad_reproduccion,  # Capacidad de reproducción (0 - 1)
        tasa_alimentacion,  # Tasa de alimentación en kg/día
        dieta,  # Dieta (por ejemplo, 1 para Carnívora)
        expectativa_vida,  # Expectativa de vida en años
        # Comportamiento Social (por ejemplo, 3 para Manada)
        comportamiento_social,
        [],  # Depredadores
        [],  # Presas
        nivel_agresividad,  # Nivel de Agresividad (0 - 1)
        resistencia_enfermedades,  # Resistencia a Enfermedades (0 - 1)
        fertilidad_promedio,  # Fertilidad (promedio de crías)
    ))

# Simulación de 100 épocas
for epoca in range(1, 101):
    simularEpoca(animal, entorno)

# Ejemplo de uso:
frecuenciaCardiacaIdeal = calcularFrecuenciaCardiacaIdeal(animal)
print(
    f"Frecuencia Cardíaca Ideal: {frecuenciaCardiacaIdeal} latidos por minuto.")
