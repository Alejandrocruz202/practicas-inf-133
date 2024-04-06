import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL para crear nuevo planta
query_crear = """
mutation {
        crearPlanta(nombre: "manzano", especie: "Malus domestica", edad: 25 ,altura: 300, frutos:"True") {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print("-----------------------------crear---------------------------------------------")
print(response_mutation.text)

# Definir la consulta GraphQL simple
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""

response = requests.post(url, json={'query': query_lista})
print("--------------------------------listar-------------------------------------")
print(response.text)

# Definir la consulta GraphQL con parametros
query_lista = """
    {
        plantaPorEspecie(especie: "Malus domestica"){
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print("----------------------------buscar por especie-----------------------------------")
print(response.text)

# Definir la consulta GraphQL con parametros
query_lista = """
    {
        plantaPorFruta(frutos: "True"){
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print("-----------------------------------buscar por fruta-----------------------------------")
print(response.text)

# Definir la consulta GraphQL para crear nuevo planta
query_actualizar = """
mutation {
        actualizarPlanta(id: 1 ,nombre: "margarita", especie: "Bellis perennis", edad: 24 ,altura: 10, frutos:"False") {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_actualizar})
print("-----------------------------actualizar---------------------------------------------")
print(response_mutation.text)

# Definir la consulta GraphQL para eliminar una planta
query_eliminar = """
mutation {
        deletePlanta(id: 3) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print("-------------------------eliminar-------------------------------------------------")
print(response_mutation.text)


# Definir la consulta GraphQL simple
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""

response = requests.post(url, json={'query': query_lista})
print("--------------------------------listar-------------------------------------")
print(response.text)
