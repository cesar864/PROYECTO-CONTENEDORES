# Proyecto de Integración Continua - Entrega 1

Este proyecto crea dos contenedores con Docker:
- Una aplicación Flask (contenedor `web`)
- Una base de datos MySQL (contenedor `db`)

## Cómo ejecutar

1. Clona el repositorio.
2. Ejecuta:
   ```
   docker-compose up --build
   ```
3. Abre tu navegador en: [http://localhost:5000](http://localhost:5000)

## Verificación

La app intentará conectarse a la base de datos MySQL y mostrará un mensaje de éxito o error.
