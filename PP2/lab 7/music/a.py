import pygame as pg 
import os

pg.init()
screen = pg.display.set_mode((490, 835))
BACKGROUD = pg.image.load('lab 7\\bg.png').convert()
BACKGROUD = pg.transform.scale(BACKGROUD, (490, 835))
screen.blit(BACKGROUD, (0, 0))
is_playing = True

sound_files = os.listdir('music\\')
sound_images = os.listdir('sound_images\\')
sound_files.sort()
sound_images.sort()
sound_queue = []
for filename in sound_files:
    sound = pg.mixer.Sound('music\\' + filename)
    sound_queue.append(sound)
music_index = 0
sound_queue[music_index].play()

def changeSoundsImage():
    SOUND_IMAGE = pg.image.load('sound_images\\' + sound_images[music_index]).convert()
    SOUND_IMAGE = pg.transform.scale(SOUND_IMAGE, (430, 410))
    screen.blit(SOUND_IMAGE, (250, 120))

changeSoundsImage()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif pg.mouse.get_pressed()[0]:
            if -165.96 <=  pg.mouse.get_pos()[0] <= 104.64 and 
