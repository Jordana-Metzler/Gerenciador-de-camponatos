import json
from Classes.Campeonato import Campeonato
from Classes.Time import Time
from utils.string import normalizar_nome


def salvar_campeonato(campeonato) -> None:
    dados = {
        "nome": campeonato.nome,
        "times": [time.para_dict() for time in campeonato.times]
    }
    arquivo_nome: str = normalizar_nome(campeonato.nome) + ".json"
    with open(arquivo_nome, "w") as arquivo:
        json.dump(dados, arquivo)
        
def carregar_campeonato(nome : str) -> Campeonato:
    arquivo_nome: str = normalizar_nome(nome) + ".json"
    with open(arquivo_nome, "r") as arquivo:
        dados = json.load(arquivo)
    campeonato = Campeonato(dados["nome"])
    for dado_time in dados["times"]:
        time = Time.de_dict(dado_time)
        campeonato.times.append(time)
    return campeonato