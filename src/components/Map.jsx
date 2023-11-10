import React, { useEffect, useRef } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';


const Map = () => {
  const chartRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      const mapData = await fetch(
        'https://code.highcharts.com/mapdata/custom/world.topo.json'
      ).then(response => response.json());

      const data = await fetch(
        'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json'
      ).then(response => response.json());

      // Initialize the chart
      if (chartRef.current) {
        chartRef.current.chart.mapChart({
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
    <div>
      <HighchartsReact
        highcharts={Highcharts}
        options={{ /* Opciones iniciales del gráfico */ }}
        ref={chartRef}
      />
    </div>
  );
};

export default Map;
