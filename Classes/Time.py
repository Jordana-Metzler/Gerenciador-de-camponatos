import time


class Time:
    def __init__( self, nome: str)-> None:
        self.nome: str = nome
        self.vitorias: int = 0
        self.pontos: int = 0
        self.sets_vencidos: int = 0
        self.sets_perdidos: int = 0
        self.pontos_feitos: int = 0
        self.pontos_sofridos: int = 0

    def calcular_pontos_avarege(self)-> float:
        try:
            media_pontos: float = self.pontos_feitos / self.pontos_sofridos
            return media_pontos
        except ZeroDivisionError:
            return 0

    def __str__(self)-> str:
        return f"Time: {self.nome}"
     
    def atualizar_stats(self, vitorias: int, pontos: int, sets_vencidos: int, sets_perdidos: int, parciais_feitos: int, parciais_sofridos: int)-> None:
        self.vitorias += vitorias
        self.pontos += pontos
        self.sets_vencidos += sets_vencidos
        self.sets_perdidos += sets_perdidos
        self.pontos_feitos += parciais_feitos
        self.pontos_sofridos += parciais_sofridos
        
    def para_dict(self)-> dict:
        return {
        "nome": self.nome,
        "vitorias": self.vitorias,
        "pontos": self.pontos,
        "sets_vencidos": self.sets_vencidos,
        "sets_perdidos": self.sets_perdidos,
        "pontos_feitos": self.pontos_feitos,
        "pontos_sofridos": self.pontos_sofridos
        }
        
    @classmethod
    def de_dict(cls, dados: dict) -> "Time":
        time = cls(dados["nome"])
        time.vitorias = dados["vitorias"]
        time.pontos = dados["pontos"]
        time.sets_vencidos = dados["sets_vencidos"]
        time.sets_perdidos = dados["sets_perdidos"]
        time.pontos_feitos = dados["pontos_feitos"]
        time.pontos_sofridos = dados["pontos_sofridos"]
        return time