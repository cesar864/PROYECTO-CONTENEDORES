# Proyecto de Integración Continua con Docker

Este proyecto consiste en una aplicación web desarrollada con Flask que se conecta a una base de datos MySQL, ambos ejecutándose en contenedores Docker orquestados con Docker Compose.

## Tecnologías

- Python / Flask
- MySQL
- Docker
- Docker Compose

## Estructura del Proyecto

- `/app`: Código fuente de la aplicación Flask.
- `Dockerfile`: Construye la imagen de la app.
- `docker-compose.yml`: Orquesta la aplicación y la base de datos.

## ¿Cómo ejecutar?

1. Clona el repositorio:
   ```bash
   git clone https://github.com/cesar864/PROYECTO-CONTENEDORES.git
   cd PROYECTO-CONTENEDORES
   ```

2. Ejecuta los contenedores:
   ```bash
   docker-compose up
   ```

3. Accede a la aplicación:
   - Visita `http://localhost:5000` para verificar que la app está conectada a MySQL correctamente.

## Autoría

Trabajo realizado como parte del módulo Énfasis Profesional I del Politécnico Grancolombiano.

