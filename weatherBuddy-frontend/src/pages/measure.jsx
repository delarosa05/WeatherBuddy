// pages/MeasuresPage.jsx

import { useState, useEffect } from "react";
// import { fetchMeasures } from "../api/MeasureEndpoints";  // Importamos la función para obtener las medidas
import "./measure.css";

const MeasuresPage = () => {
  const [measure, setMeasure] = useState(null); // Estado para almacenar la medida
  const [error, setError] = useState("");

    // Datos mock para simular la API de medidas
    const mockMeasures = [
      {
        light_level: 350, // Nivel de iluminación en lux
        pressure_level: 1012, // Presión en hPa
        temperature: 24, // Temperatura en grados Celsius
        humidity_level: 55, // Humedad en porcentaje
        createdAt: new Date().toISOString(), // Fecha actual
      },
    ];
    // ESTO ESTÁ COMENTADO PARA PODER PROBAR CON EL MOCK
  // useEffect(() => {
  //   // Función para obtener las medidas más recientes
  //   const getMeasures = async () => {
  //     try {
  //       const measures = await fetchMeasures();  // Llamamos a la API
  //       if (measures && measures.length > 0) {
  //         setMeasure(measures[0]);  // Guardamos la medida más reciente en el estado
  //       }
  //     } catch (error) {
  //       setError("Error al obtener las medidas: " + error);
  //     }
  //   };

  //   getMeasures();
  // }, []);  // Se ejecuta solo una vez cuando el componente se monta

  useEffect(() => {
    // Función para obtener las medidas más recientes
    const getMeasures = async () => {
      try {
        // Simulamos la llamada a la API con datos mock
        const measures = mockMeasures; // Aquí usamos los datos ficticios en lugar de la API
        if (measures && measures.length > 0) {
          setMeasure(measures[0]); // Guardamos la medida más reciente en el estado
        }
      } catch (error) {
        setError("Error al obtener las medidas: " + error); // Manejo del error
      }
    };

    getMeasures();
  }, []); // Se ejecuta solo una vez cuando el componente se monta

  return (
    <div className="measure-page">
      <div className="header-container">
        <h2>Últimas Medidas</h2>
        {measure && <p>Fecha: {new Date(measure.createdAt).toLocaleString()}</p>}
      </div>
      
      {error && <p className="error">{error}</p>}

      {/* Aquí continuarás con el resto de los elementos */}
    {/* Contenedor para las medidas */}
    <div className="measure-row">
    <div className="measure-card">
      <p><strong>Iluminación:</strong> {measure?.light_level} lux</p>
    </div>
    <div className="measure-card">
      <p><strong>Presión:</strong> {measure?.pressure_level} hPa</p>
    </div>
    <div className="measure-card">
      <p><strong>Temperatura:</strong> {measure?.temperature} °C</p>
    </div>
    <div className="measure-card">
      <p><strong>Humedad:</strong> {measure?.humidity_level} %</p>
    </div>
  </div>
  </div>
  );
};


export default MeasuresPage;
