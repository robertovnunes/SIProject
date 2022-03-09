from queue import Queue





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
