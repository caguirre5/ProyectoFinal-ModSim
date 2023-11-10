# Importa las clases Animal y Terreno (asumiendo que están definidas en archivos separados)
from animal import Animal
from terrain import Terreno
import random

# Instancia de la clase Entorno
entorno = Terreno(
    4,  # Tipo de terreno (Montaña)
    4,  # Clima (Frío)
    4,  # Estaciones (Frío con estaciones marcadas)
    3,  # Disponibilidad de alimentos (Escasa)
    0.8,  # Riesgos Ambientales (Puedes ajustar según la situación)
    2,  # Topografía (Montañoso)
    0.2,  # Vegetación (Baja)
    0.2,  # Humedad (Baja)
    0.2,  # Contaminación (Baja)
    0.9,  # Calidad del agua (Alta)
    400,  # Nivel de precipitación (Puedes ajustar según la situación)
    3500,  # Nivel de altitud (Montañas de gran altitud)
    0.4,  # Calidad del suelo (Puede ser baja en zonas de hielo)
    -20,  # Rango de temperaturas (Puedes ajustar según la situación)
    0.4,  # Razón día/noche (Puede haber noches largas en zonas frías)
    200,  # Nivel de radiación solar (Puede ser bajo en zonas frías)
    20,  # Nivel de ruido ambiental (Puedes ajustar según la situación)
    0.2,  # Nivel de polución lumínica (Puede ser bajo en zonas frías)
    0.5,  # Razón depredadores/presas (Puedes ajustar según la situación)
    0.8
)


def calcularPeso(animal, entorno):
    # El cambio de peso del animal puede depender de la disponibilidad de alimentos y la calidad del hábitat.
    # Una fórmula simple podría ser:
    cambio_peso = ((animal.tasaAlimentacion * entorno.disponibilidadAlimentos /
                   100) - animal.tasaAlimentacion) * 0.01 * animal.peso

    nuevo_peso = animal.peso + cambio_peso
    return nuevo_peso


def calcularNivelHidratacion(animal, entorno):
    # Establece una tasa de cambio gradual para el nivel de hidratación.
    # Puedes ajustar este valor según la velocidad de cambio deseada.
    tasa_cambio = 0.05

    # Calcula el cambio en función de la calidad del agua, la humedad y un valor aleatorio.
    cambio = (entorno.calidadAgua * 0.6 + entorno.humedad * 0.4) * \
        random.uniform(0.8, 1.2)

    # Limita el cambio para que esté dentro del rango [0, 1].
    # Evita que el nivel supere 1.
    cambio = max(0, min(1 - animal.nivelHidratacion, cambio))

    # Actualiza el nivel de hidratación con el cambio gradual.
    nivelHidratacion = animal.nivelHidratacion
    nivelHidratacion += cambio * tasa_cambio

    # Asegúrate de que el nivel de hidratación permanezca en el rango [0, 1].
    nivelHidratacion = max(0, min(1, nivelHidratacion))

    return nivelHidratacion


def calcularNivelEnergia(animal, entorno):
    # Define la tasa de cambio gradual para el nivel de energía.
    # Puedes ajustar este valor según la velocidad de cambio deseada.
    tasa_cambio = 0.05

    # Calcula el cambio en función de la actividad, disponibilidad de alimentos y temperatura.
    nivel_actividad = random.uniform(0.8, 1.2)
    disponibilidad_alimentos = entorno.disponibilidadAlimentos
    temperatura_ambiente = entorno.rangoTemperaturas

    # Fórmula que toma en cuenta la actividad, la disponibilidad de alimentos y la temperatura.
    cambio = (nivel_actividad * 0.4 + disponibilidad_alimentos *
              0.4 - (temperatura_ambiente - 25) * 0.05)

    # Limita el cambio para que esté dentro del rango [0, 1].
    # Evita que el nivel supere 1.
    cambio = max(0, min(1 - animal.nivelEnergia, cambio))

    # Actualiza el nivel de energía con el cambio gradual.
    nivelEnergia = animal.nivelEnergia
    nivelEnergia += cambio * tasa_cambio

    # Asegúrate de que el nivel de energía permanezca en el rango [0, 1].
    nivelEnergia = max(0, min(1, animal.nivelEnergia))

    return nivelEnergia


def calcularTemperaturaCorporal(animal, entorno):
    # La temperatura corporal del animal podría depender de la temperatura ambiente y la tasa de actividad.
    # Una fórmula podría ser:
    temperatura_ambiente = entorno.rangoTemperaturas
    nivel_actividad = random.uniform(0.8, 1.2)
    temperatura_corporal = 38 + \
        (temperatura_ambiente - 25) * 0.1 + (nivel_actividad - 1) * 0.2
    return temperatura_corporal


def calcularRespiracion(animal, entorno):
    # Factores que afectan la tasa de respiración.
    altitud = entorno.nivelAltitud  # Altitud en metros
    temperatura_ambiente = entorno.rangoTemperaturas  # Temperatura en grados Celsius
    nivel_actividad = random.uniform(0.8, 1.2)  # Nivel de actividad del animal

    # Coeficientes para ajustar la tasa de respiración.
    coeficiente_altitud = 0.005  # Aumento de la tasa de respiración por metro de altitud
    # Aumento de la tasa de respiración por cada grado por encima de 20°C
    coeficiente_temperatura = 0.1
    # Aumento de la tasa de respiración por nivel de actividad
    coeficiente_actividad = 0.02

    # Fórmula para calcular la tasa de respiración.
    tasa_respiracion = 10 + (altitud * coeficiente_altitud) + (temperatura_ambiente - 20) * \
        coeficiente_temperatura + (nivel_actividad - 1) * coeficiente_actividad

    return tasa_respiracion


def calcularSaturacionOxigeno(animal, entorno):
    # La saturación de oxígeno podría depender de la tasa de respiración del animal.
    # Una fórmula podría ser:
    tasa_respiracion = calcularRespiracion(animal, entorno)
    saturacion_oxigeno = 100 - (tasa_respiracion * 0.1)
    return saturacion_oxigeno


def calcularFrecuenciaCardiacaIdeal(animal, entorno):
    # Frecuencia cardíaca en reposo promedio de un león.
    frecuenciaCardiacaEnReposo = random.randint(60, 90)

    # Factores de ajuste
    factorEdad = min(1, animal.edad / 10)
    factorAgresividad = 1 + (animal.nivelAgresividad - 0.5) * 0.1
    factorComportamientoSocial = 1 - (animal.comportamientoSocial - 1) * 0.1
    factorResistenciaEnfermedades = 1 - \
        (animal.resistenciaEnfermedades - 0.5) * 0.1
    factorCalidadHabitat = 1 - (entorno.calidadHabitat - 0.5) * 0.1
    factorHidratacion = 1 - (1 - animal.nivelHidratacion) * 0.1
    factorEnergia = 1 - (1 - animal.nivelEnergia) * 0.1
    factorTemperaturaCorporal = 1 + (animal.temperaturaCorporal - 38.5) * 0.1
    factorRespiracion = 1 + (animal.respiracion - 20) * 0.05
    factorSaturacionOxigeno = 1 - (animal.saturacionOxigeno - 95) * 0.1

    # Calculamos la frecuencia cardíaca ideal considerando todos los factores.
    frecuenciaCardiacaIdeal = frecuenciaCardiacaEnReposo * factorEdad * factorAgresividad * factorComportamientoSocial * factorResistenciaEnfermedades * \
        factorCalidadHabitat * factorHidratacion * factorEnergia * \
        factorTemperaturaCorporal * factorRespiracion * factorSaturacionOxigeno

    return round(frecuenciaCardiacaIdeal)


def simularEpoca(poblacion, entorno):

    for specimen in poblacion:

        # Realiza cálculos y actualizaciones para cada variable de estado
        specimen.frecuenciaCardiaca = calcularFrecuenciaCardiacaIdeal(
            specimen, entorno)
        specimen.peso = calcularPeso(specimen, entorno)
        specimen.nivelHidratacion = calcularNivelHidratacion(specimen, entorno)
        specimen.nivelEnergia = calcularNivelEnergia(specimen, entorno)
        specimen.temperaturaCorporal = calcularTemperaturaCorporal(
            specimen, entorno)
        specimen.respiracion = calcularRespiracion(specimen, entorno)
        specimen.saturacionOxigeno = calcularSaturacionOxigeno(
            specimen, entorno)


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
    peso = random.randint(
        150, 250) if genero == 0 else random.randint(128, 182)
    tamano = random.randint(
        170, 250) if genero == 0 else random.randint(140, 175)

    poblacion.append(Animal(
        nombre=nombre,  # Nombre
        edad=random.randint(0, expectativa_vida),  # Edad
        genero=genero,  # Género
        peso=peso,  # Peso en kg
        tamano=tamano,  # Tamaño en cm
        velocidad=random.randint(50, 60),  # Velocidad en km/h
        # Capacidad de reproducción (0 - 1)
        capacidadReproduccion=capacidad_reproduccion,
        tasaAlimentacion=tasa_alimentacion,  # Tasa de alimentación en kg/día
        dieta=dieta,  # Dieta (por ejemplo, 1 para Carnívora)
        expectativaVida=expectativa_vida,  # Expectativa de vida en años
        # Comportamiento Social
        comportamientoSocial=comportamiento_social,
        depredadores=[],  # Depredadores
        presas=[],  # Presas
        nivelAgresividad=nivel_agresividad,  # Nivel de Agresividad (0 - 1)
        # Resistencia a Enfermedades (0 - 1)
        resistenciaEnfermedades=resistencia_enfermedades,
        fertilidad=fertilidad_promedio,  # Fertilidad (promedio de crías)
        frecuenciaCardiaca=random.randint(60, 90)  # frecuencia cardiaca
    ))

# Simulación de 100 épocas
for epoca in range(1, 101):
    if epoca == 1 or epoca == 50 or epoca == 100:
        print(
            f'\n\nDia {epoca}: \nFrecuencia: {poblacion[1].frecuenciaCardiaca} \nNivel hidratacion: {poblacion[1].nivelHidratacion}\nNivel Energia: {poblacion[1].nivelEnergia}\nTemperatura corporal: {poblacion[1].temperaturaCorporal}\nRespiracion: {poblacion[1].respiracion}\nSaturacion oxigeno: {poblacion[1].saturacionOxigeno}\nPeso: {poblacion[1].peso}')
    simularEpoca(poblacion, entorno)
