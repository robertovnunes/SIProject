tileSize = 20;
scl = 0.1;

class Celula():
        def __init__(self, x, y, w, h, c):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.custo = c

class Terreno(Celula):
    
    def __init__(self):
        self.mapa = []
        for i in range (width/tileSize):
            self.mapa.append([])
            for j in range (height/tileSize):
                self.mapa[i].append([])
                    
                

        
                    

    
    def drawTerrain(self):
        for i in range (width/tileSize):
            
            for j in range (height/tileSize):
                #vizinhos = self.Vizinhos(self.mapa[i][j])
                sp = self.getColor(i, j)
                fill(sp[0])
                rect(i * tileSize, j * tileSize, tileSize, tileSize)
                if sp[1] < 0.3:
                    #verde: grama com custo 0
                    self.mapa[i][j].append(Celula(i*tileSize/2,j*tileSize/2,tileSize,tileSize, 0))
                elif sp[1] < 0.5:
                    #laranja: areia com custo 1
                    self.mapa[i][j].append(Celula(i*tileSize/2,j*tileSize/2,tileSize,tileSize, 1))
                elif sp[1] < 0.7:
                    #azul: agua com custo 2
                    self.mapa[i].append(Celula(i*tileSize/2,j*tileSize/2,tileSize,tileSize, 2))
                else:
                    #preto
                    self.mapa[i].append(Celula(i*tileSize/2,j*tileSize/2,tileSize,tileSize, 3))

    
    
    def getColor (self, x, y):
        v = noise(x * scl, y * scl)
        if v < 0.3:
            #azul
            return (color(155, 255, 255), v)
        elif v < 0.5:
            #verde
            return (color(66, 255, 255), v)
        elif v < 0.7:
            #laranja
            return (color(30, 255, 255), v)
        else:
            #preto
            return (color(0, 0, 0), v)
    
