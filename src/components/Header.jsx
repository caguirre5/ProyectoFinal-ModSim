import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlay, faSliders } from '@fortawesome/free-solid-svg-icons';
import './Header.css'

function Header(props) { 
    return (
        <div className='header-container'>
            
            <button id='params-button' onClick={props.toggleMenu}>
                <FontAwesomeIcon  icon={faSliders} className='params-icon'/>
            </button>
            <div className='right-navbar-buttons'>
                {/* <button>Estadísticas</button> */}
                <button id='play-button' onClick={props.onStartSimulation}>
                    Ejecutar
                    <FontAwesomeIcon icon={faPlay} className='play-icon'/> 
                </button>
            </div>
        </div>
    )
}

export default Header;