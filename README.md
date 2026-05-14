<div align="center">Yeshua Chavez
Data Engineer y desarrollador Full Stack con enfoque en la construccion de pipelines de datos, APIs REST y aplicaciones web de impacto real. Trabajo principalmente con Python y TypeScript, aplicando principios de arquitectura limpia tanto en proyectos de ingenieria de datos como en desarrollo de software.
Me interesa el cruce entre datos, estadistica aplicada e inteligencia artificial como herramientas para resolver problemas concretos.
</div>Tecnologias
Lenguajes
Ingenieria de Datos
Backend
Frontend
Herramientas y entornos
Proyectos
<table>
<tr>
<td width="50%" valign="top">proyecto-monitoreo-posta-medica
Plataforma web full-stack para el monitoreo de indicadores de atencion medica en postas de salud. El sistema centraliza informacion operativa (registro de pacientes, tiempos de atencion y metricas clave) en un dashboard interactivo accesible desde el navegador.
El frontend esta construido en TypeScript con React y Vite. El backend expone una API REST en Python. Ambas capas estan desacopladas, lo que facilita el mantenimiento y la escalabilidad independiente de cada parte.
</td>
<td width="50%" valign="top">article-prompter
Aplicacion frontend para la generacion de articulos asistida por inteligencia artificial. Permite al usuario ingresar parametros y obtener contenido generado mediante integracion con modelos de lenguaje.
Construida en TypeScript puro, con un nivel de tipado estricto que refleja buenas practicas de desarrollo en proyectos de produccion. La estructura del proyecto separa la logica de integracion con la API del componente visual, facilitando el mantenimiento y la extension de funcionalidades.
El proyecto demuestra manejo de llamadas asincronicas, estados de carga, manejo de errores y construccion de interfaces orientadas a flujos de entrada y salida de texto.
</td>
</tr>
<tr>
<td colspan="2" valign="top">pipeline-datos-deportivos
Pipeline de datos de extremo a extremo para analisis predictivo de la Liga 1 Peru. Implementa la Arquitectura Medallion en tres capas diferenciadas:
Bronze: extraccion de datos desde FBRef via web scraping con requests y BeautifulSoup, con rate limiting, retry backoff y rotacion de User-Agent para respetar al servidor
Silver: limpieza, normalizacion de nombres de equipos, parsing de fechas en multiples formatos, validacion de rangos y deduplicacion
Gold: feature engineering con metricas agregadas por equipo, rolling averages de los ultimos 5 partidos, y calculo de fuerza de ataque y defensa relativa a la liga
El modelo predictivo aplica la distribucion de Poisson con correccion Dixon-Coles para resultados de pocos goles, produciendo probabilidades 1X2 y un ranking de los marcadores mas probables para cualquier enfrentamiento. Este es el mismo modelo estadistico utilizado como base por casas de apuestas europeas.
Las tres capas se persisten en SQLite y el pipeline exporta CSVs listos para consumir en Power BI. Incluye una CLI con flags para ejecutar capas individuales o lanzar predicciones directamente desde la terminal.
</td>
</tr>
</table>Contacto
<div align="center">
</div>
