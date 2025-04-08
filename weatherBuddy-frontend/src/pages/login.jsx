// pages/LoginPage.jsx
import { useState,useEffect } from "react";
import { login } from "../api/UserEndpoints"; // Importa la función del servicio
import { useNavigate } from "react-router-dom"
import "./login.css"

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
    useEffect(() => {
        document.body.className = "login-page"; // Añade la clase 'login-page' al body
        return () => {
            document.body.className = ""; // Limpia la clase al salir de la página
        };
    }, []);

  return (
    <div className="container">
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          name="email"
          placeholder="Usuario"
          value={formData.email}
          onChange={handleChange}
          className="input"
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={formData.password}
          onChange={handleChange}
          className="input"
        />
        <button type="submit" className="button">Entrar</button>
      </form>
      {error && <p className="error">{error}</p>}
      {success && <p className="success">{success}</p>}
      <p>Aun no tienes cuenta <a href="/register">¡Crea una!</a></p>
    </div>
  );
};


export default LoginPage;
