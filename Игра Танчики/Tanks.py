import pygame
size = width, height = (1200, 700)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()

class Tank():
    def __init__(self, x, y, w, h, speed, image, orient, visible):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.image = image
        self.orient = orient
        self.visible = visible
        
    def draw(self):
        if self.visible:
            screen.blit(self.image[self.orient], (self.x, self.y))

class Missile():
    def __init__(self, x, y, speed, orient, visible, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.orient = orient
        self.visible = visible
        self.color = color

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 5, 0)


tank_red = Tank(100, 100, 94, 64, 5, [pygame.image.load(f"tank_red_{i}.png") for i in range(0,4)], 0, True)
tank_blue = Tank(100, 500, 94, 64, 5, [pygame.image.load(f"tank_blue_{i}.png") for i in range(0,4)], 0, True)
missile_red = Missile(0, 5, 0, 0, False, 'red')
missile_blue = Missile(0, 5, 0, 0, False, 'blue')

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
        if keyboard[pygame.K_d]:
            tank_red.x += tank_red.speed
            tank_red.orient = 1
        if keyboard[pygame.K_w]:
            tank_red.y -= tank_red.speed
            tank_red.orient = 0
        if keyboard[pygame.K_s]:
            tank_red.y += tank_red.speed
            tank_red.orient = 2
        if keyboard[pygame.K_f]:
            missile_red.visible = True
            missile_red.speed = 2
            if tank_red.orient == 0:
                missile_red.x = tank_red.x+tank_red.w
                missile_red.y = tank_red.y+tank_red.h//2
                missile_red.orient = 0  
            if tank_red.orient == 1:
                missile_red.x = tank_red.x+tank_red.w
                missile_red.y = tank_red.y+tank_red.h//2
                missile_red.orient = 1  
            if tank_red.orient == 2:
                missile_red.x = tank_red.x+tank_red.w
                missile_red.y = tank_red.y+tank_red.h//2
                missile_red.orient = 2  
            if tank_red.orient == 3:
                missile_red.x = tank_red.x+tank_red.w
                missile_red.y = tank_red.y+tank_red.h//2
                missile_red.orient = 3
        
       
        if keyboard[pygame.K_h]:
            tank_blue.x -= tank_blue.speed
            tank_blue.orient = 3
            missile_red.orient = 3
        if keyboard[pygame.K_k]:
            tank_blue.x += tank_blue.speed
            tank_blue.orient = 1
            missile_red.orient = 1
        if keyboard[pygame.K_u]:
            tank_blue.y -= tank_blue.speed
            tank_blue.orient = 0
            missile_red.orient = 0
        if keyboard[pygame.K_j]:
            tank_blue.y += tank_blue.speed
            tank_blue.orient = 2
            missile_red.orient = 2
        if keyboard[pygame.K_l]:
            missile_blue.visible = True 
            missile_blue.speed = 2 
            if tank_blue.orient == 0:
                missile_blue.x = tank_blue.x+tank_blue.w//2
                missile_blue.y = tank_blue.y
                missile_blue.orient = 0
            if tank_blue.orient == 1:
                missile_blue.x = tank_blue.x+tank_blue.w
                missile_blue.y = tank_blue.y+tank_blue.h//2
                missile_blue.orient = 1
            if tank_blue.orient == 2:
                missile_blue.x = tank_blue.x+tank_blue.w//3
                missile_blue.y = tank_blue.y+tank_blue.h+5
                missile_blue.orient = 2
            if tank_blue.orient == 3:
                missile_blue.x = tank_blue.x
                missile_blue.y = tank_blue.y+tank_blue.h//2
                missile_blue.orient = 3
    
    screen.fill('White')        
    tank_red.draw()     
    tank_blue.draw()
    missile_red.draw()
    missile_blue.draw() 
    if missile_red.visible:
        if missile_red.orient == 0:
            missile_red.y -= missile_red.speed  
        if missile_red.orient == 1:
            missile_red.x += missile_red.speed          
        if missile_red.orient == 2:
            missile_red.y += missile_red.speed  
        if missile_red.orient == 3:
            missile_red.x -= missile_red.speed 
        
    if missile_blue.visible:
        if missile_blue.orient == 0:
            missile_blue.y -= missile_blue.speed  
        if missile_blue.orient == 1:
            missile_blue.x += missile_blue.speed          
        if missile_blue.orient == 2:
            missile_blue.y += missile_blue.speed  
        if missile_blue.orient == 3:
            missile_blue.x -= missile_blue.speed     

    if missile_red.x>tank_blue.x and missile_red.x<tank_blue.x+tank_blue.w and missile_red.y>tank_blue.y and missile_red.y<tank_blue.y+tank_blue.h:
        tank_blue.visible = False
        
    if missile_blue.x>tank_red.x and missile_blue.x<tank_red.x+tank_red.w and missile_blue.y>tank_red.y and missile_blue.y<tank_red.y+tank_red.h:
        tank_red.visible = False    
   
    pygame.display.flip()
    fps.tick(60)
pygame.quit()