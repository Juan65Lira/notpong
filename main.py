import pygame as pg

UP = -1
NONE = 0
DOWN = 1


class Pallet:
    WIDTH = 30
    HEIGHT = 100
    COLOR = pg.Color('white')
    SPEED = 500

    def __init__(self, game, x: int, y: int):
        self.game = game
        self.hitbox = pg.Rect(x, y, self.WIDTH, self.HEIGHT)

    def move(self, direction: int):
        self.hitbox.move_ip((0, self.SPEED/60 * direction))
        self.hitbox.clamp_ip(self.game.screen_rect)

    def draw(self):
        pg.draw.rect(self.game.screen, self.COLOR, self.hitbox)


class Ball:
    WIDTH = 20
    HEIGHT = 20
    COLOR = pg.Color('white')

    def __init__(self, game):
        self.game = game
        self.hitbox = pg.Rect(
            game.width//2 - self.WIDTH//2,
            game.height//2 - self.HEIGHT//2,
            self.WIDTH,
            self.HEIGHT
        )

    def draw(self):
        pg.draw.rect(self.game.screen, self.COLOR, self.hitbox)


class NotPong:
    width = 800
    height = 600

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen_rect = self.screen.get_rect()

        gap = self.width // 30
        y = self.height//2 - Pallet.HEIGHT//2
        self.left_plt = Pallet(self, gap, y)
        self.right_plt = Pallet(self, self.width - gap - Pallet.WIDTH, y)
        self.ball = Ball(self)

    def mainloop(self):
        clock = pg.time.Clock()

        running = True
        while running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False
                elif ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_ESCAPE:
                        running = False

            keys = pg.key.get_pressed()

            if keys[pg.K_UP]:
                self.right_plt.move(UP)
            if keys[pg.K_DOWN]:
                self.right_plt.move(DOWN)

            if keys[pg.K_w]:
                self.left_plt.move(UP)
            if keys[pg.K_s]:
                self.left_plt.move(DOWN)

            self.screen.fill(pg.Color('black'))
            self.left_plt.draw()
            self.right_plt.draw()
            self.ball.draw()
            pg.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    NotPong().mainloop()
