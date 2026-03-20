from Classes.Partida import Partida
from Classes.Time import Time

class Campeonato:
    def __init__(self, nome: str)-> None:
        self.nome: str = nome
        self.times: list[Time] = []
        self.chaves: dict = {}
        self.partidas: list[Partida] = []
    
    def cadastrar_time(self, nome_time: str)-> None:
        novo_time: Time = Time(nome_time)
        self.times.append(novo_time)
    
    def buscar_time(self, nome: str)-> Time | None:
        for time in self.times:
            if time.nome == nome:
                return time
        return None
    
    def classificacao(self)-> list[Time]:
        return sorted(self.times, key=lambda time: (time.vitorias, time.pontos, time.sets_vencidos, time.calcular_pontos_avarege()), reverse=True)
    
    def para_dict(self) -> dict:
        return {
        "nome": self.nome,
        "times": [time.para_dict() for time in self.times],
        "partidas": [partida.para_dict() for partida in self.partidas],
        "chaves": self.chaves
    }
        
    @classmethod
    def de_dict(cls, dados: dict) -> "Campeonato":
        campeonato = cls(dados["nome"])
        for dado_time in dados["times"]:
            time = Time.de_dict(dado_time)
            campeonato.times.append(time)
        for dado_partida in dados["partidas"]:
            partida = Partida.de_dict(dado_partida, campeonato)
            campeonato.partidas.append(partida)
        campeonato.chaves = dados["chaves"]
        return campeonato