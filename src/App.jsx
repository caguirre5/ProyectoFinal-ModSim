import { useState } from 'react'
import Formulario from './components/Form';
import Header from './components/Header'
import Content from './components/Content'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);



  function toggleMenu() {
    setIsMenuOpen(!isMenuOpen);
  }  

  return (
    <div className='app-container'>
      <Header toggleMenu={toggleMenu}/>
      <Content/>
      <div className={`menu ${isMenuOpen ? 'open' : ''}`}>
        <Formulario toggleMenu = {toggleMenu}/>
      </div>
    </div>
  )
}

export default App
