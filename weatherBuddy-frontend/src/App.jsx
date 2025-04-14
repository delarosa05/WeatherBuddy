import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import './App.css'
import "../src/pages/register"
import "../src/pages/login";
import LoginPage from "../src/pages/login";
import MeasuresPage from "./pages/measure";
import InicioPage from "./pages/inicio";
import Cabecera from "./componentes extras/cabecera";
import Pie_Pagina from "./componentes extras/pie_Pagina";
function App() {
  return (
    <BrowserRouter>
    <Cabecera />
      <Routes>
        <Route path="/" element={<Navigate to="/register" />} />  //Navigate para redirecciona a /register 
        <Route path= "/register" element={<register />}/> //devuelve la pagina register.jsx cuando accedemos a /register
        <Route path="/login" element={<LoginPage />}/>
        <Route path="/measures" element={<MeasuresPage/>}/>
        <Route path="/inicio" element={<InicioPage/>}/>
      </Routes>
    <Pie_Pagina />
    </BrowserRouter>
  )
}

export default App
