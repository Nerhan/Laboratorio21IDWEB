import json

def crear_equipos_futbol():
    """Crea una lista de diccionarios con equipos de fútbol"""
    equipos = [
        {
            "Nombre": "Real Madrid",
            "País": "España",
            "nivelAtaque": 92,
            "nivelDefensa": 88
        },
        {
            "Nombre": "Barcelona",
            "País": "España", 
            "nivelAtaque": 90,
            "nivelDefensa": 85
        },
        {
            "Nombre": "Bayern Munich",
            "País": "Alemania",
            "nivelAtaque": 91,
            "nivelDefensa": 89
        },
        {
            "Nombre": "Manchester City",
            "País": "Inglaterra",
            "nivelAtaque": 93,
            "nivelDefensa": 87
        },
        {
            "Nombre": "Melgar",
            "País": "Perú",
            "nivelAtaque": 100,
            "nivelDefensa": 100
        }
    ]
    return equipos

if __name__ == "__main__":
    # Crear lista de equipos
    equipos = crear_equipos_futbol()
    
    # Convertir a JSON con formato legible
    json_string = json.dumps(equipos, indent=2, ensure_ascii=False)
    
    print("=== Equipos de Fútbol en JSON ===")
    print(json_string)
    
    # Guardar en archivo (opcional)
    with open("equipos_futbol.json", "w", encoding="utf-8") as f:
        json.dump(equipos, f, indent=2, ensure_ascii=False)
    
    print("\nArchivo 'equipos_futbol.json' creado exitosamente.")