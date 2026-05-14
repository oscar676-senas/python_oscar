# Reporte de Proyecto: API REST Comercial

## 🧑‍💻 Información del Aprendiz
*   **Nombre:** Oscar Andrés Navarro Ochoa
*   **Ficha:** 3407184
*   **Trabajo:** Proyecto Clientes

---

## 📌 Resumen del Trabajo
Diseñamos y construimos una **API REST comercial** utilizando **FastAPI** y **Pydantic**. El sistema gestiona de forma interactiva tres entidades enlazadas mediante objetos complejos:

*   **Clientes:** Permite registrar usuarios ocultando el campo `id` en el formulario para calcularlo de forma automatizada y secuencial en el servidor. Incluye operaciones completas de lectura, actualización (`PUT`) y eliminación (`DELETE`).
*   **Facturas:** Entidad que registra ventas asociando la fecha/hora automática, un valor monetario y el objeto de un `Cliente` completo.
*   **Transacciones:** Módulo financiero que registra descripciones contables vinculadas directamente a una `Factura` específica.

---

## 🛠️ Configuración del Entorno de Desarrollo

### 1. Creación del Entorno Virtual (`venv`)
El entorno virtual crea una carpeta aislada que contendrá únicamente las librerías que este proyecto necesita.

*   **Comando ejecutado:**
    ```bash
    python -m venv venv
    ```

*   **Activación según el sistema operativo:**
    *   **Windows (CMD / PowerShell):**
        ```powershell
        venv\Scripts\activate
        ```
    *   **Mac / Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   *Nota: Sabemos que está activo porque aparece la palabra `(venv)` al inicio de la línea de comandos en la terminal.*

### 2. Instalación de FastAPI y sus Dependencias
Instalamos el paquete completo estándar para asegurar que todas las herramientas de desarrollo y servidores locales estén disponibles inmediatamente.

*   **Comando ejecutado:**
    ```bash
    pip install "fastapi[standard]"
    ```
    *Nota: Este comando instala automáticamente FastAPI, Pydantic (para la validación de datos) y Uvicorn (el servidor web ASGI que procesa las peticiones).*

### 3. Ejecución del Servidor de Desarrollo
Para arrancar el proyecto en tiempo real y habilitar el reinicio automático cada vez que guardas un archivo, utilizamos la interfaz de comandos moderna de FastAPI:

*   **Comando ejecutado:**
    ```bash
    fastapi dev main.py
    ```

El servidor levanta localmente y nos entrega el acceso a la documentación interactiva autogenerada (Swagger UI) a través de la dirección **`127.0.0`**, lugar donde validamos visualmente el comportamiento de cada endpoint.
