class flowField:
    
    def __init__(self, r):
        self.resolution = r
        cols = width/self.resolution
        rows = width/self.resolution
        self.cols = int(floor(cols))
        self.rows = int(floor(rows))
        self.field = [[PVector(0,0)]*self.cols for _ in range(self.rows)]

        xoff = 0.0
        
        for x in range(0, self.cols):
            yoff = 0.0
            
            for y in range(0, self.rows):
                n = map(noise(xoff,yoff), 0, 1, 0, TWO_PI)
                self.field[x][y] = PVector(cos(n), sin(n)) 
                print(self.field[x][y])
                yoff = yoff + 0.1
                
            xoff = xoff + 0.1
            
    def Lookup(self, lookup):
        column = int(constrain(lookup.x/self.resolution,0,self.cols-1))
        row = int(constrain(lookup.y/self.resolution,0,self.rows-1))
        return self.field[column][row].get()
