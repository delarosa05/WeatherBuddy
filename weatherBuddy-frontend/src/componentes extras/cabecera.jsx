import React from "react";
import "./cabecera.css"

const Cabecera = () => {
    return (
        <header className="cabecera">
            <div className="cabecera-contenido">
            <a href="/inicio" className="cabecera-link">
                    <div className="cabecera-logo"></div> {/* Contenedor para el logo */}
                    <h1 className="cabecera-titulo">WeatherBuddy</h1>
                </a>
            </div>
            <div className="cabecera-boton-contenedor">
                <a href="/login" className="cabecera-boton">Iniciar Sesión</a>
            </div>
        </header>
    );
};

export default Cabecera;