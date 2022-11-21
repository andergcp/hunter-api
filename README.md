# API - Proceso Backend Developer

API para la consulta y administración de Usuarios, Empresas y Empleos.
Desarrollada por Anderson Castiblanco (https://www.linkedin.com/in/andergcp/)

**ps:** Le hunter-api no por equivocación :) , es porque algunas empresas prefieren que no se mencione su nombre en los repos públicos de pruebas técnicas :)

## Ejecuta la aplicación usando un contenedor de Docker.

1. Descarga el repositorio, si tienes instalado git usa el siguiente comando desde tu terminal: `git clone https://github.com/andergcp/hunter-api.git`
2. Desde tu terminal ve a la carpeta del proyecto que acabas de descargar.
3. Verifica que tengas instalado y corriendo Docker en tu computador. 
4. Contruye la imagen de docker usando el comando desde tu terminal: `docker build -t ander-hunty-api .`
5. Crea el contendor basado en la imagen creada, con este comando desde tu terminal: `docker run -dp 8000:8000 ander-hunty-api`
6. Una vez el contenedor esté corriendo, podrás enviar requests a la Api desde la ruta http://127.0.0.1:8000 en tu local. Visita la documentación de la api para más detalles.

## Documentación de la API
Encuentra la documentación de la API en: https://elements.getpostman.com/redirect?entityId=13424395-e166430e-6966-43f7-889b-7efe1a801b3c&entityType=collection



