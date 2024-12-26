
from evento import Evento
from evento_online import EventoOnline
ev = Evento("Aula de Python")
ev2 = Evento("Aula de Javascript","Rio de Janeiro")

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de Javascript")
#ev_online.imprime_informacoes()   
#ev2_online.imprime_informacoes()
# print(Evento.calcula_limite_pessoas_area(5))  
ev =Evento ("Aula de Python","Rio de Janeiro")
ev.imprime_informacoes()
print(ev_online.to_json())
print(ev2_online.to_json())