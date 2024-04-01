import pygame
size = width, height = (1200, 700)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()

class Tank():
    def __init__(self, x, y, w, h, speed, image, orient):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.image = image
        self.orient = orient
    
    def draw(self):
        screen.blit(self.image[self.orient], (self.x, self.y))

class Missile():
    def __init__(self, x, y, speed, orient, visible):
        self.x = x
        self.y = y
        self.speed = speed
        self.orient = orient
        self.visible = visible

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, 'red', (self.x, self.y), 5, 0)

tank_red = Tank(100, 100, 94, 64, 5, [pygame.image.load(f"tank_red_{i}.png") for i in range(0,4)], 0)
missile_red = Missile(0, 0, 5, 0, False)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        keyboard = pygame.key.get_pressed()
        buttons_mouse = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()        
        
        #Управление красным танком
        if keyboard[pygame.K_a]:
            tank_red.x -= tank_red.speed
            tank_red.orient = 3
            missile_red.orient = 3
        if keyboard[pygame.K_d]:
            tank_red.x += tank_red.speed
            tank_red.orient = 1
            missile_red.orient = 1
        if keyboard[pygame.K_w]:
            tank_red.y -= tank_red.speed
            tank_red.orient = 0
            missile_red.orient = 0
        if keyboard[pygame.K_s]:
            tank_red.y += tank_red.speed
            tank_red.orient = 2
            missile_red.orient = 2
        if keyboard[pygame.K_f]:
            missile_red.x = tank_red.x+tank_red.w
            missile_red.y = tank_red.y+tank_red.h//2
            missile_red.visible = True           
    
    screen.fill('White')        
    tank_red.draw()            
    missile_red.draw() 
    if missile_red.visible:
        if missile_red.orient == 0:
            missile_red.y -= missile_red.speed  
        if missile_red.orient == 1:
            missile_red.x += missile_red.speed          
        if missile_red.orient == 2:
            missile_red.y += missile_red.speed  
        if missile_red.orient == 3:
            missile_red.x -= missile_red.speed        
   
    pygame.display.flip()
    fps.tick(60)
pygame.quit()