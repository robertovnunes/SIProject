# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position


from Vehicle import Vehicle
from Food import Food 

count = 0

def setup():
    global v
    global f
    global x
    global count
    size(640, 360)
    velocity = PVector(0, 0)
    v = Vehicle(width / 2, height / 2)
    x = random(1, 10)
    f = Food(width/x, height/3, velocity)
    

def draw():
    background(255)
    #mouse = PVector(mouseX, mouseY)
    message = "Comida: " + str(count)
    textSize(20);
    text(message, 5, 30); 
    fill(0, 408, 612);

    f.display()
    v.arrive(f.position)
    v.run()
    
    diff_x = f.position.x - v.position.x
    diff_y = f.position.y - v.position.y
    if diff_x < 0.5 and diff_y < 0.5:
       x = random(1, 10)
       y = random(1,10)
       f.update_pos(x,y)
       f.display()
       sum_count()

def sum_count():
    global count
    count = count + 1
    
    
