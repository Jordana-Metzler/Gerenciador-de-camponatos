from Classes.Campeonato import Campeonato
from menu import cadastrar_time, exibir_chaves, registrar_partida, exibir_classificacao
from service.persistencia import carregar_campeonato, salvar_campeonato
from service.sorteio import sortear_times

nome = input("Nome do campeonato: ")
try:
    meu_campeonato = carregar_campeonato(nome)
    print("Campeonato carregado!")
except FileNotFoundError:
    meu_campeonato = Campeonato(nome)
    print("Novo campeonato criado!")


while True:
    print("\n=== GESTOR DE CAMPEONATO ===")
    print("1. Cadastrar time")
    print("2. Registrar partida")
    print("3. Ver classificação")
    print("4. Sortear chaves")
    print("5. Exibir chaves")
    print("6. Times cadastrados")
    print("0. Sair")
        
    opcao = input("Escolha: ")
        
    match opcao:
        case "1":
            cadastrar_time(meu_campeonato)
            salvar_campeonato(meu_campeonato)
            pass
        case "2":
            registrar_partida(meu_campeonato)
            salvar_campeonato(meu_campeonato)
            pass
        case "3":
            exibir_classificacao(meu_campeonato)
            pass
        case "4":
            sortear_times(meu_campeonato)
            salvar_campeonato(meu_campeonato)
            pass
        case "5":
            exibir_chaves(meu_campeonato)
        case "6":
            print("Times cadastrados:")
            for time in meu_campeonato.times:
                print(f"- {time.nome}")
        case "0":
            break
        case _:
            print("Opção inválida. Tente novamente.")
                