# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    global comida
    global foodPosition
    global FoodX
    global FoodY
    string = "Comida:"
    comida = 0
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    FoodX = random(600)
    FoodY = random(300)
    foodPosition = PVector(FoodX, FoodY)
    food = Food(foodPosition)

def draw():
    loop()
    background(255)
    global comida
    global foodPosition
    global food
    vehicle.update()
    vehicle.display()
    food.display()
    textSize(26)
    text("Frutas: {}".format(comida), 50, 50)
    if floor(PVector.sub(food.position, vehicle.position).mag()) > 0:
        vehicle.seek(food.position)
    else:
        comida = comida + 1
        FoodX = random(600)
        FoodY = random(300)
        foodPosition = PVector(FoodX, FoodY)
        food = Food(foodPosition)
        food.display()
        
