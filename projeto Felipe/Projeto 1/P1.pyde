import random

from Vehicle import Vehicle
from Food import Food

def setup():
    global v
    global f
    size(720, 480)
    v = Vehicle(width / 2, height / 2)
    f = Food(width / 2, height / 2)
    
def draw():
    background(200)
    
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width)
        r2 = random.randint(0, height)
        loc = PVector(r1,r2)
        f.update(r1, r2)
        f.comeu()

    v.arrive(PVector(f.location()[0],f.location()[1]))
    print(PVector(f.location()[0],f.location()[1]))
    print(PVector(v.location()[0],v.location()[1]))

    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida - 1), 170, 40)
