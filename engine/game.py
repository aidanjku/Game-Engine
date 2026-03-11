import pygame

class Game:
    def __init__(self, width=800, height=600, title="My Engine"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self):
        self.screen.fill((30, 30, 30))
        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)