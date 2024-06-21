-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS miapp;
-- Usar la base de datos
USE miapp;
-- Crear la tabla de Productos si no existe
CREATE TABLE IF NOT EXISTS coristas (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    apellido VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    cuerda VARCHAR(255) NOT NULL,
    experiencia BOOLEAN,
    lectura_musical BOOLEAN,
    estudios_musicales BOOLEAN,
    activo BOOLEAN);