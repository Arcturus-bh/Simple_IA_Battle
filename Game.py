import env
import pygame
from Entity import Entity
from PhysicsEngine import PhysicsEngine


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(env.TITLE)
        self.width = env.WIDTH
        self.height = env.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playground_limits = {}
        self.load_playground_limits(env.WHITE)
        self.physics_engine = PhysicsEngine(self.playground_limits)
        self.running = True
        self.run()

    def load_playground_limits(self, color) -> None:
        self.playground_limits['width'] = self.width * 0.9
        self.playground_limits['height'] = self.height * 0.9
        self.playground_limits['x_offset'] = (self.width -  self.playground_limits['width']) / 2
        self.playground_limits['y_offset'] = (self.height - self.playground_limits['height']) / 2
        self.playground_limits['color'] = color

    def draw_playground(self):
        limits = self.playground_limits
        pygame.draw.rect(self.screen, limits['color'],(limits['x_offset'], limits['y_offset'], limits['width'], limits['height']), 3)

    def draw_DEBUG(self):
        font = pygame.font.Font(None, 24)
        log_surface = font.render(f"current_speed: {self.physics_engine.entities[0].current_speed:.2f}", True, (255, 255, 255))
        self.screen.blit(log_surface, (10, self.height - 30))  # Affiche le texte en bas à gauche

    def run(self) -> None:
        clock = pygame.time.Clock()
        self.physics_engine.add_entity(Entity('ally', env.GREEN, self.width, self.height))
        while self.running:
            delta_time = clock.tick(env.FPS) / 1000
            # ---
            self.screen.fill((0, 0, 0))  # nettoie la fenêtre de jeu
            self.draw_DEBUG()
            self.draw_playground()
            # ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
            keys = pygame.key.get_pressed()
            self.physics_engine.update_entities_physics(self.screen, delta_time, keys)
            pygame.display.flip()

        pygame.quit()
