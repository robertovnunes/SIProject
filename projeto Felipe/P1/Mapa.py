tileSize = 20;
scl = 0.1;

class Celula():
    def __init__(self, x, y, c, Tvizinhos):
        self.x = x
        self.y = y
        self.custo = c
        self.vizinhos = Tvizinhos
    def getValues(self):
        return (self.x, self.y, self.custo, self.vizinhos)
        
        
class Terreno():
    
    def __init__(self):
        self.mapa = []
        for i in range (width/tileSize):
            self.mapa.append([])
            for j in range (height/tileSize):
                self.mapa[i].append([])    


    def Vizinhos(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if neighbor in self.mapa:
                result.append(neighbor)
        return result
    
    def drawTerrain(self):
        for i in range(width/tileSize):
            for j in range(height/tileSize):
                x = int(i*tileSize)/2
                y = int(j*tileSize)/2
                sp = self.getColor(i, j)
                fill(sp[0])
                rect(i * tileSize, j * tileSize, tileSize, tileSize)
                vzns = self.Vizinhos(self.mapa[i][j])
                print(vzns)
                if sp[1] < 0.4:
                    #verde: grama com custo 0
                    GCell = Celula(x, y, 0, vzns)
                    #print(GCell.getValues()[1])
                    self.mapa[i][j].append(GCell.getValues())
                elif sp[1] < 0.5:
                    #Azul: Agua com custo 2
                    Bcell = Celula(x, y, 2, vzns)
                    #print(Bcell.getValues())
                    self.mapa[i][j].append(Bcell.getValues())
                elif sp[1] < 0.6:
                    #laranja: areia com custo 1
                    #OCell = Celula(x, y, 1, vzns)
                    print(OCell.getValues())
                    self.mapa[i][j].append(OCell.getValues())
                else:
                    #preto
                    BLcell = Celula(x, y, 3, vzns)
                    print(BLcell.getValues())
                    self.mapa[i][j].append(BLcell.getValues())
                #print(self.mapa[i][j])
    
    
    def getColor (self, x, y):
        v = noise(x * scl, y * scl)
        if v < 0.4:
            #verde
            return (color(66, 255, 255), v)
        elif v < 0.5:
            #azul
            return (color(155, 255, 255), v)
        elif v < 0.6:
            #laranja
            return (color(30, 255, 255), v)
        else:
            #preto
            return (color(0, 0, 0), v)
    
