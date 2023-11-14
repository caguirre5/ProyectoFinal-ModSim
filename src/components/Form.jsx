import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import './Form.css'; 

function Formulario(props) {
  const [localFormData, setLocalFormData] = useState({
    nombre: "Leon",
    expectativa_vida: 12,
    capacidad_reproduccion: 4,
    tasa_alimentacion: 7,
    dieta: 1,
    pesoMin: 150,
    pesoMax: 250,
    tamañoMin: 175,
    tamañoMax: 250,
    entorno: 1,
    duracion: 10,
    n_poblacion:10,
  });

  const handleChange = (e) => {
    // Si cambiamos un campo en el form, 
    //lo actualizamos en el state loal
    const { name, value } = e.target;
    const parsedValue = name === 'nombre' ? value : parseInt(value, 10);

    setLocalFormData({
      ...localFormData,
      [name]: parsedValue || '', // Si el valor no es numérico, se establece como una cadena vacía
    });
  }

  const handleSubmit = (e) => {
    console.log('LocalData',localFormData)
    //Si hacemos submit, llamamos a la funcion
    //onSubmit que viene del App y le pasamos la data
    e.preventDefault();
    props.toggleMenu()
    props.onSubmit(localFormData);
  };

  return (
    <div className='form-container'>
      <div className='close-button'>
        <FontAwesomeIcon onClick={props.toggleMenu} icon={faTimes} className='close-button-icon'/>
      </div>
      <form onSubmit={handleSubmit}>
      <div>
              <div className='input-group input-name'>
                  <label>Animal:</label>
                  <input type="text" name="nombre" onChange={handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Expectativa de vida:</label>
                <input type="number" name="expectativa_vida" onChange={handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Capacidad de reproducción:</label>
                <input type="number" name="capacidad_reproduccion" onChange={handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Tasa de alimentación:</label>
                <input type="number" name="tasa_alimentacion" onChange={handleChange} />
              </div>

              <div className='input-group'>
                <label>Dieta:</label>
                <select name="dieta" onChange={handleChange}>
                  <option value={1}>Herbívoros</option>
                  <option value={2}>Carnívoros</option>
                  <option value={3}>Omnívoros</option>
                </select>
              </div>
          
              <div className='input-group'>
                  <label>Peso (Rango):</label>
                  <input className='left-input' type="number" name="pesoMin" placeholder="Min" onChange={handleChange} />
                  <input className='right-input' type="number" name="pesoMax" placeholder="Max" onChange={handleChange} />
              </div>
          
              <div className='input-group'>
                  <label>Tamaño (Rango):</label>
                  <input className='left-input' type="number" name="tamañoMin" placeholder="Min" onChange={handleChange} />
                  <input className='right-input' type="number" name="tamañoMax" placeholder="Max" onChange={handleChange} />
              </div>

              <div className='input-group'>
                <label>Entorno:</label>
                <select name="entorno" onChange={handleChange}>
                  <option value={1}>Desierto</option>
                  <option value={2}>Selva Tropical</option>
                  <option value={3}>Motaña</option>
                </select>
              </div>

              <div className='input-group'>
                <label>Poblacion:</label>
                <input type="number" name="n_poblacion" onChange={handleChange} />
              </div>
              <div className='input-group'>
                <label>Duración (Dias):</label>
                <input type="number" name="duracion" onChange={handleChange} />
              </div>
            </div>
            <button type="submit">Guardar</button>
      </form>
    </div>
  );
}

export default Formulario;
