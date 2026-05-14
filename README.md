<div align="center">

```
██╗   ██╗███████╗███████╗██╗  ██╗██╗   ██╗ █████╗
╚██╗ ██╔╝██╔════╝██╔════╝██║  ██║██║   ██║██╔══██╗
 ╚████╔╝ █████╗  ███████╗███████║██║   ██║███████║
  ╚██╔╝  ██╔══╝  ╚════██║██╔══██║██║   ██║██╔══██║
   ██║   ███████╗███████║██║  ██║╚██████╔╝██║  ██║
   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
```

### `Data Engineer` / `Full Stack Developer`

<br>

Data Engineer y desarrollador Full Stack con enfoque en la construccion de pipelines de datos,<br>
APIs REST y aplicaciones web de impacto real. Trabajo principalmente con Python y TypeScript,<br>
aplicando principios de arquitectura limpia tanto en proyectos de ingenieria de datos como<br>
en desarrollo de software.

Me interesa el cruce entre datos, estadistica aplicada e inteligencia artificial<br>como herramientas para resolver problemas concretos.

</div>

<br>

---

## Tecnologias

<br>

**Lenguajes**

![Python](https://img.shields.io/badge/Python-1a1a2e?style=flat-square&logo=python&logoColor=4fc3f7)
![TypeScript](https://img.shields.io/badge/TypeScript-1a1a2e?style=flat-square&logo=typescript&logoColor=4fc3f7)
![SQL](https://img.shields.io/badge/SQL-1a1a2e?style=flat-square&logo=postgresql&logoColor=4fc3f7)

<br>

**Ingenieria de Datos**

![Apache Airflow](https://img.shields.io/badge/Airflow-1a1a2e?style=flat-square&logo=apacheairflow&logoColor=4fc3f7)
![dbt](https://img.shields.io/badge/dbt-1a1a2e?style=flat-square&logo=dbt&logoColor=4fc3f7)
![Pandas](https://img.shields.io/badge/Pandas-1a1a2e?style=flat-square&logo=pandas&logoColor=4fc3f7)
![SQLite](https://img.shields.io/badge/SQLite-1a1a2e?style=flat-square&logo=sqlite&logoColor=4fc3f7)

<br>

**Backend**

![FastAPI](https://img.shields.io/badge/FastAPI-1a1a2e?style=flat-square&logo=fastapi&logoColor=4fc3f7)
![Node.js](https://img.shields.io/badge/Node.js-1a1a2e?style=flat-square&logo=node.js&logoColor=4fc3f7)

<br>

**Frontend**

![React](https://img.shields.io/badge/React-1a1a2e?style=flat-square&logo=react&logoColor=4fc3f7)
![Vite](https://img.shields.io/badge/Vite-1a1a2e?style=flat-square&logo=vite&logoColor=4fc3f7)

<br>

**Herramientas y entornos**

![Git](https://img.shields.io/badge/Git-1a1a2e?style=flat-square&logo=git&logoColor=4fc3f7)
![Docker](https://img.shields.io/badge/Docker-1a1a2e?style=flat-square&logo=docker&logoColor=4fc3f7)
![Linux](https://img.shields.io/badge/Linux-1a1a2e?style=flat-square&logo=linux&logoColor=4fc3f7)
![Power BI](https://img.shields.io/badge/Power_BI-1a1a2e?style=flat-square&logo=powerbi&logoColor=4fc3f7)

<br>

---

## Proyectos

<br>

<table>
<tr>
<td width="50%" valign="top">

### proyecto-monitoreo-posta-medica

Plataforma web full-stack para el monitoreo de indicadores de atencion medica en postas de salud. El sistema centraliza informacion operativa (registro de pacientes, tiempos de atencion y metricas clave) en un dashboard interactivo accesible desde el navegador.

El frontend esta construido en TypeScript con React y Vite. El backend expone una API REST en Python. Ambas capas estan desacopladas, lo que facilita el mantenimiento y la escalabilidad independiente de cada parte.

`TypeScript` `React` `Vite` `Python` `REST API`

</td>
<td width="50%" valign="top">

### article-prompter

Aplicacion frontend para la generacion de articulos asistida por inteligencia artificial. Permite al usuario ingresar parametros y obtener contenido generado mediante integracion con modelos de lenguaje.

Construida en TypeScript puro, con un nivel de tipado estricto que refleja buenas practicas de desarrollo en proyectos de produccion. La estructura del proyecto separa la logica de integracion con la API del componente visual, facilitando el mantenimiento y la extension de funcionalidades.

El proyecto demuestra manejo de llamadas asincronicas, estados de carga, manejo de errores y construccion de interfaces orientadas a flujos de entrada y salida de texto.

`TypeScript` `LLM Integration` `Async` `Error Handling`

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### pipeline-datos-deportivos

Pipeline de datos de extremo a extremo para analisis predictivo de la Liga 1 Peru. Implementa la Arquitectura Medallion en tres capas diferenciadas:

```
BRONZE  →  extraccion desde FBRef via web scraping (requests, BeautifulSoup)
           rate limiting · retry backoff · rotacion de User-Agent

SILVER  →  limpieza, normalizacion de nombres, parsing de fechas,
           validacion de rangos, deduplicacion

GOLD    →  feature engineering · rolling averages (ultimos 5 partidos)
           fuerza de ataque y defensa relativa a la liga
```

El modelo predictivo aplica la distribucion de Poisson con correccion Dixon-Coles para resultados de pocos goles, produciendo probabilidades 1X2 y un ranking de los marcadores mas probables para cualquier enfrentamiento. Este es el mismo modelo estadistico utilizado como base por casas de apuestas europeas.

Las tres capas se persisten en SQLite y el pipeline exporta CSVs listos para consumir en Power BI. Incluye una CLI con flags para ejecutar capas individuales o lanzar predicciones directamente desde la terminal.

`Python` `SQLite` `BeautifulSoup` `Poisson` `Dixon-Coles` `Medallion Architecture` `Power BI` `CLI`

</td>
</tr>
</table>

<br>

---

## Contacto

<div align="center">

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-1a1a2e?style=for-the-badge&logo=linkedin&logoColor=4fc3f7)](https://linkedin.com)
[![Gmail](https://img.shields.io/badge/Gmail-1a1a2e?style=for-the-badge&logo=gmail&logoColor=4fc3f7)](mailto:tucorreo@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-1a1a2e?style=for-the-badge&logo=github&logoColor=4fc3f7)](https://github.com)

<br>

</div>
