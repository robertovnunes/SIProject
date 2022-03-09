from queue import Queue


def Vizinhos(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        result.append([node[0] + dir[0], node[1] + dir[1]])
    return result


def __main__(self, Xo, mapa):
    fronteira = Queue()
    fronteira.put(Xo)
    visitado = dict()
    visitado[Xo] = None

    while not fronteira.empty():
        atual = fronteira.get()
        for next in mapa.vizinhos(atual):
            if next not in visitado:
                fronteira.put(next)
                visitado.add(next)
