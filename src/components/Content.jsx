import React, {useState, useEffect, useRef} from 'react'
import { LineChart } from '@mui/x-charts/LineChart';
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeartbeat, faThermometerThreeQuarters, faLungs } from '@fortawesome/free-solid-svg-icons';

import './Content.css'


const data = [
  {
    id: 'data-0',
    x1: 329.39,
    x2: 391.29,
    y1: 443.28,
    y2: 153.9,
  },
  {
    id: 'data-1',
    x1: 96.94,
    x2: 139.6,
    y1: 110.5,
    y2: 217.8,
  },
  {
    id: 'data-2',
    x1: 336.35,
    x2: 282.34,
    y1: 175.23,
    y2: 286.32,
  },
  {
    id: 'data-3',
    x1: 159.44,
    x2: 384.85,
    y1: 195.97,
    y2: 325.12,
  },
  {
    id: 'data-4',
    x1: 188.86,
    x2: 182.27,
    y1: 351.77,
    y2: 144.58,
  },
  {
    id: 'data-5',
    x1: 143.86,
    x2: 360.22,
    y1: 43.253,
    y2: 146.51,
  },
  {
    id: 'data-6',
    x1: 202.02,
    x2: 209.5,
    y1: 376.34,
    y2: 309.69,
  },
  {
    id: 'data-7',
    x1: 384.41,
    x2: 258.93,
    y1: 31.514,
    y2: 236.38,
  },
  {
    id: 'data-8',
    x1: 256.76,
    x2: 70.571,
    y1: 231.31,
    y2: 440.72,
  },
  {
    id: 'data-9',
    x1: 143.79,
    x2: 419.02,
    y1: 108.04,
    y2: 20.29,
  },
  {
    id: 'data-10',
    x1: 103.48,
    x2: 15.886,
    y1: 321.77,
    y2: 484.17,
  },
  {
    id: 'data-11',
    x1: 272.39,
    x2: 189.03,
    y1: 120.18,
    y2: 54.962,
  },
  {
    id: 'data-12',
    x1: 23.57,
    x2: 456.4,
    y1: 366.2,
    y2: 418.5,
  },
  {
    id: 'data-13',
    x1: 219.73,
    x2: 235.96,
    y1: 451.45,
    y2: 181.32,
  },
  {
    id: 'data-14',
    x1: 54.99,
    x2: 434.5,
    y1: 294.8,
    y2: 440.9,
  },
  {
    id: 'data-15',
    x1: 134.13,
    x2: 383.8,
    y1: 121.83,
    y2: 273.52,
  },
  {
    id: 'data-16',
    x1: 12.7,
    x2: 270.8,
    y1: 287.7,
    y2: 346.7,
  },
  {
    id: 'data-17',
    x1: 176.51,
    x2: 119.17,
    y1: 134.06,
    y2: 74.528,
  },
  {
    id: 'data-18',
    x1: 65.05,
    x2: 78.93,
    y1: 104.5,
    y2: 150.9,
  },
  {
    id: 'data-19',
    x1: 162.25,
    x2: 63.707,
    y1: 413.07,
    y2: 26.483,
  },
  {
    id: 'data-20',
    x1: 68.88,
    x2: 150.8,
    y1: 74.68,
    y2: 333.2,
  },
  {
    id: 'data-21',
    x1: 95.29,
    x2: 329.1,
    y1: 360.6,
    y2: 422.0,
  },
  {
    id: 'data-22',
    x1: 390.62,
    x2: 10.01,
    y1: 330.72,
    y2: 488.06,
  },
];

function ProgressBar({ label, progress }) {
  const barStyle = {
    width: `${progress}%`,
  };

  return (
    <div className="progress-bar">
      <div className="label">{label}</div>
      <div className="bar">
        <div className="fill" style={barStyle}></div>
      </div>
    </div>
  );
}

function IconVital({ label, icon, color = 'red' }) {

  return (
    <div className="icon-vital">
      <div className="icon-vital-container">
        <FontAwesomeIcon icon={icon} className='icon' style={{color:color}}/> 
      </div>
      <div className="icon-vital-label">{label}</div>
    </div>
  );
}

function Content(props) {

    const [epoch, setEpoch] = useState(0)
    const [epochControl, setEpochControl] = useState(0)
    const [movimientos, setMovimientos] = useState([[0,0]])

    let n = props.result.duracion

    
    
    // if (props.result.is_running ){
    //   setMovimientos(props.result.animales.movimientos == undefined ? [[0,0]] : props.result.animales.movimientos)
    // }
    // // Efecto para actualizar la posición cada 2 segundos
    useEffect(() => {
      let intervalId;
  
      if (props.result.is_running) {
        intervalId = setInterval(() => {
          if (epochControl < n && epoch + 1 !== n) {
            setEpochControl(epochControl + 1);
            setEpoch(epoch + 1);
            let array
            if (props.result.movimientos[epoch][0].length === 0){
              array = props.result.movimientos[epoch+1]
            } else {
              array = props.result.movimientos[epoch]
            }
            setMovimientos(array)
          }  else {
            clearInterval(intervalId);
            props.handleStartSimulation
            // setEpochControl(0)
          }
        }, 500);
      } else {
        clearInterval(intervalId);
        props.handleStartSimulation
        // setEpochControl(0)
      }
  
      return () => clearInterval(intervalId);
    }, [epoch, props.isRunning, props.result.animales]);
    
    return (
        <div className='content-container'>
            <div className='main-container'>
              <div className='text-container'>
                <h1>Simulación de especies</h1>
                <p>Ya sea que seas un entusiasta de la vida salvaje o simplemente busques una experiencia relajante y educativa, nuestra aplicación web te ofrece una ventana única al mundo animal. ¡Sumérgete en la simulación y descubre la belleza y complejidad de la vida en la naturaleza!</p>
              </div>
              <div className='vitals-container'>
                <div className='vitals-text-container'>
                  <IconVital color='#F26B76' label={props.result.promedios.Frecuencia == undefined ? 0:props.result.promedios.Frecuencia[epoch]} icon={faHeartbeat}/>
                  <IconVital color='#89C2D9' label={props.result.promedios.Respiracion == undefined ? 0:props.result.promedios.Respiracion[epoch]} icon={faLungs}/>
                  <IconVital color='#FF911A' label={props.result.promedios.Temperatura == undefined ? 0:props.result.promedios.Temperatura[epoch]} icon={faThermometerThreeQuarters}/>
                </div>
                <div className='bars-container'>
                  <ProgressBar label="Hidratación" progress={props.result.promedios.Hidratacion == undefined ? 0 :props.result.promedios.Hidratacion[epoch]*100} />
                  <ProgressBar label="Energía" progress={props.result.promedios.Energia == undefined ? 0 :props.result.promedios.Energia[epoch]*100} />
                  <ProgressBar label="Saturación de oxígeno" progress={props.result.promedios.Saturacion == undefined ? 0 :props.result.promedios.Saturacion[epoch]*100} />
                </div>
              </div>
            </div>
            <aside>
              <div className='population-container'>
                <LineChart
                    xAxis={[{ data: Array.from({ length: props.result.duracion}, (_, index) => index + 1) }]}
                    series={[
                        {
                        data: props.result.poblacion,
                        color: '#59a14f'
                        },
                    ]}
                />
              </div>
              <div className='map-container'>
              <ScatterChart
                width={600}
                height={300}
                
                series={[
                  {
                    data: [].concat(movimientos.map((pair, index) => ({ id: `point_${index}`, x: pair[0], y: pair[1] }))),
                    color: '#59a14f'
                  },{
                    data:[{ id:'origin', x: 0, y: 0 }, { id:'end', x: 500, y: 500 }],
                    color:'white'
                  }
                ]}
              />
              </div>
            </aside>
            
        </div>
    )
}

export default Content