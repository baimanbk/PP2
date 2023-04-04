import pygame, sys
from collections import namedtuple


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
points = []

class Brush():
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.mode = 'draw'
        self.icon = 'brush'
        self.image = pygame.transform.scale(pygame.image.load('./assets/brush.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.pos
        self.width = 15
        self.color_mode = 'red'
        self.colors = {
                'white': (255, 255, 255), 
                'black': (0, 0, 0),
                'red': (255, 0, 0),
                'green': (0, 255, 0),
                'blue': (0, 0, 255)
                }
        self.points = []

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.image = pygame.transform.scale(pygame.image.load(f'./assets/{self.icon}.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos

    def add_points(self):
        Point = namedtuple('Point', ['x', 'y', 'radius', 'color', 'mode'])
        if self.mode == 'draw': 
            p = Point(self.pos[0], self.pos[1], self.width, self.color_mode, 'circle')
            self.points = self.points + [p]

        if self.mode == 'eraser':
            p = Point(self.pos[0], self.pos[1], self.width, 'white', 'circle')
            self.points = self.points + [p]

    def draw_line_between(self, surf, index, start, end):
        
        color = self.colors[self.color_mode]
        
        dx = start.x - end.x
        dy = start.y - end.y
        iterations = max(abs(dx), abs(dy))
        
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            if start.mode == 'circle':
                pygame.draw.circle(surf, start.color, (x, y), start.radius)

    def draw_points(self, surf):
        i = 0
        while i < len(self.points) - 1:
            self.draw_line_between(surf, i, self.points[i], self.points[i + 1])
            i += 1


            


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint")
    fps = pygame.time.Clock()

    brush = Brush()

    pygame.mouse.set_visible(False)


    while True:
        pressed_keys = pygame.key.get_pressed()
        alt_key = pressed_keys[pygame.K_LALT] and pressed_keys[pygame.K_RALT]
        ctrl_key = pressed_keys[pygame.K_LCTRL] and pressed_keys[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_key:
                    return
                if event.key == pygame.K_F4 and alt_key:
                    return 
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    brush.color_mode = 'red'
                if event.key == pygame.K_b:
                    brush.color_mode = 'blue'
                if event.key == pygame.K_g:
                    brush.color_mode = 'green'
                if event.key == pygame.K_q:
                    brush.color_mode = 'black'
                if event.key == pygame.K_e:
                    brush.color_mode = 'white'
                    brush.mode = 'eraser'
                    brush.icon = 'eraser'
                if event.key == pygame.K_d:
                    brush.mode = 'draw'
                if event.key == pygame.K_n:
                    brush.mode = 'None'
                if event.key == pygame.K_l:
                    brush.width += 5
                if event.key == pygame.K_s:
                    brush.width -= 5

            if event.type == pygame.MOUSEBUTTONDOWN:
                brush.add_points()

            if event.type == pygame.MOUSEMOTION:    
                brush.update()
                brush.add_points()


        

        screen.fill((255, 255, 255))
        brush.draw_points(screen)
        screen.blit(brush.image, brush.rect)
        pygame.display.flip()
        fps.tick(60)



if __name__ == "__main__":
    main()