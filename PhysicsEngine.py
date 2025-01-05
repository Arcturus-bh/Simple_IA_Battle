import math
import pygame

class PhysicsEngine:
    def __init__(self, playground_limits: dict):
        super().__init__()
        self.playground_limits = playground_limits
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update_entities_physics(self, entity, keys, delta_time):
        dx, dy = 0, 0
        if keys[pygame.K_UP] or keys[pygame.K_z]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_q]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1

        # Si une direction est valide
        if dx != 0 or dy != 0:
            new_angle = math.atan2(dy, dx)  # Trouve l'angle de direction
            if entity.previous_angle is None or abs(new_angle - entity.previous_angle) < float(0.01):
                entity.current_speed += entity.acceleration * delta_time
                entity.current_speed = min(entity.current_speed, entity.max_speed)
            else:
                entity.current_speed -= entity.acceleration * delta_time
                entity.current_speed = max(entity.current_speed, entity.base_speed)
            #self.move(limits, new_angle, delta_time)


    def update(self, screen, delta_time, keys):
        for entity in self.entities:
            self.update_entities_physics(entity, keys, delta_time)
            pygame.draw.rect(screen, entity.entity_color, entity.rect)
