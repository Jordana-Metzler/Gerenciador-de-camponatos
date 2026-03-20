from Classes.Partida import Partida
from Classes.Time import Time

def cadastrar_time(campeonato) -> None:
    """"Cadastra novos times no campeonato, em looping."""
    while True:
        nome_input: str = input("Digite o nome do time (ou 'PARAR' para sair): ").upper()
        if nome_input == "PARAR":
            break
        if campeonato.buscar_time(nome_input) is not None:
            print(f"Time '{nome_input}' já cadastrado, insira outro time.")
        else:
            campeonato.cadastrar_time(nome_input)
            print(f"Time '{nome_input}' cadastrado com sucesso!")


def selecionar_time(campeonato)-> tuple[Time, Time]:
    """Seleciona o vencedor e perdedor da partida, garantindo que sejam times diferentes e existam no campeonato."""
    
    while True:
            nome_vencedor : str = input("Nome do vencedor: ").upper()
            nome_perdedor : str = input("Nome do perdedor: ").upper()
            vencedor : Time | None = campeonato.buscar_time(nome_vencedor)
            perdedor : Time | None = campeonato.buscar_time(nome_perdedor)
            if nome_vencedor == nome_perdedor:
                print("Erro: vencedor e perdedor não podem ser o mesmo time!")
            elif vencedor is None or perdedor is None:
                print("Erro: time não encontrado! Verifique os nomes e tente novamente.")
            else:
                 break
    return vencedor, perdedor

def coletar_sets()-> int:
    """Coleta o número de sets perdidos pelo time perdedor, garantindo que seja um valor válido."""
    while True:
        try:
            sets_perdedor: int = int(input("Sets do perdedor (0, 1 ou 2): "))
            if sets_perdedor > 2 or sets_perdedor < 0:
                print("Erro: sets perdidos devem ser 0, 1 ou 2!")
            else:
                break
        except ValueError:
            print("Digite um número válido!")
    return sets_perdedor
   

def coletar_parciais(sets_vencedor: int, sets_perdedor: int)-> tuple[list[int], list[int]]:
    """Coleta os pontos de cada set para o vencedor e perdedor, garantindo que sejam números válidos."""
    parciais_vencedor : list[int] = []
    parciais_perdedor : list[int] = []
    for i in range(sets_vencedor + sets_perdedor):
        print(f"\nSet {i+1}:")
        while True:
            try:
                pontos_vencedor: int = int(input("Pontos do vencedor: "))
                pontos_perdedor: int = int(input("Pontos do perdedor: "))
                if pontos_vencedor < 0 or pontos_perdedor < 0:
                    print("Erro: pontos não podem ser negativos!")
                else:
                    break
            except ValueError:
                print("Digite um número válido!")
        parciais_vencedor.append(pontos_vencedor)
        parciais_perdedor.append(pontos_perdedor)
    return parciais_vencedor, parciais_perdedor

def registrar_partida(campeonato)-> None:
    """Registra uma nova partida no campeonato."""
    print("Times cadastrados:")
    for time in campeonato.times:
        print(f"- {time.nome}")
    vencedor, perdedor = selecionar_time(campeonato)
    sets_vencedor: int = 3
    sets_perdedor: int = coletar_sets()
    parciais_vencedor, parciais_perdedor= coletar_parciais(sets_vencedor, sets_perdedor)
    partida: Partida = Partida(vencedor, perdedor, sets_vencedor, sets_perdedor, parciais_vencedor, parciais_perdedor)
    partida.calcula_sets()
    campeonato.partidas.append(partida)

def exibir_classificacao(campeonato)-> None:
    """Exibe a classificação atual do campeonato, ordenada por pontos, vitórias e média de pontos."""
    for time in campeonato.classificacao():
        print(f"Equipe: {time.nome} - Vitórias: {time.vitorias}, Pontos: {time.pontos}, Sets Vencidos: {time.sets_vencidos}, Média de Pontos: {time.calcular_pontos_avarege():.4f}")
        
def exibir_chaves(campeonato) -> None:
    if not campeonato.chaves:
        print("Nenhuma chave sorteada ainda!")
        return
    for letra, times in campeonato.chaves.items():
        print(f"\nChave {letra}:")
        for time in times:
            print(f"  - {time}")





    
         