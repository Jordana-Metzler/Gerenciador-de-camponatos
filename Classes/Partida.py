from Classes.Time import Time


class Partida:
    def __init__(self, vencedor: Time, perdedor: Time, sets_vencedor: int, sets_perdedor: int, parciais_vencedor: list[int], parciais_perdedor: list[int]) -> None:
        self.vencedor: Time = vencedor
        self.perdedor: Time = perdedor
        self.sets_vencedor: int = sets_vencedor
        self.sets_perdedor: int = sets_perdedor
        self.parciais_vencedor: list[int] = parciais_vencedor
        self.parciais_perdedor: list[int] = parciais_perdedor
    
    def calcula_sets(self)-> None:
        total_sets : int = self.sets_vencedor + self.sets_perdedor
        if total_sets == 5:
            pontos_vencedor : int = 2
            pontos_perdedor : int = 1
        else:
            pontos_vencedor : int = 3
            pontos_perdedor : int = 0
    
        self.vencedor.atualizar_stats( 1, pontos_vencedor, self.sets_vencedor, self.sets_perdedor, sum(self.parciais_vencedor), sum(self.parciais_perdedor))
        self.perdedor.atualizar_stats( 0, pontos_perdedor, self.sets_perdedor, self.sets_vencedor, sum(self.parciais_perdedor), sum(self.parciais_vencedor))
    
    def para_dict(self) -> dict:
        return {
            "vencedor": self.vencedor.nome,
            "perdedor": self.perdedor.nome,
            "sets_vencedor": self.sets_vencedor,
            "sets_perdedor": self.sets_perdedor,
            "parciais_vencedor": self.parciais_vencedor,
            "parciais_perdedor": self.parciais_perdedor
        }
        
    @classmethod 
    def de_dict(cls, dados: dict, campeonato) -> "Partida":
        vencedor = campeonato.buscar_time(dados["vencedor"])
        perdedor = campeonato.buscar_time(dados["perdedor"])
        return cls(vencedor, perdedor, dados["sets_vencedor"], dados["sets_perdedor"], dados["parciais_vencedor"], dados["parciais_perdedor"])