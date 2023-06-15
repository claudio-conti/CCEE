import hashlib


def update_hash(*args):
    # Cria uma variável para o código ficar mais limpo.
    h = hashlib.sha256()

    # Criar uma string vazia.
    hash_txt = ''

    # Cria um loop para concatenar todos os argumentos
    # passados pela função.
    for arg in args:
        hash_txt += str(arg)

    h.update(hash_txt.encode())
    print(h.hexdigest())
    return h.hexdigest()


# Isso roda o script de python.
if __name__ == '__main__':
    update_hash('batataassada')
