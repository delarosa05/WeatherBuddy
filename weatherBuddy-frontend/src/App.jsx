import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import './App.css'
import "../src/pages/register"
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/register" />} />  //Navigate para redirecciona a /register 
        <Route path= "/register" element={<register />}/> //devuelve la pagina register.jsx cuando accedemos a /register
      </Routes>
    </BrowserRouter>
  )
}

export default App
