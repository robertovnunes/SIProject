tileSize = 20;
scl = 3;

class Celula():
    def __init__(self, x, y, c, tempVizinhos):
        self.x = x
        self.y = y
        self.custo = c
        self.vizinhos = tempVizinhos

    def getValues(self):
        return (self.x, self.y, self.custo, self.vizinhos)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getC(self):
        return self.custo
    def getVizinhos(self):
        return self.vizinhos
    def __str__(self):
        print(self.x, self.y, self.custo, self.vizinho)
        
class Terreno():
    
    def __init__(self):
        self.mapa = []
        self.walls =[]
        for i in range (width/tileSize):
            self.mapa.append([])
            for j in range (height/tileSize):
                self.mapa[i].append([])    
                
    def getCoord(x, y):
        print(x, y)
        return [x*20+10, y*20+10]


    def Vizinhos(self, tupla):
        (x, y) = tupla
        result = []
        
        neighbor = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] # E W N S
        if (x + y) % 2 == 0: neighbor.reverse()
        for i in neighbor:
            if i[0] < 0 or i[1] < 0 or i[0] > width/tileSize or i[1] > height/tileSize:
                neighbor.pop(neighbor.index(i))
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
                if sp[1] < 0.4:
                    #verde: grama com custo 0
                    vzns = self.Vizinhos((i, j))
                    GCell = Celula(x, y, 0, vzns)
                    self.mapa[i][j].append(GCell.getValues())
                elif sp[1] < 0.5:
                    #Azul: Agua com custo 2
                    vzns = self.Vizinhos((i, j))
                    Bcell = Celula(x, y, 2, vzns)
                    self.mapa[i][j].append(Bcell.getValues())
                elif sp[1] < 0.6:
                    #laranja: areia com custo 1
                    vzns = self.Vizinhos((i, j))
                    OCell = Celula(x, y, 1, vzns)
                    self.mapa[i][j].append(OCell.getValues())
                else:
                    #preto
                    vzns = self.Vizinhos((i, j))
                    BLcell = Celula(x, y, 3, vzns)
                    self.mapa[i][j].append(BLcell.getValues())
                    self.walls.append((BLcell.getX(), BLcell.getY()))
    
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
    
