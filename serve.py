from http.server import HTTPServer, BaseHTTPRequestHandler
from evento_online import EventoOnline
from evento import Evento

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de Javascript")
ev = Evento("Aula de Python", "Rio de Janeiro")
eventos = [ev_online, ev2_online, ev]

# Classe de manipulação de requisições
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html;charset=utf-8")
            self.end_headers()
            
            data = f"""
            <html>
                <head>
                    <title> Olá Mundo! </title>
                </head>
                <body>
                    <p>Testando nosso servidor HTTP!</p>
                    <p>Diretório: {self.path}</p>
                </body>
            </html>
            """.encode()
            
            self.wfile.write(data)
       
        elif self.path == "/eventos":
            self.send_response(200)
            self.send_header("Content-type", "text/html;charset=utf-8")
            self.end_headers()
           
            # Definindo o estilo CSS
            stylesheet = """
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
            """
           
            # Construindo o HTML dos eventos
            eventos_html = ""
            for ev in eventos:
                eventos_html += f"""
                <tr>
                    <td>{ev.id}</td>
                    <td>{ev.nome}</td>
                    <td>{ev.local}</td>
                </tr>
                """
            
            # HTML final com estilo e tabela
            data = f"""
            <html>
                <head>
                    <title>Eventos</title>
                    {stylesheet}
                </head>
                <body>
                    <h1>Lista de Eventos</h1>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Local</th>
                        </tr>
                        {eventos_html}
                    </table>
                </body>
            </html>
            """.encode()
            self.wfile.write(data)

# Configuração do servidor
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()
