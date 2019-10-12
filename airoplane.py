import pygame, sys, time, random, math
from pygame.locals import *

# Устнановка pygame
pygame.init()

# Настройка окна
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Анимация')

# Создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'


MOVESPEED1 = 2
MOVESPEED2 = 2

# Настройка цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
c1 = 0
c2 = 0
# Создание структуры данных блока
b1 = {'rect': pygame.Rect(20, 20, 20, 20), 'color': RED, 'dir': None}
b2 = {'rect': pygame.Rect(500, 500, 20, 20), 'color': GREEN, 'dir': None}
boxes = [b1,b2]

# Запуск игрового цикла
while True:
    # Проверка наличия события QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Выбор случайного направления самолета 1
    if c1 == 30:
        vec = random.randint(0, 4)
        if vec == 0:
            b1['dir'] = DOWNLEFT
        if vec == 1:
            b1['dir'] = DOWNRIGHT
        if vec == 2:
            b1['dir'] = UPLEFT
        if vec == 3:
            b1['dir'] = UPRIGHT
        c1 = 0

    # Выбор случайного направления самолета 2

    if c2 == 20:
        vec = random.randint(0, 4)
        if vec == 0:
            b2['dir'] = DOWNLEFT
        if vec == 1:
            b2['dir'] = DOWNRIGHT
        if vec == 2:
            b2['dir'] = UPLEFT
        if vec == 3:
            b2['dir'] = UPRIGHT
        c2 = 0

    # Создание на поверхности белого фона.
    windowSurface.fill(WHITE)

    for b in boxes:

        # Ловирование самолета
        x1 = random.randint(-1, 1)
        x2 = random.randint(-1, 1)
        # x_vec = random.randint(1, 2)
        # y_vec = random.randint(1, 2)
        # x1cos = math.cos(random.random())
        # x2cos = math.cos(random.random())

        # Перемещение структуры данных блока.
        if b['dir'] == DOWNLEFT:
            b['rect'].centerx -= MOVESPEED1
            b['rect'].centery += MOVESPEED2
        if b['dir'] == DOWNRIGHT:
            b['rect'].centerx += MOVESPEED1
            b['rect'].centery += MOVESPEED2
        if b['dir'] == UPLEFT:
            b['rect'].centerx -= MOVESPEED1
            b['rect'].centery -= MOVESPEED2
        if b['dir'] == UPRIGHT:
            b['rect'].centerx += MOVESPEED1
            b['rect'].centery -= MOVESPEED2


        # Проверка, переместился ли блок за пределы окна.
        if b['rect'].top < 0:
            # Прохождение блока через верхнюю границу.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # Прохождени блока через нижнюю границу.
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # Прохождени блока через левую границу.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # Прохождени блока через правую границу.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # Создание блока на поверхности
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

        c1 += 1
        c2 += 1

    # Вывод окна на экран.
    pygame.display.update()
    time.sleep(0.05)








