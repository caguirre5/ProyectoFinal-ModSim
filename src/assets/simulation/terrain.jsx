class Terreno {
    constructor(tipoTerreno, clima, estaciones, disponibilidadAlimentos, riesgosAmbientales, topografia, vegetacion, humedad, contaminacion, calidadAgua, nivelPrecipitacion, nivelAltitud, calidadSuelo, rangoTemperaturas, razonDiaNoche, nivelRadiacionSolar, nivelRuidoAmbiental, nivelPolucionLuminica, razonDepredadoresPresas, calidadHabitat) {
      this.tipoTerreno = tipoTerreno;
      this.clima = clima;
      this.estaciones = estaciones;
      this.disponibilidadAlimentos = disponibilidadAlimentos;
      this.riesgosAmbientales = riesgosAmbientales;
      this.topografia = topografia;
      this.vegetacion = vegetacion;
      this.humedad = humedad;
      this.contaminacion = contaminacion;
      this.calidadAgua = calidadAgua;
      this.nivelPrecipitacion = nivelPrecipitacion;
      this.nivelAltitud = nivelAltitud;
      this.calidadSuelo = calidadSuelo;
      this.rangoTemperaturas = rangoTemperaturas;
      this.razonDiaNoche = razonDiaNoche;
      this.nivelRadiacionSolar = nivelRadiacionSolar;
      this.nivelRuidoAmbiental = nivelRuidoAmbiental;
      this.nivelPolucionLuminica = nivelPolucionLuminica;
      this.razonDepredadoresPresas = razonDepredadoresPresas;
      this.calidadHabitat = calidadHabitat;
    }
    
}
  
// Exporta la clase Terreno
module.exports = Terreno;