from animal import Animal
from terrain import Terreno
from flask import Flask, request, jsonify
import random
import json

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
    return saturacion_oxigeno/100


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
        # Primero verificar si esta vivo
        if specimen.vivo:  # Si si lo esta hacmos las actualizaciones

            # Realiza cálculos y actualizaciones para cada variable de estado
            specimen.frecuenciaCardiaca = calcularFrecuenciaCardiacaIdeal(
                specimen, entorno)
            specimen.peso = round(calcularPeso(specimen, entorno), 2)
            specimen.nivelHidratacion = round(
                calcularNivelHidratacion(specimen, entorno), 2)
            specimen.nivelEnergia = round(
                calcularNivelEnergia(specimen, entorno), 2)
            specimen.temperaturaCorporal = round(
                calcularTemperaturaCorporal(specimen, entorno), 2)
            specimen.respiracion = round(
                calcularRespiracion(specimen, entorno), 2)
            specimen.saturacionOxigeno = round(
                calcularSaturacionOxigeno(specimen, entorno), 2)

            # Luego de actualizar, verificar signos vitales para determinar si sigue vivo o muere
            if specimen.frecuenciaCardiaca > 1000:
                specimen.vivo = False

            new_x = random.choice([-1, 1])*5
            new_y = random.choice([-1, 1])*5

            # actualizar posicion
            specimen.x += random.choice([-1, 1])*5
            specimen.y += random.choice([-1, 1])*5

        else:
            # actualizar posicion
            specimen.x = 0
            specimen.y = 0

        specimen.posicion = ([specimen.x, specimen.y])


def Execute(n_poblacion, nombre, expectativa_vida, capacidad_reproduccion, tasa_alimentacion, dieta, pesoMin, pesoMax, tamanoMin, tamanoMax, entorno, duracion):
    # Incializar poblacion
    poblacion = []

    if entorno == 1:
        entorno = Terreno(
            2,    # Tipo de terreno (Desierto)
            3,    # Clima (Árido)
            2,    # Estaciones (Pocas o ninguna)
            1,    # Disponibilidad de alimentos (Muy escasa)
            0.9,  # Riesgos Ambientales (Puedes ajustar según la situación)
            1,    # Topografía (Plano o dunas)
            0.1,  # Vegetación (Prácticamente nula)
            0.1,  # Humedad (Extremadamente baja)
            0.3,  # Contaminación (Baja en general)
            0.5,  # Calidad del agua (Moderada a baja)
            50,   # Nivel de precipitación (Muy bajo)
            1000,  # Nivel de altitud (Zonas bajas o llanuras)
            0.3,  # Calidad del suelo (Árido)
            40,   # Rango de temperaturas (Muy altas)
            0.6,  # Razón día/noche (Días muy largos en zonas calurosas)
            300,  # Nivel de radiación solar (Muy alto)
            # Nivel de ruido ambiental (Puedes ajustar según la situación)
            10,
            0.1,  # Nivel de polución lumínica (Bajo)
            # Razón depredadores/presas (Puedes ajustar según la situación)
            0.3,
            0.5   # Otros parámetros (Puedes ajustar según la situación)
        )
    elif entorno == 2:
        entorno = Terreno(
            1,    # Tipo de terreno (Selva tropical)
            2,    # Clima (Cálido y húmedo)
            4,    # Estaciones (Marcadas)
            4,    # Disponibilidad de alimentos (Abundante)
            0.6,  # Riesgos Ambientales (Puedes ajustar según la situación)
            3,    # Topografía (Variada, con colinas y llanuras)
            0.8,  # Vegetación (Exuberante)
            0.7,  # Humedad (Alta)
            0.4,  # Contaminación (Moderada)
            0.8,  # Calidad del agua (Alta)
            250,  # Nivel de precipitación (Muy alto)
            500,  # Nivel de altitud (Llanuras y colinas)
            0.7,  # Calidad del suelo (Rico en nutrientes)
            25,   # Rango de temperaturas (Cálido)
            0.7,  # Razón día/noche (Equilibrada)
            400,  # Nivel de radiación solar (Alto)
            30,   # Nivel de ruido ambiental (Moderado)
            0.4,  # Nivel de polución lumínica (Moderado)
            # Razón depredadores/presas (Puedes ajustar según la situación)
            0.6,
            0.8   # Otros parámetros (Puedes ajustar según la situación)
        )

    else:
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
            # Razón depredadores/presas (Puedes ajustar según la situación)
            0.5,
            0.8
        )

    result = {
        "poblacion": [],
        "animales": {},
        "movimientos": [],
    }

    for i in range(n_poblacion):
        ID = i+1
        nombre = nombre
        genero = random.randint(0, 1)
        expectativa_vida = expectativa_vida
        capacidad_reproduccion = capacidad_reproduccion  # 0.7
        tasa_alimentacion = tasa_alimentacion  # 8 kgs/dia
        dieta = dieta  # 1
        comportamiento_social = 3
        nivel_agresividad = 0.8
        resistencia_enfermedades = 0.85
        fertilidad_promedio = 4
        peso = random.randint(
            pesoMin, pesoMax) if genero == 0 else random.randint(int(round(pesoMin*0.72, 0)), int(round(pesoMax*0.72, 0)))
        tamano = random.randint(
            tamanoMin, tamanoMax) if genero == 0 else random.randint(int(round(tamanoMin * 0.72, 0)), int(round(tamanoMax * 0.72, 0)))

        animal = Animal(
            ID=ID,
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
        )
        poblacion.append(animal)
        result["animales"][ID] = {
            "Frecuencia": {"valores": []},
            "Hidratacion": {"valores": []},
            "Energia": {"valores": []},
            "Temperatura": {"valores": []},
            "Respiracion": {"valores": []},
            "Saturacion": {"valores": []},
        }

    result["promedios"] = {
        "Frecuencia": [],
        "Hidratacion": [],
        "Energia": [],
        "Temperatura": [],
        "Respiracion": [],
        "Saturacion": [],
    }

    # Simulación de 100 épocas
    for epoca in range(1, duracion+1):
        promedio_f = []
        promedio_h = []
        promedio_e = []
        promedio_t = []
        promedio_r = []
        promedio_s = []
        movimientos_del_dia = []
        vivos = 0
        for animal in result["animales"]:

            # Si el animal esta vivo, lo agregamos al contador
            if poblacion[int(animal-1)].vivo:
                vivos += 1

            result["animales"][animal]["Frecuencia"]["valores"].append(
                poblacion[animal-1].frecuenciaCardiaca)
            promedio_f.append(poblacion[animal-1].frecuenciaCardiaca)

            result["animales"][animal]["Hidratacion"]["valores"].append(
                poblacion[animal-1].nivelHidratacion)
            promedio_h.append(poblacion[animal-1].nivelHidratacion)

            result["animales"][animal]["Energia"]["valores"].append(
                poblacion[animal-1].nivelEnergia)
            promedio_e.append(poblacion[animal-1].nivelEnergia)

            result["animales"][animal]["Temperatura"]["valores"].append(
                poblacion[animal-1].temperaturaCorporal)
            promedio_t.append(poblacion[animal-1].temperaturaCorporal)

            result["animales"][animal]["Respiracion"]["valores"].append(
                poblacion[animal-1].respiracion)
            promedio_r.append(poblacion[animal-1].respiracion)

            result["animales"][animal]["Saturacion"]["valores"].append(
                poblacion[animal-1].saturacionOxigeno)
            promedio_s.append(poblacion[animal-1].saturacionOxigeno)

            # Agrgar posicion del animal
            movimientos_del_dia.append(poblacion[int(animal-1)].posicion)

        result["promedios"]["Frecuencia"].append(
            round(sum(promedio_f) / len(promedio_f), 0))
        result["promedios"]["Hidratacion"].append(
            round(sum(promedio_h) / len(promedio_h), 2))
        result["promedios"]["Energia"].append(
            round(sum(promedio_e) / len(promedio_e), 2))
        result["promedios"]["Temperatura"].append(
            round(sum(promedio_t) / len(promedio_t), 2))
        result["promedios"]["Respiracion"].append(
            round(sum(promedio_r) / len(promedio_r), 2))
        result["promedios"]["Saturacion"].append(
            round(sum(promedio_s) / len(promedio_s), 2))
        result["movimientos"].append(movimientos_del_dia)

        result["poblacion"].append(vivos)
        simularEpoca(poblacion, entorno)

    for animal in result["animales"]:
        result["animales"][animal]["Frecuencia"]["promedio"] = round(sum(
            result["animales"][animal]["Frecuencia"]["valores"]) / len(result["animales"][animal]["Frecuencia"]["valores"]), 0)
        result["animales"][animal]["Hidratacion"]["promedio"] = round(sum(
            result["animales"][animal]["Hidratacion"]["valores"]) / len(result["animales"][animal]["Hidratacion"]["valores"]), 2)
        result["animales"][animal]["Energia"]["promedio"] = round(sum(
            result["animales"][animal]["Energia"]["valores"]) / len(result["animales"][animal]["Energia"]["valores"]), 2)
        result["animales"][animal]["Temperatura"]["promedio"] = round(sum(
            result["animales"][animal]["Temperatura"]["valores"]) / len(result["animales"][animal]["Temperatura"]["valores"]), 2)
        result["animales"][animal]["Respiracion"]["promedio"] = round(sum(
            result["animales"][animal]["Respiracion"]["valores"]) / len(result["animales"][animal]["Respiracion"]["valores"]), 2)
        result["animales"][animal]["Saturacion"]["promedio"] = round(sum(
            result["animales"][animal]["Saturacion"]["valores"]) / len(result["animales"][animal]["Saturacion"]["valores"]), 0)

    return result
