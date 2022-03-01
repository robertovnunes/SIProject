# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 3
        self.maxforce = 0.2

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
    def seek(self, target):
        desired = target - self.position
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        self.applyForce(steer)
        self.arrive(target)
    
    

        
    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
            #popMatrix()
            
    def arrive(self, target):
        desired = PVector.sub(target,self.position)
        d = desired.mag()
        desired.normalize()
        if(d < 100):
            m = map(d,0,100,0,self.maxspeed)
            desired.mult(m)
        else:
            desired.mult(self.maxspeed)
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        self.applyForce(steer)
