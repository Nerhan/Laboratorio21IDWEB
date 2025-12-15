import threading
import asyncio
import multiprocessing
import time
import random

def consulta_bd_sincrona(nombre, id_consulta):
    """Simula una consulta a BD con tiempo variable"""
    tiempo_respuesta = random.uniform(1, 5)
    print(f"[{nombre}] Consulta {id_consulta} iniciada. Tiempo estimado: {tiempo_respuesta:.2f}s")
    time.sleep(tiempo_respuesta)
    print(f"[{nombre}] Consulta {id_consulta} completada en {tiempo_respuesta:.2f}s")
    return tiempo_respuesta

def ejecutar_con_hilos():
    print("\n=== EJECUTANDO CON HILOS ===")
    inicio = time.time()
    
    hilos = []
    for i in range(1, 4):
        hilo = threading.Thread(target=consulta_bd_sincrona, args=("HILO", i))
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos:
        hilo.join()
    
    total = time.time() - inicio
    print(f"Tiempo total con hilos: {total:.2f} segundos")
    return total

async def consulta_bd_asincrona(nombre, id_consulta):
    tiempo_respuesta = random.uniform(1, 5)
    print(f"[{nombre}] Consulta {id_consulta} iniciada. Tiempo estimado: {tiempo_respuesta:.2f}s")
    await asyncio.sleep(tiempo_respuesta)
    print(f"[{nombre}] Consulta {id_consulta} completada en {tiempo_respuesta:.2f}s")
    return tiempo_respuesta

async def ejecutar_asincrono():
    print("\n=== EJECUTANDO CON ASYNCIO ===")
    inicio = time.time()
    
    tareas = [
        consulta_bd_asincrona("ASYNC", 1),
        consulta_bd_asincrona("ASYNC", 2),
        consulta_bd_asincrona("ASYNC", 3)
    ]
    
    resultados = await asyncio.gather(*tareas)
    
    total = time.time() - inicio
    print(f"Tiempo total con asyncio: {total:.2f} segundos")
    return total

def ejecutar_con_procesos():
    print("\n=== EJECUTANDO CON PROCESOS ===")
    inicio = time.time()
    
    procesos = []
    for i in range(1, 4):
        proceso = multiprocessing.Process(
            target=consulta_bd_sincrona, 
            args=("PROCESO", i)
        )
        procesos.append(proceso)
        proceso.start()
    
    for proceso in procesos:
        proceso.join()
    
    total = time.time() - inicio
    print(f"Tiempo total con procesos: {total:.2f} segundos")
    return total

def ejecutar_secuencial():
    print("\n=== EJECUTANDO SECUENCIALMENTE ===")
    inicio = time.time()
    
    for i in range(1, 4):
        consulta_bd_sincrona("SECUENCIAL", i)
    
    total = time.time() - inicio
    print(f"Tiempo total secuencial: {total:.2f} segundos")
    return total

if __name__ == "__main__":
    print("=== SIMULACIÓN DE CONSULTAS A BASE DE DATOS ===")
    print("Cada consulta tarda entre 1 y 5 segundos\n")
    
    tiempos = {}
    
    tiempos['secuencial'] = ejecutar_secuencial()
    tiempos['hilos'] = ejecutar_con_hilos()
    tiempos['asyncio'] = asyncio.run(ejecutar_asincrono())
    tiempos['procesos'] = ejecutar_con_procesos()
    
    print("\n" + "="*50)
    print("COMPARACIÓN DE TIEMPOS:")
    print("="*50)
    for metodo, tiempo in tiempos.items():
        print(f"{metodo.upper():<15}: {tiempo:.2f} segundos")
    
    mas_rapido = min(tiempos, key=tiempos.get)
    print(f"\nMétodo más rápido: {mas_rapido} ({tiempos[mas_rapido]:.2f}s)")