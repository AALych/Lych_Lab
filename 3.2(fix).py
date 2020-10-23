import pygame
from pygame.draw import *

pygame.init()
'''
Не успела доделать программу до конца, 
расположение мороженого и шарика не меняется
'''
FPS = 30
# параметры экрана
scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))

# Параметры рисования людей
human_height = 300  # рост человека, используется для всех людей
human_xcor = 180  # абсцисса верхней точки первого человека
human_ycor = 500  # ордината верхней точки первого человека
man_hands_cos = 0.4  # косинус угла наклона руки мужчины
woman_hands_cos = 0.5  # косинус угла наклона руки женщины
order_of_people = '1001'  # порядок рисования людей (0 - женщина, 1 - мужчина)
par_of_folding = [[1, 1], [1, 0],  # параметры сгиба конечностей у 4 человек
                  [0, 1], [1, 1]]  # номер строки - номер человека,
# первый элемент строки - параметр сгиба левой руки,
# второй элемент строки - параметр сгиба правой руки.
# 1 - разогнута, 0 - согнута

# Цветовая гамма
Orange = (255, 178, 0)
Human = (255, 218, 185)
Gray = (128, 128, 128)
Pink = (255, 20, 147)
Black = (0, 0, 0)
SkyBlue = (135, 206, 235)
ForestGreen = (34, 139, 34)
Red = (255, 0, 0)
Maroon = (128, 0, 0)
White = (255, 255, 255)


def draw_man(surface, x, y, height, k_left, k_right):
    '''
    Функция рисует мужчину
    surface - объект pygame.Surface
    x, y - координаты самой нижней средней точки, от которой будет нарисован мужчина
    height - высота человека
    k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
    '''

    def draw_mans_body(surface, x, y, width, height, color):
        '''
        Функция рисует тело
        surface - объект pygame.Surface
        x, y - координаты нижней точки тела
        wight, height - ширина и высота
        color - цвет изображения
        '''
        ellipse(surface, color, (x - width // 2, y - height, width, height))

    def draw_mans_head(surface, x, y, width, color):
        '''
        Функция рисует голову
        surface - объект pygame.Surface
        x, y - координаты нижней точки головы
        wight - диаметр
        color - цвет изображения 
        '''
        circle(surface, color, (x, y - width // 2), width // 2)

    def draw_mans_hands(surface, x, y, width, cos, length, color,
                        k_left, k_right):
        '''
        Функция рисует руки
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине между плечами
        width - ширина туловища
        length - длина руки
        cos - косинус угла наклона рук
        color - цвет изображения
        k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
        '''
        sin = (1 - cos ** 2) ** (1 / 2)
        lines(surface, color, False,
              [(x - width // 4, y),
               (x - width // 4 - int(length * cos) // 2,
                y + int(length * sin) // 2),
               (x - width // 4 - int(length * cos),
                y + int(length * sin) * k_left)])
        lines(surface, color, False,
              [(x + width // 4, y),
               (x + width // 4 + int(length * cos) // 2,
                y + int(length * sin) // 2),
               (x + width // 4 + int(length * cos),
                y + int(length * sin) * k_right)])

    def draw_mans_legs(surface, x, y, width, height, length, color):
        '''
        Функция рисует ноги
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине тела на высоте начала ног
        width - ширина тела
        height - высота ног
        length - длина ступни
        color - цвет изображения
        '''
        a = 0.2  # случайный параметр для наклона ноги ( при a = 0 наклон отсутствует)
        lines(surface, color, False,
              [(x - width // 4, y),
               (x - width // 4 - int(a * height), y + height),
               (x - width // 4 - int(a * height) - length, y + height)])
        lines(surface, color, False, [(x + width // 4, y),
                                      (x + width // 4, y + height),
                                      (x + width // 4 + length, y + height)])

    # ширина человека
    width = height // 4

    # тело
    body_y = y - height // 3
    body_color = Gray
    body_height = height // 2

    # голова
    head_y = y - height * 4 // 5
    head_width = height // 5
    head_color = Human

    # руки
    hands_y = int(body_y - body_height * 0.9)
    hands_cos = 0.4
    hands_length = height // 3
    hands_color = Black

    # ноги
    legs_y = body_y - body_height // 10
    legs_height = y - legs_y
    legs_length = legs_height // 4
    legs_color = Black

    # непосредственно рисование
    draw_mans_body(surface, x, body_y, width, body_height, body_color)
    draw_mans_head(surface, x, head_y, head_width, head_color)
    draw_mans_hands(surface, x, hands_y, width, hands_cos, hands_length,
                    hands_color, k_left, k_right)
    draw_mans_legs(surface, x, legs_y, width, legs_height, legs_length,
                   legs_color)


def draw_woman(surface, x, y, height, k_left, k_right):
    # Функция рисует женщину
    # surface - объект pygame.Surface
    # x, y - координаты самой нижней средней точки, от которой будет нарисована женщина
    # k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
    # height - высота человека

    def draw_womans_body(surface, x, y, width, height, color):
        '''
        Функция рисует тело
        surface - объект pygame.Surface
        x, y - координаты нижней точки тела
        wight, height - ширина и высота
        color - цвет изображения 
        '''
        polygon(surface, color, [(x, y - height), (x + width // 2, y),
                                 (x - width // 2, y)])

    def draw_womans_head(surface, x, y, width, color):
        '''
        Функция рисует голову
        surface - объект pygame.Surface
        x, y - координаты нижней точки головы
        wight - диаметр
        color - цвет изображения 
        '''
        circle(surface, color, (x, y - width // 2), width // 2)

    def draw_womans_hands(surface, x, y, width, cos, length, color,
                          k_left, k_right):
        '''
        Функция рисует руки
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине между плечами
        width - ширина туловища
        length - длина руки
        cos - косинус угла наклона рук
        color - цвет изображения
        k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
        '''
        sin = (1 - cos ** 2) ** (1 / 2)  # считаем синус угла
        lines(surface, color, False,
              [(x - width // 8, y),
               (x - width // 8 - int(length * cos) // 2,
                y + int(length * sin) // 2),
               (x - width // 8 - int(length * cos),
                y + int(length * sin) * k_left)])
        lines(surface, color, False,
              [(x + width // 8, y),
               (x + width // 8 + int(length * cos) // 2,
                y + int(length * sin) // 2),
               (x + width // 8 + int(length * cos),
                y + int(length * sin) * k_right)])

    def draw_womans_legs(surface, x, y, width, height, length, color):
        '''
        Функция рисует ноги
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине тела на высоте начала ног
        width - ширина тела
        height - высота ног
        length - длина ступни
        color - цвет изображения
        '''
        lines(surface, color, False,
              [(x - width // 6, y), (x - width // 6, y + height),
               (x - width // 6 - length, y + height)])
        lines(surface, color, False,
              [(x + width // 6, y), (x + width // 6, y + height),
               (x + width // 6 + length, y + height)])

    # ширина человека
    width = height // 3

    # тело
    body_y = y - height // 3
    body_color = Pink
    body_height = int(height // 1.75)

    # голова
    head_y = y - height * 4 // 5
    head_width = height // 5
    head_color = Human

    # руки
    hands_y = int(body_y - body_height * 0.8)
    hands_cos = 0.5
    hands_length = int(height // 2.5)
    hands_color = Black

    # ноги
    legs_y = body_y
    legs_height = y - legs_y
    legs_length = legs_height // 4
    legs_color = Black

    # непосредственно рисование
    draw_womans_body(surface, x, body_y, width, body_height, body_color)
    draw_womans_head(surface, x, head_y, head_width, head_color)
    draw_womans_hands(surface, x, hands_y, width, hands_cos, hands_length,
                      hands_color, k_left, k_right)
    draw_womans_legs(surface, x, legs_y, width, legs_height, legs_length,
                     legs_color)


def draw_icecream(surface, x, y, height, color1, color2, color3):
    '''
    Функция рисует мороженое
    surface - объект pygame.Surface
    x, y - координаты нижней точки рожка
    height - высота
    color1, color2, color3 - цвета шариков мороженого
    '''

    def draw_cone(surface, x, y, width, height, color):
        '''
        Функция рисует рожок
        surface - объект pygame.Surface
        x, y - координаты нижней точки
        width - ширина
        height - высота
        color - цвет
        '''
        polygon(surface, color, [(x, y), (x + width // 2, y - height),
                                 (x - width // 2, y - height)])

    def draw_ball_1(surface, x, y, r, color):
        '''
        Функция рисует первый шарик мороженого
        surface - объект pygame.Surface
        x, y - координаты центра
        r - радиус шарика
        color - цвет шарика
        '''
        circle(surface, color, (x, y), r)

    def draw_ball_2(surface, x, y, r, color):
        '''
        Функция рисует второй шарик мороженого
        surface - объект pygame.Surface
        x, y - координаты центра
        r - радиус шарика
        color - цвет шарика
        '''
        circle(surface, color, (x, y), r)

    def draw_ball_3(surface, x, y, r, color):
        '''
        Функция рисует третий шарик мороженого
        surface - объект pygame.Surface
        x, y - координаты центра
        r - радиус шарика
        color - цвет шарика
        '''
        circle(surface, color, (x, y), r)

    # рожок
    cone_height = height * 3 // 5
    cone_color = Orange
    cone_width = height * 8 // 15

    # радиус шариков
    r = height * 2 // 15

    # первый шарик
    ball_1_x = x - r
    ball_1_y = y - cone_height - r

    # второй шарик
    ball_2_x = x + r
    ball_2_y = y - cone_height - r

    # третий шарик
    ball_3_x = x
    ball_3_y = ball_1_y - r

    # непосредственно рисование
    draw_cone(surface, x, y, cone_width, cone_height, cone_color)
    draw_ball_1(surface, ball_1_x, ball_1_y, r, color1)
    draw_ball_2(surface, ball_2_x, ball_2_y, r, color2)
    draw_ball_3(surface, ball_3_x, ball_3_y, r, color3)


def draw_balloon(surface, x, y, height, color):
    '''
    Функция рисует воздушный шарик
    surface - объект pygame.Surface
    x, y - координаты нижней точки веревки
    height - высота шарика вместе с веревкой
    color - цвет шарика
    '''

    def draw_rope(surface, x, y, length):
        '''
        Функция рисует веревку
        surface - объект pygame.Surface
        x, y - координаты нижней точки
        length - длина веревки
        '''
        line(surface, Black, (x, y), (x, y - length))

    def draw_main_balloon(surface, x, y, height, color):
        '''
        Функция рисует основу шарика
        surface - объект pygame.Surface
        x, y - координаты нижней точки
        height - высота шарика
        color - цвет шарика
        '''
        polygon(surface, color,
                [(x, y), (x + height * 2 // 5, y - height * 4 // 5),
                 (x - height * 2 // 5, y - height * 4 // 5)])
        circle(surface, color, (x + height // 5, y - height * 4 // 5),
               height // 5)
        circle(surface, color, (x - height // 5, y - height * 4 // 5),
               height // 5)

    # веревка
    rope_length = height * 3 // 5

    # основа шарика
    main_y = y - rope_length
    main_height = height - rope_length

    # непосредственно рисование
    draw_rope(surface, x, y, rope_length)
    draw_main_balloon(surface, x, main_y, main_height, color)


def people_draw(surface, x, y, h, order, par):
    '''
    Функция рисует воздушный шарик
    surface - объект pygame.Surface
    x, y - координаты верхней точки первого человека
    h - высота человека
    order - порядок людей на рисунке
    par - список параметров сгиба рук у людей
    '''
    for i in range(0, 4):
        if int(order[i]) == 1:
            draw_man(surface, x, y, h, par[i][0], par[i][1])
            x += int(h // 16 + h // 3 * man_hands_cos)
            if i != 3:
                if int(order[i + 1]) == 1:
                    x += int(h // 16 + h // 3 * man_hands_cos)
                else:
                    x += int(h // 18 + h // 2.5 * woman_hands_cos)
        else:
            draw_woman(surface, x, y, h, par[i][0], par[i][1])
            x += int(h // 18 + h // 2.5 * woman_hands_cos)
            if i != 3:
                if int(order[i + 1]) == 1:
                    x += int(h // 16 + h // 3 * man_hands_cos)
                else:
                    x += int(h // 18 + h // 2.5 * woman_hands_cos)


rect(screen, SkyBlue, (0, 0, scr_width, scr_height // 2))
rect(screen, ForestGreen, (0, scr_height // 2,
                           scr_width, scr_height // 2))
people_draw(screen, human_xcor, human_ycor, human_height,
            order_of_people, par_of_folding)
draw_icecream(screen, 390, 265, 100, Black, White, Maroon)
draw_icecream(screen, 660, 355, 60, White, Red, Maroon)
draw_balloon(screen, 122, 355, 300, Red)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
