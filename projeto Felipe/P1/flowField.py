class flowField:
    
    def __init__(self, width, height):
        self.resolution = PVector(width, height)
        cols = width/self.resolution.x
        rows = width/self.resolution.y
        self.cols = int(floor(cols))
        self.rows = int(floor(rows))
        self.field = [[0]*self.cols for _ in range(self.rows)]

        xoff = 0.0
        
        for x in range(self.cols):
            yoff = 0.0
            
            for y in range(self.rows):
                n = noise((x) * xoff, (y) * yoff)
                self.field[x][y] = n 
                yoff = yoff + 0.1
                
            xoff = xoff + 0.1
            
    def Lookup(self, lookup):
        column = int(constrain(lookup.x/self.resolution.x,0,self.cols-1))
        row = int(constrain(lookup.y/self.resolution.y,0,self.rows-1))
        return self.field[column][row]
    
    def display(self):
        fill(20)
        xoff = 0.0
        for x in range(self.cols):
            yoff = 0.0
            for y in range(self.rows):
                n = noise((x) * xoff,
                        (y) * yoff)
                fill(240 * n, 255, 255) 
                square(x, y, 10)     
                yoff = yoff + 0.1
                
            xoff = xoff + 0.1
