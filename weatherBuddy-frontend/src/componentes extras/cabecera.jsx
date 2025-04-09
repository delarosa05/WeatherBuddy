import React from "react";
import "./cabecera.css"

const Cabecera = () => {
    return (
        <header className="cabecera">
            <div className="cabecera-contenido">
                <div className="cabecera-logo"></div> {/* Contenedor para el logo */}
                <h1 className="cabecera-titulo">WeatherBuddy</h1>
            </div>
            <div className="cabecera-boton-contenedor">
                <a href="/login" className="cabecera-boton">Iniciar Sesión</a>
            </div>
        </header>
    );
};

export default Cabecera;