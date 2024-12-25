class Evento:
    
    id = 1
    def __init__(self,nome,local=""):
        self.nome = nome
        self.local = local
        self.id =Evento.id
        Evento.id +=1
        
    def imprime_informacoes(self):
        print(f"ID do evento",{self.id})
        print(f"Nome do evento:",{self.nome})    
        print(f"Local do evento:",{self.local})
        print("------------------------------")
        
    
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5<= area <10:
            return 5
        elif 10<= area <20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
        
        
class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome,local)
    
    def imprime_informacoes(self):
        print(f"ID do evento",{self.id})
        print(f"Nome do evento:",{self.nome})    
        print(f"Link para acessar o evento:",{self.local})
        print("------------------------------")        
    
         
ev = Evento("Aula de Python")
ev2 = Evento("Aula de Javascript","Rio de Janeiro")

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de Javascript")
ev_online.imprime_informacoes()   
ev2_online.imprime_informacoes()
# print(Evento.calcula_limite_pessoas_area(5))  
ev =Evento ("Aula de Python","Rio de Janeiro")
ev.imprime_informacoes()