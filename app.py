from evento import Evento
from evento_online import EventoOnline
from flask import Flask, jsonify,make_response,abort,request,json

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


@app.errorhandler(400)
def nao_encontrado(erro):
    data={"erro":str(erro)}
    return (jsonify(data),400)


def get_evento_or_404(id):
    for ev in eventos:
        if ev.id == id:
            return ev
    


@app.route("/api/eventos/<int:id>/")
def buscar_id(id):
    """
    Busca um evento específico pelo seu ID.
    
    :param event_id: ID do evento a ser buscado.
    :type event_id: int
    :return: JSON com os detalhes do evento se encontrado, ou uma mensagem de erro.
    """
    ev = get_evento_or_404(id)
    if ev:
        return jsonify(ev.to_dict())
    data={"erro":f"Não encontrei o evento com id: {id}"}
    abort(404,"Evento não encontrado")
    
    
@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
    """
    Deletar um evento específico pelo seu ID.
    
    :param id: ID do evento a ser buscado.
    :type id: int
    :return: JSON com os detalhes do evento se encontrado, ou uma mensagem de erro.
    """
    ev = get_evento_or_404(id)
    if ev:
        eventos.remove(ev)
        return jsonify(id=id)
    
    abort(404, "Evento não encontrado")

       
    
    
@app.route("/api/eventos/", methods=["POST"])  
def criar_eventos():  
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")
    
    #Validação
    if not nome:
         abort(400," 'Nome'  deve ser informado")
        
    
    if local:
        evento = Evento(nome=nome,local=local)
    else:
        evento = EventoOnline(nome=nome)
    
    
    eventos.append(evento)
    return {
        "id": evento.id,
        "url":f"/api/eventos/{evento.id}/"
    }
    
    
    
@app.route("/api/eventos/<int:id>", methods=["PUT"])
def atualizar_eventos(id):
    data = request.get_json()
    nome = data.get("nome")
    local = data.get("local")

    # Validação
    if not nome:
        abort(400, "'Nome' deve ser informado")
    if not local:
        abort(400, "'Local' deve ser informado")

    # Recupera o evento ou retorna 404
    ev = get_evento_or_404(id)
    if ev is None:
        abort(404, f"Evento com id {id} não encontrado.")

    # Atualiza os atributos do objeto
    ev.nome = nome
    ev.local = local

    return jsonify(ev.to_dict())



@app.route("/api/eventos/<int:id>", methods=["PATCH"])
def atualizar_eventos_parcialmente(id):
    ev = get_evento_or_404(id)
    data = request.get_json()
    #quero editar o nome
    if "nome" in data.keys():
        nome = data.get("nome")
        if not nome:
            abort(400, "'Nome' deve ser informado")
        ev.nome = nome    
    #quero editar o local
    if "local" in data.keys():
        local = data.get("local")
        if not local:
            abort(400, "'Local' deve ser informado")        
        ev.local=local 
    
    return jsonify(ev.to_dict())

if __name__ == "__main__":
    app.run(debug=True)