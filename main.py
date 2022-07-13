import pygame as pg

WIDTH, HEIGHT = 720, 500  # Width and height of the window
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


class Ball:
    def __init__(self):
        self.x = WIDTH / 2 - 15 / 2
        self.y = HEIGHT / 2 - 15 / 2
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


class Player:
    def __init__(self, player):
        self.player = player
        if self.player == 0:
            self.x = 10 / 2
        elif self.player == 1:
            self.x = WIDTH - 10 / 2 - 10
        self.y = HEIGHT / 2 - 50 / 2
        self.controls = [[pg.K_UP, pg.K_z], [pg.K_DOWN, pg.K_s]]
        self.position = pg.Rect(self.x, self.y, 10, 50)

    def move(self):
        if pg.key.get_pressed()[self.controls[1][self.player]]:
            self.y += 10
        self.position = pg.Rect(self.x, self.y, 10, 50)

        if pg.key.get_pressed()[self.controls[0][self.player]]:
            self.y -= 10


ball = Ball()
player1 = Player(0)
player2 = Player(1)
running = True

while running:
    clock.tick(60)  # Number of FPS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if ball.position.colliderect(player1.position):
        ball.x = 15
        ball.speed_x *= -1
    if ball.position.colliderect(player2.position):
        ball.x = WIDTH - 30
        ball.speed_x *= -1

    WINDOW.fill((0, 0, 0))
    player1.move()
    player2.move()
    pg.draw.rect(WINDOW, (0, 255, 255), ball.position)
    pg.draw.rect(WINDOW, (0, 255, 255), player1.position)
    pg.draw.rect(WINDOW, (0, 255, 255), player2.position)
    ball.move()

    pg.display.flip()


pg.quit()
