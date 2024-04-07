import requests

url = "http://localhost:8000/pizzas"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_paciente = {
    
        "ci": 789481,
        "nombre": "Pepe",
        "apellido": "Peñas",
        "edad": 21,
        "genero": "masculino",
        "diagnostico": "miopia",
        "doctor": "juanito"
    
}
response = requests.post(url, json=mi_paciente, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
edit_paciente = {
    "ci": 789481,
    "nombre": "Pepe",
    "apellido": "Peñas",
    "edad": 21,
    "genero": "masculino",
    "diagnostico": "miopia",
    "doctor": "juan Palomera"
}
response = requests.put(url, json=edit_paciente, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())