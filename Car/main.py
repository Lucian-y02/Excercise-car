from os import path

import pygame


class Car(pygame.sprite.Sprite):
    car_image = pygame.image.load(path.join("data", "car2.png"))

    def __init__(self, screen_width, *args):
        super(Car, self).__init__(*args)
        self.image = self.car_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.screen_width = screen_width
        self.step = 2

    def update(self, *args):
        self.rect.move_ip(self.step, 0)
        if (self.rect.x + self.rect.width) >= self.screen_width:
            self.step = -2
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x <= 0:
            self.step = 2
            self.image = pygame.transform.flip(self.image, True, False)


class Game:
    def __init__(self, **kwargs):
        self.size = kwargs.get("size", (600, 400))
        self.bg_color = kwargs.get("bg_color", (0, 0, 0))
        self.title = kwargs.get("title", "New Game")
        self.FPS = kwargs.get("FPS", 30)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        self.objects_groups = dict()

    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def game_update(self):
        for group in self.objects_groups.values():
            group.update()

    def game_render(self):
        self.screen.fill(self.bg_color)
        for group in self.objects_groups.values():
            group.draw(self.screen)

    def add_group(self, name):
        self.objects_groups[name] = pygame.sprite.Group()

    def play(self):
        while self.game_events():
            self.game_update()
            self.game_render()

            pygame.display.flip()
            self.clock.tick(self.FPS)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game(size=(600, 95), bg_color=(255, 255, 255), title="Машинка", FPS=30)
    game.add_group("car")
    car = Car(game.size[0], game.objects_groups["car"])
    game.play()
