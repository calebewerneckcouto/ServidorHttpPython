from http.server import HTTPServer, BaseHTTPRequestHandler




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
       
      elif  self.path == "/eventos":
           self.send_response(200)
           self.send_header("Content-type", "text/html;charset=utf-8")
           self.end_headers()
           data = f"""
        <html>
               <p>oi</p>
        </html>           
        
        """.encode()
           self.wfile.write(data)
          
          
server = HTTPServer(('localhost',8000),SimpleHandler)
server.serve_forever()
