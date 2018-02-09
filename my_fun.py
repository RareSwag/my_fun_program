# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Fun Stuff"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
 
# Timer
clock = pygame.time.Clock()
refresh_rate = 30

#Image
SUN = pygame.image.load('coop.jpg')
ROCKET = pygame.image.load('rocket.png')
FIREWORKS = pygame.image.load('fire.png')

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
ORANGE = (255, 69, 0)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

rockets = []
def make_rocket():
    rocketx = random.randrange(-10, 800)
    rockety = 500
    rockets.append([rocketx, rockety])

''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])

daytime = True
lights_on = False
sunm = [False, False, False, False]
sunx = 575
suny = 75
vel = [0,0]
speed = 5
acceleration = 20

# Sound Effects
pygame.mixer.music.load("jazz.ogg")
explosion = pygame.mixer.Sound("explosion.ogg")
wow = pygame.mixer.Sound("wow.ogg")
rocketsound = pygame.mixer.Sound("rocket.ogg")

# Game loop
pygame.mixer.music.play(-1)
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_LEFT:
                vel[0] = -1 * speed
                wow.play()
            elif event.key == pygame.K_RIGHT:
                vel[0] = speed
                wow.play()
            elif event.key == pygame.K_UP:
                vel[1] = -1 * speed
                wow.play()
            elif event.key == pygame.K_DOWN:
                vel[1] = speed
                wow.play()
            elif event.key == pygame.K_r:
                make_rocket()
                rocketsound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vel[0] = 0
                wow.play()
            elif event.key == pygame.K_RIGHT:
                vel[0] = 0
                wow.play()
            elif event.key == pygame.K_UP:
                vel[1] = 0
                wow.play()
            elif event.key == pygame.K_DOWN:
                vel[1] = 0
                wow.play()
            # google 'pygame key constants' for more keys
                
    # Game logic
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)

    ''' move rocket '''
    for r in rockets:
        r[1] -= speed * acceleration

        if r[1] < -100 :
            rockets.remove(r)
            explosion.play()
            
            
            

    ''' set sky color '''
    if daytime:
        sky = BLUE
    else:
        sky = BLACK
        
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    sunx += vel[0]
    suny += vel[1]
    
    screen.blit(SUN, (sunx, suny))

    ''' rocket '''
    for r in rockets:
        screen.blit(ROCKET, (r[0], r[1]))
        
    
    
    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
