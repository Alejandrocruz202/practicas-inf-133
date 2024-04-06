from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation


class Planta(ObjectType):
    id = Int()
    nombre = String()
    especie = String()
    edad = Int()
    altura=Int()
    frutos=String()

class Query(ObjectType):
    plantas= List(Planta)
    aux=List(Planta)
    planta_por_id = Field(Planta, id=Int())
    planta_por_especie = Field(aux, especie=String())
    planta_por_fruta = Field(aux,frutos=String())
    def resolve_plantas(root, info):
        return plantas
    
    def resolve_planta_por_id(root, info, id):
        for planta in plantas:
            if planta.id == id:
                return planta
        return None
    
    def resolve_planta_por_especie(root, info, especie):
        aux=[]
        for planta in plantas:
            if planta.especie== especie:
                aux.append(planta)
        print(aux)
        return aux
    
    def resolve_planta_por_fruta(root, info, frutos):
        aux=[]
        for planta in plantas:
            if planta.frutos == frutos:
                aux.append(planta)
        print(aux)
        return aux

class CrearPlanta(Mutation):
    class Arguments:
        nombre = String()
        especie = String()
        edad = Int()
        altura=Int()
        frutos=String()

    planta = Field(Planta)

    def mutate(root, info, nombre, especie, edad, altura, frutos):
        nuevo_planta = Planta(
            id=len(plantas) + 1, 
            nombre = nombre,
            especie = especie,
            edad = edad,
            altura=altura,
            frutos=frutos
        )
        plantas.append(nuevo_planta)
        return CrearPlanta(planta=nuevo_planta)

class DeletePlanta(Mutation):
    class Arguments:
        id = Int()

    planta = Field(Planta)

    def mutate(root, info, id):
        for i, planta in enumerate(plantas):
            if planta.id == id:
                plantas.pop(i)
                return DeletePlanta(planta=planta)
        return None

class ActualizarPlanta(Mutation):
    class Arguments:
        id=Int()
        nombre = String()
        especie = String()
        edad = Int()
        altura=Int()
        frutos=String()

    planta = Field(Planta)

    def mutate(root, info, id, nombre, especie, edad, altura, frutos):
        for i, planta in enumerate(plantas):
            if planta.id == id:
                plantas.pop(i)
                nuevo_planta = Planta( 
                    id=id,
                    nombre = nombre,
                    especie = especie,
                    edad = edad,
                    altura=altura,
                    frutos=frutos
                )
                plantas.insert(i,nuevo_planta)
                return ActualizarPlanta(planta=nuevo_planta)
        return None

class Mutations(ObjectType):
    crear_planta = CrearPlanta.Field()
    delete_planta = DeletePlanta.Field()
    actualizar_planta=ActualizarPlanta.Field()
    
plantas = [
    Planta(
        id=1,
        nombre="rosa",
        especie="Rosa grandiflora",
        edad=15,
        altura=50,
        frutos="False"
    ),
    Planta(
        id=2,
        nombre="manzanilla",
        especie="Chamaemelum nobile",
        edad=9,
        altura=10,
        frutos="False"
    ),
    Planta(
        id=3,
        nombre="frutilla",
        especie="Fragaria × ananassa",
        edad=15,
        altura=16,
        frutos="True"
    )
]


schema = Schema(query=Query, mutation=Mutations)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print("----------------------------------------------------")
        print(f"Iniciando servidor web en http://localhost:{port}/")
        print("""⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢷⡄⠈⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠂⢹
⠈⡷⡄⠈⠲⢤⣈⠻⠉⠛⠉⠉⠁⠒⠖⠉⠉⠉⠒⠶⢦⣤⠴⠒⢉⣡⠴⠀⢀⠏
⠀⢸⡿⡂⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡞⠉⠀⢀⣠⡞⠀
⠀⠀⢙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢠⡼⡟⠀⠀
⠀⠀⡼⠋⠀⣤⣀⠀⠀⠀⠀⠀⠈⠐⣂⣄⠀⠀⠀⠀⠀⠀⠀⢀⠀⣰⡟⠁⠀⠀
⠀⢠⡇⠀⠀⠘⠛⠃⠀⠀⠀⠀⠾⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
⠀⢸⡇⢺⡀⠀⢠⡒⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠸⡇⠀⠀⠀
⠀⢸⡇⣘⠑⡀⠀⠙⢏⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⣔⣇⠀⠀⠀
⠀⢸⡇⡁⠀⢳⣶⣾⣷⣦⣄⣀⡀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
⠀⠸⡇⠁⠀⠀⢏⠉⠀⠀⠙⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠀⠀⠀
⠀⠀⠯⣀⣈⣀⣈⣐⣲⣄⣄⣤⣴⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⡧⠀⠀""")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡿⠟⠛⠻⢿⣧⠀⠀⠀⣰⣿⠟⠉⠉⠉⠛⢷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⠈⣿⡇⠀⣼⡟⠁⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢹⣷⣠⣿⠁⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣿⡄⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣤⣼⣿⣧⠀⠀⠀⢀⣀⣬⢧⣀⡀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠙⢷⣄⣴⠋⠁⠀⠀⠀⠙⢷⡄⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣧⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣧⡀⠀⠹⣦⣀⠀⠀⢀⣀⡤⠾⠤⠤⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣷⡦⣄⣀⡽⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡛⠢⠤⠄⠓⠦⠤⣀⣀⣠⡤⠴⠚⢁⣼⠇⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⢋⣠⣾⣿⠛⣀⠀⠀⠀
⠀⠀⢀⣰⣿⢿⣿⡇⣠⣄⢀⡈⠙⠛⠷⠶⠶⠶⠶⣿⡟⠛⣿⣄⢻⣟⠛⢿⣿⣿⠃⣠⣤
⢀⣴⣿⠟⢿⣿⠛⠀⣿⣧⣾⠿⣿⣿⢿⡶⠀⠀⣿⣿⢿⣧⠙⠻⣿⣿⡄⠀⠙⢿⣿⡿⠋
⠈⠛⠿⣷⡿⠟⠀⢀⣿⡟⠁⢠⣿⣷⣶⠀⣤⣤⢸⣿⡿⢿⣶⡄⠀⢻⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⣼⣿⣅⣠⡄⠀⠀⠀⣿⣷⣼⣿⠇⠀⠀⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠃⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()