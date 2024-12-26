from evento import Evento
from evento_online import EventoOnline
from flask import Flask, jsonify,make_response,abort

app = Flask(__name__)

# Inicializa os eventos
ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de Javascript")
ev = Evento("Aula de Python", "Rio de Janeiro")

# Lista de eventos
eventos = [ev_online, ev2_online, ev]

@app.route("/")
def index():
    """Endpoint raiz para verificar se a aplicação está funcionando."""
    return "<h1>Flask configurado com Sucesso!</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    """
    Retorna uma lista de todos os eventos.
    
    :return: JSON contendo uma lista de dicionários representando os eventos.
    """
    return jsonify([ev.to_dict() for ev in eventos])


@app.errorhandler(404)
def nao_encontrado(erro):
    data={"erro":str(erro)}
    return (jsonify(data),404)


@app.route("/api/eventos/<int:id>")
def buscar_id(id):
    """
    Busca um evento específico pelo seu ID.
    
    :param event_id: ID do evento a ser buscado.
    :type event_id: int
    :return: JSON com os detalhes do evento se encontrado, ou uma mensagem de erro.
    """
    event = next((ev for ev in eventos if ev.id == id), None)
    if event:
        return jsonify(event.to_dict())
    data={"erro":f"Não encontrei o evento com id: {id}"}
    abort(404,"Evento não encontrado")

if __name__ == "__main__":
    app.run(debug=True)
