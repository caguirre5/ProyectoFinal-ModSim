class Animal:
    def __init__(self, ID, nombre, edad, genero, peso, tamano, velocidad, capacidadReproduccion, tasaAlimentacion, dieta, expectativaVida, comportamientoSocial, depredadores, presas, nivelAgresividad, resistenciaEnfermedades, fertilidad, frecuenciaCardiaca):
        self.ID = ID,
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.tamano = tamano
        self.velocidad = velocidad
        self.capacidadReproduccion = capacidadReproduccion
        self.tasaAlimentacion = tasaAlimentacion
        self.dieta = dieta
        self.expectativaVida = expectativaVida
        self.comportamientoSocial = comportamientoSocial
        self.depredadores = depredadores
        self.presas = presas
        self.nivelAgresividad = nivelAgresividad
        self.resistenciaEnfermedades = resistenciaEnfermedades
        self.fertilidad = fertilidad

        # --------------------- Signos vitales ------------------------
        self.frecuenciaCardiaca = frecuenciaCardiaca
        self.nivelHidratacion = 0.6
        self.nivelEnergia = 0.7
        self.temperaturaCorporal = 38.5
        self.respiracion = 20
        self.saturacionOxigeno = 95

        self.vivo = True
