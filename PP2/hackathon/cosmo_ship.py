import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Game')

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

HEALTH_FONT=pygame.font.SysFont('comicsans',20)
BULLETS_FONT=pygame.font.SysFont('comicsans',20)
WINNER_FONT=pygame.font.SysFont('comicsans',100)

FPS=60
VEL=20
BULLET_VEL=25
MAX_BULLETS=3000

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
#BULLET_FIRE_SOUND1=pygame.mixer.Sound(os.path.join('Assets','TFU2.mp3'))
#BULLET_FIRE_SOUND2=pygame.mixer.Sound(os.path.join('Assets','chort0.mp3'))


SHIP_WIDTH=50
SHIP_HEIGHT=45

YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2

#ROTATIONS AND IMAGES
Yellow_Spaceship_pic=pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png' ))#'BAIS2.png'))
Yellow_Spaceship=pygame.transform.rotate(pygame.transform.scale(
    Yellow_Spaceship_pic,(SHIP_WIDTH,SHIP_HEIGHT)),90) #0)

Red_Spaceship_pic=pygame.image.load(os.path.join('Assets', 'spaceship_red.png')) #'DAUREN.png'))
Red_Spaceship=pygame.transform.rotate(pygame.transform.scale(
    Red_Spaceship_pic,(SHIP_WIDTH,SHIP_HEIGHT)), 270) #0)

SPACE_PIC=pygame.image.load(os.path.join('Assets','space.png'))

def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()/2,HEIGHT//2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE_PIC,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    
    red_health_txt=HEALTH_FONT.render('HEALTH: '+ str(red_health),1,WHITE)
    yellow_health_txt=HEALTH_FONT.render('HEALTH: '+ str(yellow_health),1,WHITE)
    
    red_bullets_display=BULLETS_FONT.render('BULLETS: '+str(len(red_bullets)),1,WHITE)
    yellow_bullets_display=BULLETS_FONT.render('BULLETS: '+str(len(yellow_bullets)),1,WHITE)

    
    WIN.blit(red_health_txt,(WIDTH-red_health_txt.get_width()-10,10))
    WIN.blit(yellow_health_txt,(10,10))
    
    WIN.blit(red_bullets_display,(WIDTH-red_bullets_display.get_width()-12,30))
    WIN.blit(yellow_bullets_display,(10,30))

    
    WIN.blit(Yellow_Spaceship,(yellow.x,yellow.y))
    WIN.blit(Red_Spaceship,(red.x,red.y))
    
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()

def movement(keys_pressed,yellow,red):
    #YELLOW
    if keys_pressed[pygame.K_a] and yellow.x-VEL>=0: #LEFT
            yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL<=430: #RIGHT
            yellow.x+=VEL
    #if keys_pressed[pygame.K_q]: #RIGHT-BOOST
            #yellow.x+=VEL+15
    if keys_pressed[pygame.K_w] and yellow.y-VEL>=0: #UP
            yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL<=450: #DOWN
            yellow.y+=VEL
    #RED
    if keys_pressed[pygame.K_KP4] and red.x-VEL>=430: #LEFT
            red.x-=VEL
    #if keys_pressed[pygame.K_KP7]: #LEFT-BOOST
            #red.x-=VEL+15
    if keys_pressed[pygame.K_KP6] and red.x+VEL<=850: #RIGHT
            red.x+=VEL
    if keys_pressed[pygame.K_KP8] and red.y-VEL>=0: #UP
            red.y-=VEL
    if keys_pressed[pygame.K_KP5] and red.y+VEL<=450: #DOWN
            red.y+=VEL
            
def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
    

def main():
    red=pygame.Rect(700,300,SHIP_WIDTH,SHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SHIP_WIDTH,SHIP_HEIGHT)
    
    red_bullets=[]
    yellow_bullets=[]
    
    red_health=10
    yellow_health=10

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_e and len(yellow_bullets)<MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
                if event.key == pygame.K_KP9 and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
            if event.type==RED_HIT:
                red_health-=1
                BULLET_HIT_SOUND.play()
                99
            if event.type==YELLOW_HIT:
                yellow_health-=1
                BULLET_HIT_SOUND.play()
            
            winner_txt=""
            if red_health<=0:
                winner_txt="YELLOW WINS"
                
                        
            if yellow_health<=0:
                winner_txt="RED WINS"
                
            
            if winner_txt!="":
                draw_winner(winner_txt)
                red_health=10
                yellow_health=10
                break
                
        keys_pressed=pygame.key.get_pressed()
        
        handle_bullets(red_bullets,yellow_bullets,red,yellow)
        
        movement(keys_pressed,yellow,red)
        
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        
        
        
    main()
    
if __name__=="__main__":
    main()
    
