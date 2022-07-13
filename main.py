import pygame as pg
from time import sleep
pg.init()
WIDTH, HEIGHT = 720, 500  # Width and height of the window
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont("comicsansms", 72)


class Ball:

    def __init__(self):
        self.x = WIDTH / 2 - 15 / 2
        self.y = HEIGHT / 2 - 15 / 2
        self.initial_x = WIDTH / 2 - 15 / 2
        self.initial_y = HEIGHT / 2 - 15 / 2
        self.position = pg.Rect(self.x, self.y, 15, 15)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        if self.y >= HEIGHT - 15 or self.y <= 0:
            self.speed_y *= -1
        self.y += self.speed_y
        self.position = pg.Rect(self.x, self.y, 15, 15)

        if self.x >= WIDTH - 15 or self.x <= 0:
            self.speed_x *= -1
        self.x += self.speed_x

    def reset(self):
        ball.x, ball.y = ball.initial_x, ball.initial_y
        player1.y, player2.y = player1.initial_y, player2.initial_y
        sleep(2)
        

class Player:

    def __init__(self, player):
        self.width = 10
        self.height = 50
        self.player = player
        if self.player == 0:
            self.x = self.width / 2
        elif self.player == 1:
            self.x = WIDTH - self.width / 2 - self.width
        
        self.initial_y = HEIGHT / 2 - 50 / 2
        self.y = HEIGHT / 2 - 50 / 2
        self.points = 0
        self.controls = [[pg.K_UP, pg.K_z], [pg.K_DOWN, pg.K_s]]
        self.position = pg.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if pg.key.get_pressed()[self.controls[1][self.player]]:
            self.y += 10
    
        if pg.key.get_pressed()[self.controls[0][self.player]]:
            self.y -= 10
        
        self.position = pg.Rect(self.x, self.y, self.width, self.height)

ball = Ball()
player1 = Player(0)
player2 = Player(1)
running = True

while running:
    clock.tick(60)  # Number of FPS
    WINDOW.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    text = font.render(str(player1.points), False, (0,255,255))
    WINDOW.blit(text,((WIDTH*25)/100,(HEIGHT*25)/100 ))
    text = font.render(str(player2.points),False, (0,255,255))
    WINDOW.blit(text,((WIDTH*75)/100,(HEIGHT*25)/100 ))

    if player1.points == 10 :
        text_victory = font.render("Player 1 won !", False, (0,255,255))
        WINDOW.blit(text_victory,(200,200))
        pg.display.flip()
        sleep(5)
        running = False
    elif player2.points == 10:
        text_victory = font.render("Player 2 won !", False, (0,255,255))
        WINDOW.blit(text_victory,(200,200))
        pg.display.flip()
        sleep(5)
        running = False

    if ball.position.colliderect(player1.position):
        ball.x = 15
        ball.speed_x *= -1
    if ball.position.colliderect(player2.position):
        ball.x = WIDTH - 30
        ball.speed_x *= -1

    if ball.x <=0:
        player2.points += 1
        ball.reset()
    elif ball.x >= WIDTH-15:
        player1.points += 1
        ball.reset()

    player1.move()
    player2.move()
    pg.draw.rect(WINDOW, (0, 255, 255), ball.position)
    pg.draw.rect(WINDOW, (0, 255, 255), player1.position)
    pg.draw.rect(WINDOW, (0, 255, 255), player2.position)
    ball.move()
    pg.display.flip()

pg.quit()