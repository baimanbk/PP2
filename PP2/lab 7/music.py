import pygame as pg
import os

pg.init()

class SOUND:
    def __init__(self, path_to_sound, path_to_photo):
        self.sound = pg.mixer.Sound('music\\' + path_to_sound)
        self.photo = pg.image.load('assets\\sound_images\\' + path_to_photo)
        self.is_playing = True
    
    def placePhoto(self,screen):
        self.photo = pg.transform.scale(self.photo, (430, 410))
        screen.blit(self.photo, (31, 121))

path_to_sound = os.listdir('music\\')
path_to_photo = os.listdir('assets\\sound_images\\')
path_to_sound.sort()
path_to_photo.sort()

#path_to_photo.pop(path_to_photo.index('.DS_Store'))
#path_to_sound.pop(path_to_sound.index('.DS_Store'))
sounds = []

for i in zip(path_to_photo, path_to_sound):
    print(i)
    print(i[0])
    sound = SOUND(path_to_photo = i[0], path_to_sound = i[1])
    sounds.append(sound)

screen = pg.display.set_mode((490, 835))

BACKGROUD = pg.image.load('assets\\bg.png').convert()
screen.blit(BACKGROUD, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            if 685.64 <= pg.mouse.get_pos()[1] <= 755.81 and 215.3 <= pg.mouse.get_pos()[0] <= 289.54:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 98 <= pg.mouse.get_pos()[0] <= 156 and 695 <= pg.mouse.get_pos()[1] <= 756:
                pg.mixer.stop()
                sound_index -= 1
                sounds[sound_index+1].is_playing = True
                if(sound_index == -1):
                    sound_index = len(sounds) - 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 355 <= pg.mouse.get_pos()[0] <= 413 and 696 <= pg.mouse.get_pos()[1] <= 757:
                pg.mixer.stop()
                sound_index += 1
                sounds[sound_index - 1].is_playing = True
                if(sound_index == len(sounds)):
                    sound_index = -1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)

        
    pg.display.flip()