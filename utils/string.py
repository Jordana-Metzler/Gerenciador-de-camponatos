import unicodedata


def normalizar_nome(nome: str) -> str:
    # remove acentos
    sem_acento = unicodedata.normalize("NFKD", nome)
    sem_acento = sem_acento.encode("ASCII", "ignore").decode("ASCII")
    # substitui espaços por _ e coloca em minúsculo
    return sem_acento.lower().replace(" ", "_")