import React, {useState, useEffect, useRef} from 'react'
import { LineChart } from '@mui/x-charts/LineChart';
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import HighCharts3D from 'highcharts/highcharts-3d'
import Plot from 'react-plotly.js';
import Map from './Map';

import './Content.css'

if (typeof Highcharts === 'object') {
    HighCharts3D(Highcharts)
} 


const options = {
    chart: {
        type: 'scatter3d',
        options3d: {
          enabled: true,
          alpha: 13,
          beta: 31,
          depth: 1000,
          viewDistance: 10,
          frame: {
            bottom: {
              size: 1,
              color: 'rgba(0,255,0,0.1)'
            }
          }
        },
        height:'60%',
    },
    title: {
        text: ''
    },
    yAxis: {
        min: 0,
        max: 10
    },
    xAxis: {
        min: 0,
        max: 10,
        gridLineWidth: 1
    },
    zAxis: {
        min: 0,
        max: 10,
        showFirstLabel: false
    },
    series: [{
        data: [
        // [X, Y, Z]
        [1, 0, 1],
        [1, 0, 2],
        [1, 0, 5],
        [2, 0, 2],
        [2, 0, 4],
        [4, 0, 7],
        [4, 0, 8],
        [7, 0, 3],
        [7, 0, 5],
        [8, 0, 5]
        ]
    }]
}

function Content() {

  const chartRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      const mapData = await fetch(
        'https://code.highcharts.com/mapdata/custom/world.topo.json'
      ).then(response => response.json());
  
      const data = await fetch(
        'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json'
      ).then(response => response.json());
  
      // Accede al gráfico directamente a través de chartRef.current
      if (chartRef.current) {
        chartRef.current.chart.update({
          title: {
            text: 'Predefined zoomed area'
          },
  
          mapNavigation: {
            enabled: true,
            buttonOptions: {
              verticalAlign: 'bottom'
            }
          },
  
          mapView: {
            projection: {
              name: 'WebMercator'
            },
            center: [10, 58],
            zoom: 2.8
          },
  
          colorAxis: {
            min: 1,
            max: 1000,
            type: 'logarithmic'
          },
  
          legend: {
            title: {
              text: 'Population density per km²'
            }
          },
  
          series: [{
            data,
            mapData,
            joinBy: ['iso-a2', 'code'],
            name: 'Population density',
            tooltip: {
              valueSuffix: '/km²'
            }
          }]
        });
      }
    };
  
    fetchData();
  }, []);
    
    return (
        <div className='content-container'>
            <div className='map-container'>
            <HighchartsReact
              highcharts={Highcharts}
              options={{ /* Opciones iniciales del gráfico */ }}
              ref={chartRef}
            />
            </div>
            <aside>
              <div className='vitals-container'>
                <LineChart
                    xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
                    series={[
                        {
                        data: [2, 5.5, 2, 8.5, 1.5, 5],
                        },
                    ]}
                />
              </div>
              <div className='image-container'>
                <HighchartsReact className='chart' highcharts={Highcharts} options = {options}></HighchartsReact>
              </div>
            </aside>
            
        </div>
    )
}

export default Content