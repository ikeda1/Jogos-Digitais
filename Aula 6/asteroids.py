import math
import pygame as pg
import random


speed = 5
x = 0

w, h = (600, 400)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 0, 0)
RED = (255, 0, 0)



class Asteroid:
    def __init__(self, x, y, radius, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
    
    def move(self):

        if self.direction == 'N':
            self.y-=speed
        elif self.direction == 'NE':
            self.y-=speed
            self.x+=speed
        elif self.direction == 'E':
            self.x += speed
        elif self.direction == 'SE':
            self.x += speed
            self.y += speed
        elif self.direction == 'S':
            self.y += speed
        elif self.direction == 'SW':
            self.y += speed
            self.x -= speed
        elif self.direction == 'W':
            self.x -= speed
        elif self.direction == 'NW':
            self.x -= speed
            self.y -= speed

    def checkWallCollision(self):
        # upper
        if self.y - self.radius <= 0:
            if self.direction == 'N':
                self.direction = 'S'
            elif self.direction == 'NE':
                self.direction = 'SE'
            elif self.direction == 'NW':
                self.direction = 'SW'
        
        # bottom
        elif self.y + self.radius >= h:
            if self.direction == 'S':
                self.direction = 'N'

            elif self.direction == 'SE':
                self.direction = 'NE'

            elif self.direction == 'SW':
                self.direction = 'NW'

        # right
        elif self.x + self.radius >= w:
            if self.direction == 'E':
                self.direction = 'W'

            elif self.direction == 'SE':
                self.direction = 'SW'

            elif self.direction == 'NE':
                self.direction = 'NW'
        
        # left
        elif self.x - self.radius <= 0:
            if self.direction == 'W':
                self.direction = 'E'

            elif self.direction == 'SW':
                self.direction = 'SE'

            elif self.direction == 'NW':
                self.direction = 'NE'


    
def collide(ast1, ast2):
    # Euclidian distance between two asteroids
    distance = math.sqrt(((ast1.x-ast2.x)**2)+((ast1.y-ast2.y)**2))
    print(distance)

    if (ast1.radius + ast2.radius) >= distance:
        return True
    else:
        return False


colors = [BLACK, BLUE, GREEN]
sizes = [25, 50, 75]
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

nAsteroids = 10
asteroids = []
for n in range(nAsteroids):
    randN = random.randrange(0,3)
    randX = random.randrange(75, w-75)
    randY = random.randrange(75, h-75)
    randDirection = random.randrange(0, 8)
    asteroids.append(Asteroid(randX, randY, sizes[randN], directions[randDirection]))


asteroids.append(Asteroid(90, 100, 50, 'N'))
asteroids.append(Asteroid(300, 300, 50, 'NE'))

print(collide(asteroids[0], asteroids[1]))


pg.init()

screen = pg.display.set_mode((w,h))

clock = pg.time.Clock()


pg.draw.circle(screen, RED, (asteroids[0].x, asteroids[0].y), asteroids[0].radius, 1)
pg.draw.circle(screen, BLUE, (asteroids[1].x, asteroids[1].y), asteroids[1].radius, 1)


game_loop = True
while game_loop:
    screen.fill((255, 255, 255))

    fps = clock.tick(60)

    
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            game_loop = False
            pg.quit()    
            quit()
    
    for asteroid in asteroids:
        asteroid.move()
        pg.draw.circle(screen, RED, (asteroid.x, asteroid.y), asteroid.radius, 1)
        asteroid.checkWallCollision()
        
    
    pg.display.flip()

