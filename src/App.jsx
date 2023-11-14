import { useState } from 'react'
import Formulario from './components/Form';
import Header from './components/Header'
import Content from './components/Content'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const [tempResult, setTempResult] = useState({
    poblacion: [10],
    animales: [],
    promedios: [],
    movimientos:[],
    duracion: 6, //dias
    n_poblacion: 10, //ejemplares
    is_running: false
  })

  //Data inicial del componente
  const [result, setResult] = useState({
    poblacion: [10],
    animales: [],
    promedios: [],
    movimientos:[],
    duracion: 6, //dias
    n_poblacion: 10, //ejemplares
    is_running: false,
    epoch:0,
  })

  function toggleMenu() {
    setIsMenuOpen(!isMenuOpen);
  }  

  const handleFormSubmit = async (values) => {
    // Construye la URL con los valores de formData
    const url = new URL('https://cristian2605.pythonanywhere.com/modsim');
    Object.entries(values).forEach(([key, value]) => {
      url.searchParams.append(key, value);
    });
  
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      if (response.ok) {
        const resultFetch = await response.json();
  
        setTempResult({
          ...tempResult,
          duracion:values.duracion,
          n_poblacion: values.n_poblacion,
          poblacion: resultFetch["poblacion"],
          animales: resultFetch["animales"],
          promedios: resultFetch["promedios"],
          movimientos:resultFetch["movimientos"],
        });
      } else {
        console.error('Error al obtener los datos del servidor');
      }
    } catch (error) {
      console.error('Error de red:', error);
    }
  };

  // Iniciar simulacion (Boton ejecutar)
  const handleStartSimulation = () => {
    //Hasta que se ejecuta actualizamos la data
    setResult({
      ...tempResult,
      is_running:!result["is_running"],
      epoch:0
    })
  };

 
  return (
    <div className='app-container'>
      <Header toggleMenu={toggleMenu} onStartSimulation={handleStartSimulation}/>
      <Content result={result} handleRunning={handleStartSimulation}/>
      <div className={`menu ${isMenuOpen ? 'open' : ''}`}>
        <Formulario toggleMenu = {toggleMenu} onSubmit={handleFormSubmit}/>
      </div>
    </div>
  )
}

export default App
