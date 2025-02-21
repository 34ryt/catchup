from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Catch up')

#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))

#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
x1 = 200
x2 = 400
y1 = 300
y2 = 300

#создай игровой цикл
fps = 60
speed = 10
clock = time.Clock()
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_pressed[K_a] and x2 > 0:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 600:
        x2 += speed
    if keys_pressed[K_w] and y2 > 0:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    if x1 == x2 and y1 == y2:
        print('Player touched Player')
    display.update()
    clock.tick(fps)

#обработай событие «клик по кнопке "Закрыть окно"»