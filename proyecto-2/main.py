from datetime import datetime
import zoneinfo

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def inicio ():
    return{"mensaje": "Aprendiendo fastapi"}

@app.get("/saludo/{nombre}")
def saludo(nombre):
    return {"mensaje": f"Mi nombre es: {nombre}"}

# Crear otro endpoint, que me muestre la hora actual del 
# servidor, debe importar el modulo datetime.
@app.get("/horas")
def horas():
    return {"Hora": datetime.now()} 

ciudades = {
    "AR": "America/Argentina/Buenos_Aires",
    "GT": "America/Guatemala",
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "ES": "España",
    "CL": "Chile"
}

@app.get("/hora/{iso_code}")
def hora(iso_code):
    clave = iso_code.upper()
    zona_ciudad = ciudades.get(clave)
    tiempo_zona = zoneinfo.ZoneInfo(zona_ciudad)
    return {"Hora": datetime.now(tiempo_zona)}



@app.get("/hora/{iso_code}")
def hora(iso_code):
    clave = iso_code.upper()
    zona_ciudad = ciudades.get(clave)
    
    # CORRECCIÓN AQUÍ: Usamos zona_ciudad para crear el objeto ZoneInfo
    tiempo_zona = zoneinfo.ZoneInfo(zona_ciudad)
    
    return {"Hora": datetime.now(tiempo_zona)}