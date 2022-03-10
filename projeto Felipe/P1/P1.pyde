import random

from Vehicle import Vehicle
from Food import Food
from Mapa import Terreno
from flowField import flowField
from BFS import BFS
from Dijkstra import *

tileSize = 20;
scl = 3;

def setup():
    global v
    global f
    global mapa
    global flow
    global path
    size(720, 480)
    noStroke()
    colorMode(HSB)
    
    r1 = random.randint(0, width/tileSize)
    r2 = random.randint(0, height/tileSize)
    r3 = random.randint(0, width/tileSize)
    r4 = random.randint(0, height/tileSize)
    mapa = Terreno()
    flow = flowField(tileSize)
    v = Vehicle(r1, r2)
    f = Food(r3*tileSize-10, r4*tileSize-10)
    
def draw():
    #background(200)
    mapa.drawTerrain()
    
    if(round(v.location()[0]) == round(f.location()[0]) and round(v.location()[1]) == round(f.location()[1])):
        r1 = random.randint(0, width/tileSize)
        r2 = random.randint(0, height/tileSize)
        f.update(r1*tileSize-10, r2*tileSize-10)
        f.comeu()

    v.arrive(f.location())

    f.display()        
    v.update()
    v.display()
    
    textSize(28)
    text("Pontuacao: ", 15, 40)
    text(str(f.comida), 170, 40)
    
