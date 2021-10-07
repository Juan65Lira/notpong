import pygame as pg


class Pallet:
    WIDTH = 30
    HEIGHT = 100
    COLOR = pg.Color('white')

    def __init__(self, x: int, y: int):
        self.hitbox = pg.Rect(x, y, self.WIDTH, self.HEIGHT)

    def draw(self, surface):
        pg.draw.rect(surface, self.COLOR, self.hitbox)


class NotPong:
    width = 800
    height = 600

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((self.width, self.height))

        gap = self.width // 30
        y = self.height//2 - Pallet.HEIGHT//2
        self.left_plt = Pallet(gap, y)
        self.right_plt = Pallet(self.width - gap - Pallet.WIDTH, y)

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

            self.screen.fill(pg.Color('black'))
            self.left_plt.draw(self.screen)
            self.right_plt.draw(self.screen)
            pg.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    NotPong().mainloop()
