// pages/LoginPage.jsx
import { useState } from "react";
import { login } from "../api/UserEndpoints"; // Importa la función del servicio
import { useNavigate } from "react-router-dom"

const LoginPage = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();
  
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); // Limpia los errores al intentar hacer login
    setSuccess(""); // Limpia los mensajes de éxito
    try {
      const data = await login(formData.email, formData.password); // Llama al servicio de login
      localStorage.setItem("access", data.access); // Guarda el token en localStorage
      localStorage.setItem("refresh", data.refresh);
      setSuccess("Inicio de sesión exitoso!");
      navigate('/measures')
    } catch (err) {
      setError(err.message); // Muestra el error si las credenciales son incorrectas
    }
  };

  return (

    <div style={styles.container}>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          name="email"
          placeholder="Usuario"
          value={formData.email}
          onChange={handleChange}
          style={styles.input}
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={formData.password}
          onChange={handleChange}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Entrar</button>
      </form>
      {error && <p style={styles.error}>{error}</p>}
      {success && <p style={styles.success}>{success}</p>}
      <p>Aun no tienes cuenta  <a href="/register">Create una!</a></p>
    </div>
    
  );
};

const styles = {
  container: {
    maxWidth: "400px",
    margin: "100px auto",
    padding: "2rem",
    border: "1px solid #ddd",
    borderRadius: "8px",
    textAlign: "center",
    backgroundColor: "#f9f9f9",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1rem",
  },
  input: {
    padding: "0.8rem",
    fontSize: "1rem",
  },
  button: {
    padding: "0.8rem",
    backgroundColor: "#007bff",
    color: "#fff",
    border: "none",
    fontWeight: "bold",
    cursor: "pointer",
  },
  error: {
    color: "red",
    marginTop: "1rem",
  },
  success: {
    color: "green",
    marginTop: "1rem",
  },
};

export default LoginPage;
