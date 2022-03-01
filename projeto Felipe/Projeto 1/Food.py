# The "Food" class

class Food():

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.posicao = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.flag = 0
        self.comida = 0

    # Method to update location
    def update(self, x, y):
        # Update velocity
        #self.velocity.add(self.acceleration)
        # Limit speed
        #self.velocity.limit(self.maxspeed)
        self.posicao = PVector(x, y)
        # Reset accelerationelertion to 0 each cycle
        #self.acceleration.mult(0)

    def flagComeco(self, comando):
        if (comando == 1):
            self.flag = 1
            return self.flag
        else:
            return self.flag

    def location (self):
        return self.posicao
    
    def comeu (self):
        self.comida += 1

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        #theta = self.velocity.heading()# + PI / 2
        fill(100)
        stroke(200)
        strokeWeight(1)
        with pushMatrix():
            translate(self.posicao.x, self.posicao.y)
            #rotate(theta)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
