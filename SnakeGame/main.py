import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

segment_width = 16
segment_height = 16
segment_margin = 4

randx = random.randint(1, 40)
randy = random.randint(1, 30)
randx1 = random.randint(1, 40)
randy1 = random.randint(1, 30)


x_change = segment_width + segment_margin
y_change = 0
size = 3

class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen_rect = screen.get_rect()
        screen.blit(self.image, self.rect)

        if self.rect.left < screen_rect.left:
            temp_rect = self.rect.copy()
            temp_rect.x += screen_rect.width
            screen.blit(self.image, temp_rect)
        elif self.rect.right > screen_rect.right:
            temp_rect = self.rect.copy()
            temp_rect.x -= screen_rect.width
            screen.blit(self.image, temp_rect)

        if self.rect.top < screen_rect.top:
            temp_rect = self.rect.copy()
            temp_rect.y += screen_rect.height
            screen.blit(self.image, temp_rect)
        elif self.rect.bottom > screen_rect.bottom:
            temp_rect = self.rect.copy()
            temp_rect.y -= screen_rect.height
            screen.blit(self.image, temp_rect)


class SnakeSegment(Segment):
    def __init__(self, x, y):
        super().__init__(x, y, GREEN)


class AppleSegment(Segment):
    def __init__(self, x, y):
        super().__init__(x, y, RED)


pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()


pygame.display.set_caption('Snake')

allspriteslist = pygame.sprite.Group()

snake_segments = []
for i in range(size):
    x = 400 - (segment_width + segment_margin) * 1
    y = 200
    segment = SnakeSegment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)

apple_segments = []
for i in range(1):
    x = 200 - (segment_width + segment_margin) * 1
    y = 100
    segment = AppleSegment(x, y)
    apple_segments.append(segment)
    allspriteslist.add(segment)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = (segment_width + segment_margin) * -1
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = (segment_width + segment_margin)
            y_change = 0
        if event.key == pygame.K_UP:
            x_change = 0
            y_change = (segment_height + segment_margin) * -1
        if event.key == pygame.K_DOWN:
            x_change = 0
            y_change = (segment_height + segment_margin)

    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)

    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change

    if x < screen_rect.left:
        x += screen_rect.width
    elif x + segment_width + segment_margin > screen_rect.right:
        x -= screen_rect.width

    if y < screen_rect.top:
        y += screen_rect.height
    elif y + segment_height + segment_margin > screen_rect.bottom:
        y -= screen_rect.height


    segment = SnakeSegment(x, y)

    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    def AppleIntersection1() :
        if (snake_segments[0].rect.x == apple_segments[0].rect.x) & (snake_segments[0].rect.y == apple_segments[0].rect.y):
            x = snake_segments[1].rect.x
            y = snake_segments[1].rect.y
            segment = SnakeSegment(x, y)
            snake_segments.append(segment)
            apple_segments[0].rect.y = randy * 20
            apple_segments[0].rect.x = randx * 20


    def AppleIntersection2() :
        if (snake_segments[0].rect.x == apple_segments[0].rect.x) & (snake_segments[0].rect.y == apple_segments[0].rect.y):
            x = snake_segments[1].rect.x
            y = snake_segments[1].rect.y
            segment = SnakeSegment(x, y)
            snake_segments.append(segment)
            apple_segments[0].rect.y = randy1 * 20
            apple_segments[0].rect.x = randx1 * 20



    AppleIntersection1()
    AppleIntersection2()


    for i in range(1, len(snake_segments) - 1):
        if ((snake_segments[0].rect.x == snake_segments[i].rect.x) & (snake_segments[0].rect.y == snake_segments[i].rect.y)):
            pygame.quit()
            quit()



    screen.fill(BLACK)

    allspriteslist.draw(screen)

    for x in allspriteslist:
        x.draw(screen)

    pygame.display.flip()

    clock.tick(7)

pygame.quit()