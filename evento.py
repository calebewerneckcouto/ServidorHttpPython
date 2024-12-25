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
        
    @classmethod
    def cria_evento_online(cls,nome):
        evento = cls(nome,local=f"https://tamarcado.com/eventos?id={cls.id}") 
        return evento   
    
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
        
ev = Evento("Aula de Python")
ev2 = Evento("Aula de Javascript","Rio de Janeiro")

ev_online = Evento.cria_evento_online("Live de Python")
ev2_online = Evento.cria_evento_online("Live de Javascript")
ev_online.imprime_informacoes()   
ev2_online.imprime_informacoes()
# print(Evento.calcula_limite_pessoas_area(5))  
