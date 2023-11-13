import React, {useState, useEffect, useRef} from 'react'
import { LineChart } from '@mui/x-charts/LineChart';
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import HighCharts3D from 'highcharts/highcharts-3d'
import Plot from 'react-plotly.js';
import Map from './Map';

import './Content.css'

if (typeof Highcharts === 'object') {
    HighCharts3D(Highcharts)
}

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
    height: `${progress}%`,
  };

  return (
    <div className="progress-bar">
      <div className="bar">
        <div className="fill" style={barStyle}></div>
      </div>
      <div className="label">{label}</div>
    </div>
  );
}

function Content() {

    // Define el progreso para cada barra
    const [progress1, setProgress1] = useState(30);
    const [progress2, setProgress2] = useState(60);
    const [progress3, setProgress3] = useState(75);
    const [progress4, setProgress4] = useState(45);
    const [progress5, setProgress5] = useState(90);

    
    return (
        <div className='content-container'>
            <div className='main-container'>
              <div className='text-container'>
                <h1>Simulación de especies</h1>
                <p>Ya sea que seas un entusiasta de la vida salvaje o simplemente busques una experiencia relajante y educativa, nuestra aplicación web te ofrece una ventana única al mundo animal. ¡Sumérgete en la simulación y descubre la belleza y complejidad de la vida en la naturaleza!</p>
              </div>
              <div className='vitals-container'>
                <div className='vitals-text-container'>
                  <h2>Frecuencia cardiaca: 90 P/min</h2>
                  <h2>Peso: 90 Kg</h2>
                </div>
                <div className='bars-container'>
                  <ProgressBar label="Hidratación" progress={progress1} />
                  <ProgressBar label="Energía" progress={progress2} />
                  <ProgressBar label="Saturación de oxígeno" progress={progress3} />
                  <ProgressBar label="Respiración" progress={progress4} />
                  <ProgressBar label="Temperatura corporal" progress={progress4} />
                </div>
              </div>
            </div>
            <aside>
              <div className='population-container'>
                <LineChart
                    xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
                    series={[
                        {
                        data: [2, 5.5, 2, 8.5, 1.5, 5],
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
                    data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
                    color: '#59a14f'
                  }
                ]}
              />
              </div>
            </aside>
            
        </div>
    )
}

export default Content