// api/UserEndpoints.js
import axios from "axios";

// Función para obtener la última medida del usuario autenticado
export const fetchMeasures = async () => {
  const token = localStorage.getItem("access");  // Obtener el token de localStorage
  if (!token) {
    throw new Error("No se encontró un token de acceso.");
  }

  try {
    const response = await axios.get('http://localhost:8000/main/myMeasures/', {
      headers: {
        Authorization: `Bearer ${token}`  // Enviar el token en el encabezado
      }
    });
    return response.data;  // Retorna los datos de la respuesta
  } catch (error) {
    throw new Error("Error al obtener las medidas: " + error.message);
  }
};
