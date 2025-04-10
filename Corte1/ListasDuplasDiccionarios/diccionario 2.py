building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])
print(building_heights["Ping An"])

zodiac_elements = {
    "agua": ["Cáncer", "Escorpio", "Piscis"],
    "fuego": ["Aries", "Leo", "Sagitario"],
    "tierra": ["Tauro", "Virgo", "Capricornio"],
    "aire": ["Géminis", "Libra", "Acuario"]
}

print(zodiac_elements["tierra"])
print(zodiac_elements["fuego"])
key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights[key_to_check])
else:
    print(f"{key_to_check} no está en el diccionario.")

zodiac_elements["energía"] = "No es un elemento zodiacal"

if "energía" in zodiac_elements:
    print(zodiac_elements["energía"])
print(building_heights.get("Shanghai Tower"))  # Retorna 632
print(building_heights.get("Mi Casa"))         # Retorna None

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
raffle = {
    223842: "Osito de Peluche",
    872921: "Entradas de Concierto",
    320291: "Canasta de Regalos",
    412123: "Collar",
    298787: "Máquina de Pasta"
}

print(raffle.pop(320291, "Sin premio"))  # Elimina "Canasta de Regalos"
print(raffle)

print(raffle.pop(100000, "Sin premio"))  # Clave inexistente
print(raffle)

print(raffle.pop(872921, "Sin premio"))  # Elimina "Entradas de Concierto"
print(raffle)
available_items = {
    "poción de salud": 10,
    "pastel de la cura": 5,
    "elixir verde": 20,
    "sándwich de fuerza": 25,
    "granos de resistencia": 15,
    "estofado de poder": 30
}

puntos_salud = 20

puntos_salud += available_items.pop("granos de resistencia", 0)
puntos_salud += available_items.pop("estofado de poder", 0)
puntos_salud += available_items.pop("pan místico", 0)  # No existe

print(available_items)
print(puntos_salud)
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

for estudiante in test_scores.keys():
    print(estudiante)

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}

print(user_ids.keys())
print(num_exercises.keys())
for notas in test_scores.values():
    print(notas)

total_ejercicios = sum(num_exercises.values())
print(total_ejercicios)
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for empresa, valor in biggest_brands.items():
    print(f"{empresa} tiene un valor de {valor} mil millones de dólares.")

pct_mujeres_por_ocupacion = {
    "CEO": 28,
    "Gerente de Ingeniería": 9,
    "Farmacéutico": 58,
    "Médico": 40,
    "Abogado": 37,
    "Ingeniero Aeroespacial": 9
}

for ocupacion, porcentaje in pct_mujeres_por_ocupacion.items():
    print(f"Las mujeres representan el {porcentaje}% de los/as {ocupacion}s.")