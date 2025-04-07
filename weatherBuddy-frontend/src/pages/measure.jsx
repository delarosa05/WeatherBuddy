// pages/MeasuresPage.jsx

import { useState, useEffect } from "react";
import { fetchMeasures } from "../api/MeasureEndpoints";  // Importamos la función para obtener las medidas

const MeasuresPage = () => {
  const [measure, setMeasure] = useState(null); // Estado para almacenar la medida
  const [error, setError] = useState("");

  useEffect(() => {
    // Función para obtener las medidas más recientes
    const getMeasures = async () => {
      try {
        const measures = await fetchMeasures();  // Llamamos a la API
        if (measures && measures.length > 0) {
          setMeasure(measures[0]);  // Guardamos la medida más reciente en el estado
        }
      } catch (error) {
        setError("Error al obtener las medidas: " + error);
      }
    };

    getMeasures();
  }, []);  // Se ejecuta solo una vez cuando el componente se monta

  return (
    <div style={styles.container}>
      <h2>Última Medida</h2>

      {error && <p style={styles.error}>{error}</p>}

      {measure ? (
        <div>
          <p><strong>Iluminación:</strong> {measure.light_level} lux</p>
          <p><strong>Presión:</strong> {measure.pressure_level} hPa</p>
          <p><strong>Temperatura:</strong> {measure.temperature} °C</p>
          <p><strong>Humedad:</strong> {measure.humidity_level} %</p>
          <p><strong>Fecha:</strong> {new Date(measure.createdAt).toLocaleString()}</p>
        </div>
      ) : (
        <p>Cargando medida...</p>
      )}
    </div>
  );
};

const styles = {
  container: {
    maxWidth: "600px",
    margin: "50px auto",
    padding: "2rem",
    border: "1px solid #ddd",
    borderRadius: "8px",
    textAlign: "center",
    backgroundColor: "#f9f9f9",
  },
  error: {
    color: "red",
    marginTop: "1rem",
  },
};

export default MeasuresPage;
