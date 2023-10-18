import Animal from './animal.jsx';
import Terreno from './terrain.js';

// Instancia de la clase Leon (Animal)
const animal = new Leon(
    "León Africano",
    8, // Edad
    "Macho", // Género
    180, // Peso en kg
    200, // Tamaño en cm
    60, // Velocidad en m/s
    0.7, // Capacidad de reproducción (0 - 1)
    8, // Tasa de alimentación en kg/día
    1, // Dieta (por ejemplo, 1 para Carnívora)
    12, // Expectativa de vida en años
    3, // Comportamiento Social (por ejemplo, 3 para Manada)
    [], // Depredadores
    [4, 5, 6], // Presas
    0.8, // Nivel de Agresividad (0 - 1)
    0.3, // Capacidad de Movimiento (0 - 1)
    0.85, // Resistencia a Enfermedades (0 - 1)
    4, // Fertilidad (promedio de crías)
    15, // Longevidad en años
    "Caza en grupo y se alimenta de grandes mamíferos herbívoros." // Comportamiento de Caza/Alimentación
);
  
  // Instancia de la clase Entorno
const entorno = new Entorno(
    1, // Tipo de terreno
    1, // Clima
    4, // Estaciones
    3, // Disponibilidad de alimentos (por ejemplo, Abundante)
    0.8, // Riesgos Ambientales
    2, // Topografía (por ejemplo, Montañoso)
    0.8, // Vegetación
    0.6, // Humedad
    0.2, // Contaminación
    0.9, // Calidad del agua
    800, // Nivel de precipitación
    1500, // Nivel de altitud
    0.7, // Calidad del suelo
    25, // Rango de temperaturas
    0.6, // Razón día/noche
    300, // Nivel de radiación solar
    40, // Nivel de ruido ambiental
    0.2, // Nivel de polución lumínica
    0.5, // Razón depredadores/presas
    0.8 // Calidad del hábitat
);
  

function handleFrecuenciaCardiaca() {
  // La frecuencia cardíaca normal en reposo de un león puede variar, pero
  // en promedio, se estima en alrededor de 60-90 latidos por minuto.
  const frecuenciaCardiacaEnReposo = Math.floor(Math.random() * 31) + 60;

  // Ajustamos la frecuencia cardíaca en función de la edad del león.
  // Los leones más jóvenes tienden a tener frecuencias cardíacas más altas.
  const factorEdad = Math.min(1, animal.edad / 10);

  // Ajustamos la frecuencia cardíaca en función de la agresividad.
  // Los leones más agresivos pueden tener frecuencias cardíacas ligeramente más altas.
  const factorAgresividad = 1 + (animal.nivelAgresividad - 0.5) * 0.1;

  // Ajustamos la frecuencia cardíaca en función del comportamiento social.
  // Los leones que viven en manadas pueden tener frecuencias cardíacas más bajas.
  const factorComportamientoSocial = 1 - (animal.comportamientoSocial - 1) * 0.1;

  // Calculamos la frecuencia cardíaca ideal.
  const frecuenciaCardiacaIdeal = frecuenciaCardiacaEnReposo * factorEdad * factorAgresividad * factorComportamientoSocial;

  return Math.round(frecuenciaCardiacaIdeal);
}

 
function handleNivelHidratacion(){

}
function handleNivelEnergia(){

}
function handleTemperaturaCorporal(){

}
function handleRespiracion(){

}
function handleSaturacionOxigeno(){

}  

// Función para simular una época de la simulación
function simularEpoca(animal, entorno) {
    // Realiza cálculos y actualizaciones para cada variable de estado
    leon.FrecuenciaCardiaca = handleFrecuenciaCardiaca(leon, terreno);
    leon.NivelHidratacion = handleNivelHidratacion(leon, terreno);
    leon.NivelEnergia = handleNivelEnergia(leon, terreno);
    leon.TemperaturaCorporal = handleTemperaturaCorporal(leon, terreno);
    leon.Respiracion = handleRespiracion(leon, terreno);
    leon.SaturacionOxigeno = handleSaturacionOxigeno(leon, terreno);

    // Puedes imprimir los valores de cada época si lo deseas
    console.log(`Época ${epoca}:`);
    console.log(`Frecuencia Cardíaca: ${frecuenciaCardiaca}`);
    console.log(`Nivel de Hidratación: ${nivelHidratacion}`);
    // ... Otros valores

    // Incrementa la edad del león en cada época
    leon.Edad++;
}

// Simulación de 100 épocas
// for (let epoca = 1; epoca <= 100; epoca++) {
//     simularEpoca(animal, entorno);
// }

 // Ejemplo de uso:
const frecuenciaCardiacaIdeal = calcularFrecuenciaCardiacaIdeal(animal);
console.log(`Frecuencia Cardíaca Ideal: ${frecuenciaCardiacaIdeal} latidos por minuto.`);
 
  