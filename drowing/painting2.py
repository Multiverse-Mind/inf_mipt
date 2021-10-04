# Вызов необходимых библиотек
import pygame
from random import *


def needles(x, y, scale=1):
    '''
    Функция рисует иголку случайного цвета (в определённом диапазоне).
    x, y - координаты самой левой вершины треугольника иголки.
    scale - коэффициент масштабирования иголки (по умолчанию равен 1).
    '''
    # Рисование иголки
    color_value = randint(0, 50)
    pygame.draw.polygon(screen, (color_value, color_value, color_value), 
                        [(x, y), (x + randint(0, 4) * scale, y - randint(2, 8) 
                                  * scale), (x + 2 * scale, y + randint(2, 5))])


def hedgehog(x, y, width_body, height_body, scale_and_needles):
    '''
    Функция рисует ёжика с грибом и яблоком на иголках.
    x, y - координаты левого верхнего угла прямоугольника, в который 
    вписан эллипс тела ёжика.
    width_body, height_body - ширина и высота тела ёжика (на основе 
    которых будет задан масштаб всех частей ёжика).
    scale_and_needles - коэффициент, отвечающий за количество иголок 
    и размеры иголок, яблока, гриба, глаз, носа и ног.
    '''
    # Рисование тела и головы
    pygame.draw.ellipse(screen, (64, 65, 62), (x, y, width_body, height_body))
    pygame.draw.ellipse(screen, (64, 65, 62), (x + 5 * width_body // 6, 
                                               y + 2 * height_body // 7, 
                                               width_body // 2, 
                                               height_body // 2))
    # Рисование первого набора иголок (первый слой)
    for i in range(7 * scale_and_needles):
        x_needle = randint(x, x + 5 * width_body // 6)
        y_needle = randint(y, y + (2 * height_body // 3))
        needles(x_needle, y_needle, scale_and_needles)
    # Рисование яблока
    pygame.draw.circle(screen, 
                       (randint(110, 250), randint(10, 100), randint(10, 100)), 
                       (x + width_body // 3, y - 15), 2 * scale_and_needles)
    # Рисование гриба
    pygame.draw.ellipse(screen, (186, 143, 143), (x + 2 * width_body // 3, 
                                                  y - 20, 3 * scale_and_needles,
                                                  7 * scale_and_needles))
    pygame.draw.ellipse(screen, (255, 43, 43), (x + 2 * width_body // 3 - 2 * 
                                                scale_and_needles, y - 20, 
                                                7 * scale_and_needles, 3 * 
                                                scale_and_needles))
    # Рисование второго набора иголок (второй слой)
    for i in range(7 * scale_and_needles):
        x_needle = randint(x, x + (2 * width_body // 3))
        y_needle = randint(y, y + (height_body // 2))
        needles(x_needle, y_needle, scale_and_needles)
    # Рисование глаз
    pygame.draw.circle(screen, (255, 255, 255), 
                       (x + (7 * width_body // 6) + 6, 
                        y + (height_body // 2) - 2), scale_and_needles)
    pygame.draw.circle(screen, (0, 0, 0), 
                       (x + (7 * width_body // 6) + 7, 
                        y + (height_body // 2) - 2), scale_and_needles - 1)
    pygame.draw.circle(screen, (255, 255, 255), 
                       (x + (7 * width_body // 6) - 4, y + (height_body // 2)), 
                       scale_and_needles)
    pygame.draw.circle(screen, (0, 0, 0), 
                       (x + (7 * width_body // 6) - 3, y + (height_body // 2)), 
                       scale_and_needles - 1)
    # Рисование носа
    pygame.draw.circle(screen, (0, 0, 0), 
                       (x + 4 * width_body // 3, y + (height_body // 2) + 4), 
                       scale_and_needles - 1)
    # Рисование ног
    pygame.draw.circle(screen, (63, 61, 58), 
                       (x + width_body // 6, y + height_body), 
                       scale_and_needles + 2)
    pygame.draw.circle(screen, (64, 65, 62), 
                       (x + 2 * width_body // 6, y + height_body), 
                       scale_and_needles + 2)
    pygame.draw.circle(screen, (64, 65, 62), 
                       (x + 4 * width_body // 6, y + height_body), 
                       scale_and_needles + 2)
    pygame.draw.circle(screen, (64, 65, 62), 
                       (x + 5 * width_body // 6, y + height_body), 
                       scale_and_needles + 2)


def mushroom(x, y, scale):
    '''
    Функция рисует гриб случайных цветов (в определённом диапазоне).
    x, y - координаты левого верхнего угла прямоугольника, в который
    вписан эллипс ножки гриба.
    scale - коэффициент масштабирования гриба. При заданном 
    коэффициненте a гриб будет иметь ширину 7a и высоту 8a.
    '''
    # Рисование гриба
    pygame.draw.ellipse(screen, 
                        (randint(156, 216), randint(123, 163), 
                         randint(123, 163)), (x, y, 3 * scale, 7 * scale))
    pygame.draw.ellipse(screen, 
                        (randint(0, 155), randint(0, 155), randint(0, 155)), 
                        (x - 2 * scale, y - scale, 7 * scale, 3 * scale))


# Инициализация библиотеки pygame
pygame.init()

# Задание начальных параметров, таких как FPS, размер окна, цвет 
# фона, заголовок окна
FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill([44, 77, 50])
pygame.display.set_caption("My program")

# Рисование кустов на заднем фоне
for i in range(100):
    pygame.draw.circle(screen, 
                       (randint(50, 109), randint(70, 120), randint(20, 50)),
                       (randint(0, 500), randint(350, 500)), randint(30, 60))

# Рисование земли
pygame.draw.rect(screen, (46, 35, 35), ((0, 500), (500, 200)))

# Рисование стволов деревьев
pygame.draw.rect(screen, (105, 60, 55), ((0, 0), (75, 650)))
pygame.draw.rect(screen, (125, 80, 75), ((0, 0), (25, 650)))
pygame.draw.rect(screen, (84, 60, 70), ((200, 0), (70, 550)))
pygame.draw.rect(screen, (135, 101, 124), ((200, 0), (20, 550)))
pygame.draw.rect(screen, (135, 82, 76), ((430, 0), (50, 700)))
pygame.draw.rect(screen, (157, 109, 93), ((430, 0), (15, 700)))

# Рисование листвы у деревьев
pygame.draw.rect(screen, (92, 105, 68), ((0, 0), (500, 150)))
for i in range(100):
    pygame.draw.circle(screen, 
                       (randint(90, 159), randint(110, 170), randint(60, 90)), 
                       (randint(-100, 500), randint(-10, 200)), randint(5, 60))

# Выбор места для расположения и рисование грибов
for i in range(7):
    x_mushroom = randint(75, 400)
    y_mushroom = randint(525, 700)
    mushroom(x_mushroom, y_mushroom, 5)

# Рисование ёжиков
hedgehog(315, 550, 100, 60, 5)
hedgehog(50, 600, 200, 120, 10)
hedgehog(75, 475, 60, 40, 3)

# Проявление изображения на экране и задание параметров для игрового
# цикла
pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Игровой цикл
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

# Окончание работы библиотеки pygame
pygame.quit()
