
import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# POST agrega un nuevo estudiante por la ruta /pacientes
print("-----------------------------agregar------------------------------")
ruta_post = url + "pacientes"
nuevo_paciente = {
    "ci": 788843218,
    "nombre": "Juanito",
    "apellido": "Pérez",
    "edad": 24,
    "genero": "no binario",
    "diagnostico":"cancer",
    "doctor": "Zofia",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)  
print(post_response.text)


# GET obtener a todos los estudiantes por la ruta /pacientes
print("-----------------------------mostrar------------------------------")
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#GET obtener por ci
print("-----------------------------mostrar_por_ci------------------------------")
ruta_get = url + "pacientes/"+"9943299"
get_response_ci = requests.request(method="GET", url=ruta_get)
print(get_response_ci.text)

# GET filtrando por nombre con query params
print("-----------------------------buscar_parametros------------------------------")
ruta_get = url + "pacientes/?diagnostico=cancer"
get_response_diagnostic = requests.request(method="GET", url=ruta_get)
print(get_response_diagnostic.text)
# GET filtrando por nombre con query params
print("-----------------------------buscar_parametros------------------------------")
ruta_get = url + "pacientes_doc/?doctor=edriel"
get_response_diagnostic = requests.request(method="GET", url=ruta_get)
print(get_response_diagnostic.text)

#PUT coambiar ()
print("--------------------------actualizar------------------------")
ruta_put = url + "pacientes/"+"788843218"
paciente = {
    "ci": 788843218,
    "nombre": "Juanito",
    "apellido": "Pérez",
    "edad": 50,
    "genero": "femenino",
    "diagnostico":"cancer",
    "doctor": "edriel",
}
get_put=requests.request(method="PUT", url=ruta_put , json=paciente)
print(get_put.text)

#DELETE
print("-----------------------------eliminar------------------------------")
ruta_del = url + "pacientes"
del_elem = requests.request(method="DELETE", url=ruta_del)
print(get_response_diagnostic.text)