from random import random
import string


def sortear_times(campeonato) -> None:
    """Exibe os times cadastrados em ordem aleatória."""
    
    n_chaves: int = int(input("Quantas chaves? "))
    times_por_chave: int = len(campeonato.times) // n_chaves
    random.shuffle(campeonato.times)
    print([time.nome for time in campeonato.times])
    grupos = []
    
    for i in range(n_chaves):
        inicio : int = i * times_por_chave
        if i == n_chaves - 1: 
            grupos.append(campeonato.times[inicio:])
        else:
            grupos.append(campeonato.times[inicio:inicio + times_por_chave])
    
    for index, grupo in enumerate(grupos):
        print(f"Chave {string.ascii_uppercase[index]}: ")
        for time in grupo:
            print(f"  - {time.nome}")
    