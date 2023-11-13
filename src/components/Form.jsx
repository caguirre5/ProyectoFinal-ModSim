import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import './Form.css'; 

class Formulario extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nombre: '',
      expectativaVida: '',
      capacidadReproduccion: '',
      tasaAlimentacion: '',
      dieta: '',
      comportamientoSocial: '',
      nivelAgresividad: '',
      resistenciaEnfermedades: '',
      fertilidadPromedio: '',
      pesoMin: '',
      pesoMax: '',
      tamañoMin: '',
      tamañoMax: '',
    };
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    // Llama a la función de envío con los valores del formulario
    this.props.onSubmit(this.state);
    // Restablece el formulario o realiza otras acciones necesarias
    this.setState({
      nombre: '',
      expectativaVida: '',
      capacidadReproduccion: '',
      tasaAlimentacion: '',
      dieta: '',
      pesoMin: '',
      pesoMax: '',
      tamañoMin: '',
      tamañoMax: '',
      entorno: '',
      poblacion: '',
    });
    // Cierra el menú después de enviar el formulario (si es necesario)
    this.props.toggleMenu();
  };

  render() {
    return (
        <div className='form-container'>
          <div className='close-button'>
            <FontAwesomeIcon onClick={this.props.toggleMenu} icon={faTimes} className='close-button-icon'/>
          </div>
          <form onSubmit={this.handleSubmit}>
            <div>
              <div className='input-group input-name'>
                  <label>Animal:</label>
                  <input type="text" name="nombre" onChange={this.handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Expectativa de vida:</label>
                <input type="number" name="expectativaVida" onChange={this.handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Capacidad de reproducción:</label>
                <input type="number" name="capacidadReproduccion" onChange={this.handleChange} />
              </div>
          
              <div className='input-group'>
                <label>Tasa de alimentación:</label>
                <input type="number" name="tasaAlimentacion" onChange={this.handleChange} />
              </div>

              <div className='input-group'>
                <label>Dieta:</label>
                <select name="dieta" onChange={this.handleChange}>
                  <option value="opcion1">Opción 1</option>
                  <option value="opcion2">Opción 2</option>
                </select>
              </div>
          
              <div className='input-group'>
                  <label>Peso (Rango):</label>
                  <input className='left-input' type="number" name="pesoMin" placeholder="Min" onChange={this.handleChange} />
                  <input className='right-input' type="number" name="pesoMax" placeholder="Max" onChange={this.handleChange} />
              </div>
          
              <div className='input-group'>
                  <label>Tamaño (Rango):</label>
                  <input className='left-input' type="number" name="tamañoMin" placeholder="Min" onChange={this.handleChange} />
                  <input className='right-input' type="number" name="tamañoMax" placeholder="Max" onChange={this.handleChange} />
              </div>

              <div className='input-group'>
                <label>Entorno:</label>
                <select name="entorno" onChange={this.handleChange}>
                  <option value="opcion1">Opción 1</option>
                  <option value="opcion2">Opción 2</option>
                </select>
              </div>

              <div className='input-group'>
                <label>Poblacion:</label>
                <input type="number" value={10} name="poblacion" onChange={this.handleChange} />
              </div>
              <div className='input-group'>
                <label>Duración (Dias):</label>
                <input type="number" value={10} name="epocas" onChange={this.handleChange} />
              </div>
            </div>
            <button type="submit">Guardar</button>
          </form>
        </div>      
    );
  }
}

export default Formulario;
