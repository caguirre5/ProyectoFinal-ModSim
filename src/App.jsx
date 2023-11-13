import { useState } from 'react'
import Formulario from './components/Form';
import Header from './components/Header'
import Content from './components/Content'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [formData, setFormData] = useState({
    nombre: "Leon",
    expectativa_vida: 12,
    capacidad_reproduccion: 4,
    tasa_alimentacion: 7,
    dieta: 1,
    peso: 80,
    tamano: 120,
    entorno: 1,
    duracion: 10,
    poblacion:[10,8,7,5,2],
    animales: null
  });
  const [newData, setNewData] = useState({
    nombre: "Leon",
    expectativa_vida: 12,
    capacidad_reproduccion: 4,
    tasa_alimentacion: 7,
    dieta: 1,
    peso: 80,
    tamano: 120,
    entorno: 1,
    duracion: 10,
    poblacion:[10,8,7,5,2],
    animales: null,
  });
  const [isRunning, setIsRunning] = useState(false);

  function toggleMenu() {
    setIsMenuOpen(!isMenuOpen);
  }  

  const handleFormSubmit = async (values) => {
    // Construye la URL con los valores de formData
    const url = new URL('https://cristian2605.pythonanywhere.com/modsim');
    Object.entries(formData).forEach(([key, value]) => {
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
        const result = await response.json();
        // Actualizar el estado con los resultados
        setFormData({
          ...formData,
          poblacion: result["poblacion"],
          animales: result["animales"],
          promedios: result["promedios"]
        });
        console.log('Updated')
      } else {
        console.error('Error al obtener los datos del servidor');
      }
    } catch (error) {
      console.error('Error de red:', error);
    }
  }

  const handleStartSimulation = () => {
    setNewData({...formData});
    setIsRunning(true);
  };

  return (
    <div className='app-container'>
      <Header toggleMenu={toggleMenu} onStartSimulation={handleStartSimulation}/>
      <Content formData={newData} isRunning={isRunning} setIsRunning={setIsRunning}/>
      <div className={`menu ${isMenuOpen ? 'open' : ''}`}>
        <Formulario toggleMenu = {toggleMenu} onSubmit={handleFormSubmit}/>
      </div>
    </div>
  )
}

export default App
