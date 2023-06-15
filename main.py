import hashlib


def update_hash(*args):
    # Cria uma variável para o código ficar mais limpo.
    h = hashlib.sha256()

    # Criar uma string vazia.
    hash_txt = ''

    # Cria um loop para concatenar todos os argumentos
    # passados pela função em um String (hash_text).
    # Este loop for in passa por todos os elementos dentro do array
    for a in args:
        hash_txt += str(a)

    # O update() é para adicionar uma variável no hash antes de
    # criptografar, é necessário no mínimo um update para funcionar
    # a criptografia.
    # O encode() é necessário para transformar o hash_txt em binário,
    # E assim conseguir criptografar ele.
    h.update(hash_txt.encode())

    # O hexdigest() pega todas as variáveis lançadas no update(),
    # e criptografa todas elas em um hash contendo só hexadecimais.
    return h.hexdigest()


# Isso roda o script de python.
if __name__ == '__main__':
    update_hash('batataassada', 1454)
