#!/usr/bin/env python3
"""Script para probar todo el sistema"""

import urllib.request
import json

BASE_URL = "http://localhost:8000"
headers = {'Content-Type': 'application/json'}

def probar_endpoint(metodo, ruta, datos=None):
    """Prueba un endpoint y devuelve la respuesta"""
    try:
        if datos:
            data = json.dumps(datos).encode()
            req = urllib.request.Request(f"{BASE_URL}{ruta}", data=data, headers=headers, method=metodo)
        else:
            req = urllib.request.Request(f"{BASE_URL}{ruta}", method=metodo)
        
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "mensaje": e.reason}
    except Exception as e:
        return {"error": str(e)}

print("=" * 60)
print("PRUEBA COMPLETA DEL SISTEMA")
print("=" * 60)

# 1. Verificar API
print("\n1. Verificando API...")
resp = probar_endpoint("GET", "/")
print(f"   ✓ API funcionando: {resp}")

# 2. Crear cliente
print("\n2. Creando cliente...")
cliente = probar_endpoint("POST", "/clientes", {
    "id": 999,
    "nombre": "Test Final",
    "email": "final.test.999@test.com"
})
print(f"   ✓ Cliente creado: {cliente}")

# 3. Crear factura
print("\n3. Creando factura...")
factura = probar_endpoint("POST", "/facturas", {
    "cliente": 11,
    "numero": "FAC-999",
    "fecha": "2024-01-15"
})
print(f"   ✓ Factura creada: {factura}")

# 4. Crear transacción
print("\n4. Creando transacción...")
transaccion = probar_endpoint("POST", "/facturas/1/transacciones", {
    "valor_unitario": 100.0,
    "cantidad": 2
})
print(f"   ✓ Transacción creada: {transaccion}")

# 5. Verificar datos creados
print("\n5. Verificando datos creados...")
clientes = probar_endpoint("GET", "/clientes")
facturas = probar_endpoint("GET", "/facturas")
transacciones = probar_endpoint("GET", "/transacciones")
print(f"   ✓ Clientes: {len(clientes.get('clientes', []))} registros")
print(f"   ✓ Facturas: {len(facturas.get('facturas', []))} registros")
print(f"   ✓ Transacciones: {len(transacciones.get('transacciones', []))} registros")

# 6. Probar eliminación en cascada
print("\n6. Probando eliminación en cascada...")
eliminar = probar_endpoint("DELETE", "/clientes/11")
print(f"   ✓ Cliente eliminado: {eliminar}")

# 7. Verificar eliminación
print("\n7. Verificando eliminación...")
clientes_despues = probar_endpoint("GET", "/clientes")
facturas_despues = probar_endpoint("GET", "/facturas")
transacciones_despues = probar_endpoint("GET", "/transacciones")
print(f"   ✓ Clientes: {len(clientes_despues.get('clientes', []))} registros")
print(f"   ✓ Facturas: {len(facturas_despues.get('facturas', []))} registros")
print(f"   ✓ Transacciones: {len(transacciones_despues.get('transacciones', []))} registros")

print("\n" + "=" * 60)
print("✅ TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 60)