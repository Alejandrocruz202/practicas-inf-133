from zeep import Client

client = Client('http://localhost:8000')
suma = client.service.Sumar(a=10,b=5)
resta = client.service.Restar(a=10,b=5)
multiplicacion  = client.service.Multiplicar(a=10,b=5)
division= client.service.Dividir(a=10,b=5)
print(suma)
print(resta)
print(multiplicacion)
print(division)