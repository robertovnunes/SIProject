# The "Food" class

class Food():

    def __init__(self, posicao):
        self.position = posicao

        

    def display(self):
        fill(127)
        stroke(200)
        strokeWeight(2)
        square(self.position.x, self.position.y, 10)
